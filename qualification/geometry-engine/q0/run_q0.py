#!/usr/bin/env python3
"""BiomechE-CAD geometry-engine Q0 evidence runner.

Builds the common product-owned Q0 smoke harness against one exact candidate
source pin and records machine-readable evidence. Missing toolchains/sources are
NOT_EXECUTED; a wrong source revision is SOURCE_PIN_MISMATCH; neither is a
candidate FAIL/PASS.
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
from typing import Any

ROOT = Path(__file__).resolve().parent
LOCK_PATH = ROOT / "candidate-lock.json"


def run(cmd: list[str], cwd: Path | None = None, timeout: int | None = None) -> dict[str, Any]:
    started = time.perf_counter()
    try:
        p = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, timeout=timeout)
        return {
            "command": cmd,
            "exitCode": p.returncode,
            "durationSeconds": time.perf_counter() - started,
            "stdout": p.stdout,
            "stderr": p.stderr,
        }
    except (OSError, subprocess.SubprocessError) as exc:
        return {
            "command": cmd,
            "exitCode": None,
            "durationSeconds": time.perf_counter() - started,
            "stdout": "",
            "stderr": str(exc),
            "executionError": type(exc).__name__,
        }


def first_line(cmd: list[str]) -> str | None:
    result = run(cmd, timeout=10)
    text = (result.get("stdout") or result.get("stderr") or "").strip()
    return text.splitlines()[0] if text else None


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_lock(candidate: str) -> dict[str, Any]:
    doc = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    for item in doc["candidates"]:
        if item["candidateId"] == candidate:
            return item
    raise KeyError(candidate)


def git_commit(source_root: Path) -> str | None:
    if shutil.which("git") is None:
        return None
    result = run(["git", "-C", str(source_root), "rev-parse", "HEAD"], timeout=15)
    if result.get("exitCode") != 0:
        return None
    value = result["stdout"].strip()
    return value if len(value) >= 7 else None


def write_result(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=False) + "\n", encoding="utf-8")


def locate_outputs(build: Path, wasm: bool) -> list[Path]:
    patterns = (
        ["**/biomeche_geometry_q0_smoke.js", "**/biomeche_geometry_q0_smoke.wasm"]
        if wasm
        else ["**/biomeche_geometry_q0_smoke", "**/biomeche_geometry_q0_smoke.exe"]
    )
    out: list[Path] = []
    for pattern in patterns:
        out.extend(p for p in build.glob(pattern) if p.is_file())
    return sorted(set(out))


def compiler_command() -> list[str]:
    explicit = os.environ.get("CXX")
    if explicit:
        return [explicit, "--version"]
    if os.name == "nt" and shutil.which("cl"):
        return ["cl"]
    return ["c++", "--version"]


def dependency_probe(executable: Path) -> dict[str, Any]:
    system = platform.system().lower()
    if system == "windows" and shutil.which("dumpbin"):
        return run(["dumpbin", "/dependents", str(executable)], timeout=30)
    if system == "darwin" and shutil.which("otool"):
        return run(["otool", "-L", str(executable)], timeout=30)
    if shutil.which("ldd"):
        return run(["ldd", str(executable)], timeout=30)
    return {"status": "NOT_EXECUTED", "reason": "no_dependency_probe_available"}


def cmake_cache_evidence(build: Path) -> dict[str, Any] | None:
    cache = build / "CMakeCache.txt"
    if not cache.exists():
        return None
    selected_prefixes = (
        "CMAKE_CXX_COMPILER:",
        "CMAKE_CXX_COMPILER_ID:",
        "CMAKE_CXX_COMPILER_VERSION:",
        "CMAKE_CXX_FLAGS:",
        "CMAKE_CXX_FLAGS_RELEASE:",
        "CMAKE_BUILD_TYPE:",
        "CMAKE_GENERATOR:",
        "CMAKE_SYSTEM_NAME:",
        "CMAKE_SYSTEM_PROCESSOR:",
        "BIOMECHE_Q0_CANDIDATE:",
    )
    selected = [
        line for line in cache.read_text(encoding="utf-8", errors="replace").splitlines()
        if line.startswith(selected_prefixes)
    ]
    return {
        "path": str(cache),
        "sha256": sha256(cache),
        "selectedEntries": selected,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidate", required=True, choices=["opensubdiv", "opennurbs"])
    ap.add_argument("--source-root", required=True, type=Path)
    ap.add_argument(
        "--source-commit",
        help="Explicit source commit when source tree has no .git metadata; must match candidate-lock.json",
    )
    ap.add_argument("--mode", choices=["native", "wasm"], default="native")
    ap.add_argument("--build-dir", type=Path)
    ap.add_argument("--result", type=Path)
    ap.add_argument("--clean", action="store_true")
    args = ap.parse_args()

    source_root = args.source_root.resolve()
    build = (args.build_dir or ROOT / "_build" / f"{args.candidate}-{args.mode}").resolve()
    result_path = (args.result or ROOT / "results" / f"q0-{args.candidate}-{args.mode}.json").resolve()
    wasm = args.mode == "wasm"
    lock = load_lock(args.candidate)

    base: dict[str, Any] = {
        "schema": "BiomechE.CAD.GeometryEngineQ0Result/1",
        "candidateId": args.candidate,
        "mode": args.mode,
        "expectedSource": {
            "upstream": lock["upstream"],
            "refType": lock["refType"],
            "ref": lock["ref"],
            "commit": lock["commit"],
            "licensePath": lock["licensePath"],
            "githubLicenseBlobSha": lock["licenseBlobSha"],
        },
        "status": "INITIALIZING",
    }

    if not source_root.is_dir():
        base.update({"status": "NOT_EXECUTED", "reason": "source_root_missing", "sourceRoot": str(source_root)})
        write_result(result_path, base)
        print(json.dumps(base))
        return 3

    actual_git_commit = git_commit(source_root)
    effective_commit = args.source_commit or actual_git_commit
    if effective_commit is None:
        base.update({
            "status": "NOT_EXECUTED",
            "reason": "source_commit_unverified",
            "sourceRoot": str(source_root),
            "hint": "Use a git checkout or pass --source-commit for an exact source archive.",
        })
        write_result(result_path, base)
        print(json.dumps(base))
        return 4

    if effective_commit.lower() != lock["commit"].lower():
        base.update({
            "status": "SOURCE_PIN_MISMATCH",
            "sourceRoot": str(source_root),
            "actualGitCommit": actual_git_commit,
            "declaredSourceCommit": args.source_commit,
            "effectiveSourceCommit": effective_commit,
        })
        write_result(result_path, base)
        print(json.dumps(base))
        return 5

    license_path = source_root / lock["licensePath"]
    if not license_path.is_file():
        base.update({
            "status": "NOT_EXECUTED",
            "reason": "candidate_license_file_missing",
            "expectedLicensePath": str(license_path),
        })
        write_result(result_path, base)
        print(json.dumps(base))
        return 6

    if wasm and shutil.which("emcmake") is None:
        base.update({
            "status": "NOT_EXECUTED",
            "reason": "emcmake_not_found",
            "sourceRoot": str(source_root),
            "effectiveSourceCommit": effective_commit,
            "licenseSha256": sha256(license_path),
        })
        write_result(result_path, base)
        print(json.dumps(base))
        return 7

    if args.clean and build.exists():
        shutil.rmtree(build)
    build.mkdir(parents=True, exist_ok=True)

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
        configure = ["emcmake", *configure]

    evidence: dict[str, Any] = {
        **base,
        "status": "EXECUTING",
        "sourceRoot": str(source_root),
        "sourceIdentity": {
            "actualGitCommit": actual_git_commit,
            "declaredSourceCommit": args.source_commit,
            "effectiveSourceCommit": effective_commit,
            "matchesExpectedCommit": True,
            "licenseSha256": sha256(license_path),
        },
        "host": {
            "platform": platform.platform(),
            "system": platform.system(),
            "architecture": platform.machine(),
            "python": sys.version.split()[0],
        },
        "toolchain": {
            "cmake": first_line(["cmake", "--version"]),
            "cxx": first_line(compiler_command()),
            "emcmake": first_line(["emcmake", "--version"]) if wasm else None,
            "emcc": first_line(["emcc", "--version"]) if wasm else None,
            "node": first_line(["node", "--version"]) if shutil.which("node") else None,
        },
        "buildDir": str(build),
        "configure": None,
        "build": None,
        "cmakeCache": None,
        "runtime": None,
        "dependencyProbe": None,
        "artifacts": [],
    }

    evidence["configure"] = run(configure)
    evidence["cmakeCache"] = cmake_cache_evidence(build)
    if evidence["configure"].get("exitCode") != 0:
        evidence["status"] = "FAIL_CONFIGURE"
        write_result(result_path, evidence)
        return 10

    evidence["build"] = run(["cmake", "--build", str(build), "--config", "Release"])
    evidence["cmakeCache"] = cmake_cache_evidence(build)
    if evidence["build"].get("exitCode") != 0:
        evidence["status"] = "FAIL_BUILD"
        write_result(result_path, evidence)
        return 11

    artifacts = locate_outputs(build, wasm)
    evidence["artifacts"] = [
        {"path": str(p), "sizeBytes": p.stat().st_size, "sha256": sha256(p)} for p in artifacts
    ]

    if wasm:
        js = next((p for p in artifacts if p.suffix == ".js"), None)
        if js and shutil.which("node"):
            evidence["runtime"] = run(["node", str(js)], timeout=60)
        else:
            evidence["runtime"] = {"status": "NOT_EXECUTED", "reason": "node_or_js_missing"}
        evidence["dependencyProbe"] = {"status": "NOT_APPLICABLE", "reason": "wasm_artifact"}
    else:
        exe = next(
            (p for p in artifacts if p.suffix.lower() == ".exe" or p.name == "biomeche_geometry_q0_smoke"),
            None,
        )
        if exe:
            evidence["runtime"] = run([str(exe)], timeout=60)
            evidence["dependencyProbe"] = dependency_probe(exe)
        else:
            evidence["runtime"] = {"status": "NOT_EXECUTED", "reason": "executable_not_found"}
            evidence["dependencyProbe"] = {"status": "NOT_EXECUTED", "reason": "executable_not_found"}

    runtime_ok = isinstance(evidence["runtime"], dict) and evidence["runtime"].get("exitCode") == 0
    evidence["status"] = "PASS_SMOKE" if runtime_ok else "BUILD_PASS_RUNTIME_NOT_PASS"
    write_result(result_path, evidence)
    print(json.dumps({"status": evidence["status"], "result": str(result_path)}))
    return 0 if runtime_ok else 12


if __name__ == "__main__":
    raise SystemExit(main())
