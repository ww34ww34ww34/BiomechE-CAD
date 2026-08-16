#!/usr/bin/env python3
"""BiomechE-CAD geometry-engine Q0 runner.

Runs candidate-neutral native or Emscripten smoke builds and records truthful
machine-readable evidence. It does not interpret NOT_EXECUTED as PASS/FAIL and
it does not repair CI.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def run(cmd: list[str], cwd: Path | None = None) -> dict:
    started = time.perf_counter()
    p = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True)
    return {
        "command": cmd,
        "exitCode": p.returncode,
        "durationSeconds": time.perf_counter() - started,
        "stdout": p.stdout,
        "stderr": p.stderr,
    }


def version(cmd: list[str]) -> str | None:
    try:
        p = subprocess.run(cmd, text=True, capture_output=True, timeout=10)
        text = (p.stdout or p.stderr).strip()
        return text.splitlines()[0] if text else None
    except (OSError, subprocess.SubprocessError):
        return None


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def locate_output(build: Path, wasm: bool) -> list[Path]:
    patterns = ["**/biomeche_geometry_q0_smoke.js", "**/biomeche_geometry_q0_smoke.wasm"] if wasm else [
        "**/biomeche_geometry_q0_smoke",
        "**/biomeche_geometry_q0_smoke.exe",
    ]
    out: list[Path] = []
    for pattern in patterns:
        out.extend(p for p in build.glob(pattern) if p.is_file())
    return sorted(set(out))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidate", required=True, choices=["opensubdiv", "opennurbs"])
    ap.add_argument("--source-root", required=True, type=Path)
    ap.add_argument("--mode", choices=["native", "wasm"], default="native")
    ap.add_argument("--build-dir", type=Path)
    ap.add_argument("--result", type=Path)
    ap.add_argument("--clean", action="store_true")
    args = ap.parse_args()

    build = (args.build_dir or ROOT / "_build" / f"{args.candidate}-{args.mode}").resolve()
    result_path = (args.result or ROOT / "results" / f"q0-{args.candidate}-{args.mode}.json").resolve()
    source_root = args.source_root.resolve()
    wasm = args.mode == "wasm"

    if args.clean and build.exists():
        shutil.rmtree(build)
    build.mkdir(parents=True, exist_ok=True)
    result_path.parent.mkdir(parents=True, exist_ok=True)

    configure = [
        "cmake", "-S", str(ROOT), "-B", str(build),
        "-DCMAKE_BUILD_TYPE=Release",
        f"-DBIOMECHE_Q0_CANDIDATE={args.candidate}",
    ]
    if args.candidate == "opensubdiv":
        configure.append(f"-DBIOMECHE_OPENSUBDIV_ROOT={source_root}")
    else:
        configure.append(f"-DBIOMECHE_OPENNURBS_ROOT={source_root}")

    if wasm:
        if shutil.which("emcmake") is None:
            payload = {
                "schema": "BiomechE.CAD.GeometryEngineQ0Result/1",
                "candidateId": args.candidate,
                "mode": args.mode,
                "status": "NOT_EXECUTED",
                "reason": "emcmake_not_found",
            }
            result_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
            print(json.dumps(payload))
            return 3
        configure = ["emcmake", *configure]

    evidence = {
        "schema": "BiomechE.CAD.GeometryEngineQ0Result/1",
        "candidateId": args.candidate,
        "mode": args.mode,
        "status": "EXECUTING",
        "host": {
            "platform": platform.platform(),
            "architecture": platform.machine(),
            "python": sys.version.split()[0],
        },
        "toolchain": {
            "cmake": version(["cmake", "--version"]),
            "cxx": version([os.environ.get("CXX", "c++"), "--version"]),
            "emcc": version(["emcc", "--version"]) if wasm else None,
        },
        "sourceRoot": str(source_root),
        "buildDir": str(build),
        "configure": None,
        "build": None,
        "runtime": None,
        "artifacts": [],
    }

    evidence["configure"] = run(configure)
    if evidence["configure"]["exitCode"] != 0:
        evidence["status"] = "FAIL_CONFIGURE"
        result_path.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
        return 10

    evidence["build"] = run(["cmake", "--build", str(build), "--config", "Release"])
    if evidence["build"]["exitCode"] != 0:
        evidence["status"] = "FAIL_BUILD"
        result_path.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
        return 11

    artifacts = locate_output(build, wasm)
    evidence["artifacts"] = [
        {"path": str(p), "sizeBytes": p.stat().st_size, "sha256": sha256(p)} for p in artifacts
    ]

    if wasm:
        js = next((p for p in artifacts if p.suffix == ".js"), None)
        if js and shutil.which("node"):
            evidence["runtime"] = run(["node", str(js)])
        else:
            evidence["runtime"] = {"status": "NOT_EXECUTED", "reason": "node_or_js_missing"}
    else:
        exe = next((p for p in artifacts if p.suffix == ".exe" or p.name == "biomeche_geometry_q0_smoke"), None)
        evidence["runtime"] = run([str(exe)]) if exe else {"status": "NOT_EXECUTED", "reason": "executable_not_found"}

    runtime_ok = isinstance(evidence["runtime"], dict) and evidence["runtime"].get("exitCode") == 0
    evidence["status"] = "PASS_SMOKE" if runtime_ok else "BUILD_PASS_RUNTIME_NOT_PASS"
    result_path.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": evidence["status"], "result": str(result_path)}))
    return 0 if runtime_ok else 12


if __name__ == "__main__":
    raise SystemExit(main())
