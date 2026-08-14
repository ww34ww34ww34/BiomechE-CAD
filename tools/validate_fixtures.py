#!/usr/bin/env python3
"""Kernel-independent validation for BiomechE-CAD Project Schema v0 fixtures.

Runs JSON Schema Draft 2020-12 first, then semantic checks that can be
executed before a geometry kernel exists. The harness intentionally does not
claim coverage of geometry-dependent SCHEMA/XACC/BINT/RPT/PAQ cases.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError as exc:
    raise SystemExit("Install dev dependency: python -m pip install 'jsonschema>=4.23,<5'") from exc

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "biomeche-cad-project-0.1.schema.json"
GLOBS = ("fixtures/project/*.json", "fixtures/acceptance/*.json")

DEF_TYPES = {
    "baseTemplates": "BaseTemplate",
    "indicationProfiles": "IndicationProfile",
    "presetDefinitions": "PresetDefinition",
    "materialDefinitions": "MaterialDefinition",
    "promInstrumentDefinitions": "PROMInstrument",
    "manufacturingProfiles": "ManufacturingProfile",
    "algorithmDefinitions": "AlgorithmDefinition",
}
ID_FIELDS = {
    "orthosisProjects": "orthosisProjectId",
    "assets": "assetId",
    "frameDefinitions": "frameId",
    "acquisitions": "acquisitionId",
    "registrations": "registrationId",
    "landmarkSets": "landmarkSetId",
    "roiDefinitions": "roiId",
    "designRevisions": "revisionId",
    "outcomeTargets": "targetId",
    "outcomeMeasurements": "measurementId",
    "outcomeComparisons": "comparisonId",
    "promMeasurements": "measurementId",
    "comfortAssessments": "assessmentId",
    "fitUsabilityAssessments": "assessmentId",
    "satisfactionAssessments": "assessmentId",
    "adherenceMeasurements": "measurementId",
    "patientExperienceBundles": "bundleId",
    "materialLots": "lotId",
    "materialRegions": "regionId",
    "materialStacks": "stackId",
    "structuralMaterialRegions": "structuralRegionId",
    "mechanicalPropertyMeasurements": "measurementId",
    "postProcessMaterialStates": "stepId",
    "durabilityTests": "testId",
    "manufacturingRuns": "runId",
    "manufacturingArtifacts": "artifactId",
    "physicalOrthoses": "physicalPartId",
    "qcRequirements": "requirementId",
    "qcMeasurements": "measurementId",
    "serviceStates": "serviceStateId",
    "exportArtifacts": "exportArtifactId",
    "reportArtifacts": "reportArtifactId",
    "provenanceRecords": "provenanceId",
    "auditEvents": "auditEventId",
    "migrationHistory": "migrationId",
}


class Failure(Exception):
    pass


def need(ok: bool, test: str, msg: str) -> None:
    if not ok:
        raise Failure(f"{test}: {msg}")


def h(x: dict) -> tuple[str, str]:
    return x["algorithm"].lower(), x["value"].lower()


def all_ids(p: dict) -> set[str]:
    ids = {p["projectId"], p["patientLink"]["projectPatientId"], p["case"]["caseId"]}
    for bucket, field in ID_FIELDS.items():
        ids.update(x[field] for x in p.get(bucket, []))
    for defs in p["definitions"].values():
        ids.update(x["id"] for x in defs)
    for r in p["designRevisions"]:
        ids.update(x["operationId"] for x in r["operationStack"])
    return ids


def walk_refs(v):
    if isinstance(v, dict):
        if {"entityType", "id", "version"} <= set(v):
            yield v
        for c in v.values():
            yield from walk_refs(c)
    elif isinstance(v, list):
        for c in v:
            yield from walk_refs(c)


def base_checks(p: dict) -> list[str]:
    passed = ["SCHEMA-002"]
    ids = all_ids(p)
    need(len(ids) == len(set(ids)), "SCHEMA-002", "duplicate persistent ID")

    revisions = {r["revisionId"]: r for r in p["designRevisions"]}
    orthoses = {o["orthosisProjectId"]: o for o in p["orthosisProjects"]}
    for o in p["orthosisProjects"]:
        need(o["caseId"] == p["case"]["caseId"], "SCHEMA-003", "orthosis points to another case")
        if o.get("currentDesignRevisionId"):
            r = revisions.get(o["currentDesignRevisionId"])
            need(r is not None and r["orthosisProjectId"] == o["orthosisProjectId"], "SCHEMA-010", "current revision ownership mismatch")
            need(r["side"] == o["side"], "SCHEMA-010", "current revision side mismatch")
    for r in p["designRevisions"]:
        need(r["orthosisProjectId"] in orthoses, "SCHEMA-003", "revision orthosis missing")
        need(r["side"] == orthoses[r["orthosisProjectId"]]["side"], "SCHEMA-010", "revision side mismatch")
        for op in r["operationStack"]:
            need(op["side"] == r["side"], "SCHEMA-010", "operation side mismatch")
            need(op["algorithmRef"].get("algorithmId") and op["algorithmRef"].get("semanticVersion"), "SCHEMA-026", "operation algorithm version missing")
    passed += ["SCHEMA-003", "SCHEMA-010", "SCHEMA-026"] if p["designRevisions"] else ["SCHEMA-003"]

    parents = {r["revisionId"]: r["parentRevisionIds"] for r in p["designRevisions"]}
    visiting, done = set(), set()

    def visit(n):
        if n in done:
            return
        need(n not in visiting, "SCHEMA-005", "revision cycle")
        visiting.add(n)
        for q in parents.get(n, []):
            need(q in revisions and q != n, "SCHEMA-005", "invalid revision parent")
            visit(q)
        visiting.remove(n)
        done.add(n)

    for n in parents:
        visit(n)
    passed.append("SCHEMA-005")

    defs = {}
    for bucket, typ in DEF_TYPES.items():
        for d in p["definitions"].get(bucket, []):
            defs[(typ, d["id"], d["version"])] = d
    for ref in walk_refs(p):
        key = (ref["entityType"], ref["id"], ref["version"])
        if ref["entityType"] in DEF_TYPES.values():
            need(key in defs, "SCHEMA-006", f"definition ref unresolved {key}")
            if ref.get("contentHash"):
                need(h(ref["contentHash"]) == h(defs[key]["contentHash"]), "SCHEMA-006", f"definition hash mismatch {key}")
    passed.append("SCHEMA-006")

    frames = {f["frameId"] for f in p["frameDefinitions"]}
    for r in p["registrations"]:
        need(r["sourceFrameId"] in frames and r["targetFrameId"] in frames, "SCHEMA-011", "registration frame missing")
        need(r["transformData"].get("convention") == "SOURCE_TO_TARGET", "SCHEMA-011", "transform direction implicit/wrong")
    if p["registrations"]:
        passed.append("SCHEMA-011")

    rois = {r["roiId"] for r in p["roiDefinitions"]}
    acquisitions = {a["acquisitionId"] for a in p["acquisitions"]}
    for m in p["outcomeMeasurements"]:
        need(m["designRevisionId"] in revisions, "SCHEMA-014", "outcome revision missing")
        if m.get("acquisitionId"):
            need(m["acquisitionId"] in acquisitions, "SCHEMA-014", "outcome acquisition missing")
        if m.get("roiRef"):
            need(m["roiRef"] in rois, "SCHEMA-012", "outcome ROI missing")
    if p["outcomeMeasurements"]:
        passed += ["SCHEMA-012", "SCHEMA-014"]

    for m in p["promMeasurements"]:
        key = (m["instrumentRef"]["entityType"], m["instrumentRef"]["id"], m["instrumentRef"]["version"])
        need(key in defs and h(m["instrumentRef"]["contentHash"]) == h(defs[key]["contentHash"]), "SCHEMA-016", "PROM definition not exact")
        need(m["designRevisionId"] in revisions, "SCHEMA-016", "PROM revision missing")
    if p["promMeasurements"]:
        passed.append("SCHEMA-016")

    for m in p["mechanicalPropertyMeasurements"]:
        need(m.get("sourceType") and m.get("testMethod"), "SCHEMA-017", "material property provenance incomplete")
    if p["mechanicalPropertyMeasurements"]:
        passed.append("SCHEMA-017")

    runs = {x["runId"]: x for x in p["manufacturingRuns"]}
    arts = {x["artifactId"]: x for x in p["manufacturingArtifacts"]}
    for a in p["manufacturingArtifacts"]:
        need(a["manufacturingRunId"] in runs and a["designRevisionId"] in revisions, "SCHEMA-018", "manufacturing artifact lineage broken")
    for part in p["physicalOrthoses"]:
        need(part["manufacturingRunId"] in runs and part["manufacturingArtifactId"] in arts and part["designRevisionId"] in revisions, "SCHEMA-018", "physical part lineage broken")
    if arts or p["physicalOrthoses"]:
        passed.append("SCHEMA-018")

    reqs = {r["requirementId"]: r for r in p["qcRequirements"]}
    for m in p["qcMeasurements"]:
        req = reqs.get(m["requirementId"])
        need(req is not None, "SCHEMA-020", "QC requirement missing")
        if req["severity"] == "BLOCKING" and m["result"] == "FAIL":
            for part in p["physicalOrthoses"]:
                if part["manufacturingArtifactId"] == m["artifactId"]:
                    need("acceptedAt" not in part and part["lifecycleState"] != "ACCEPTED", "SCHEMA-020", "blocking QC failure accepted")
    if p["qcMeasurements"]:
        passed.append("SCHEMA-020")

    for m in p["migrationHistory"]:
        need(m.get("informationLoss"), "SCHEMA-023", "migration loss state missing")
    if p["migrationHistory"]:
        passed.append("SCHEMA-023")

    for pr in p["provenanceRecords"]:
        for out in pr["outputEntityRefs"]:
            need(out in ids, "SCHEMA-027", f"dangling provenance output {out}")
    if p["provenanceRecords"]:
        passed.append("SCHEMA-027")

    for ap in p["case"]["attachedProfiles"]:
        need(ap["confirmationState"] in {"USER_CONFIRMED", "IMPORTED", "SUGGESTED_NOT_CONFIRMED"}, "SCHEMA-029", "unknown profile confirmation state")
    if p["case"]["attachedProfiles"]:
        passed.append("SCHEMA-029")
    return sorted(set(passed))


def mv(m, p):
    v = [*p, 1.0]
    o = [sum(float(m[r][c]) * v[c] for c in range(4)) for r in range(4)]
    return [o[i] / o[3] for i in range(3)]


def dist(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def acceptance(p: dict) -> list[str]:
    a = p.get("extensions", {}).get("acceptance")
    if not a:
        return []
    fid, out = a["fixtureId"], []
    if fid == "registration-known-transform":
        m = p["registrations"][0]["transformData"]["matrix4x4"]
        for x, y in zip(a["inputPoints"], a["expectedTargetPoints"]):
            need(dist(mv(m, x), y) <= a["numericToleranceMm"], "XACC-008", "known transform mismatch")
        out = ["XACC-008", "SCHEMA-011"]
    elif fid == "mirror-semantics":
        e = a["expected"]
        rs = {r["revisionId"]: r for r in p["designRevisions"]}
        s, d = rs[e["sourceRevisionId"]], rs[e["targetRevisionId"]]
        need(s["side"] == "RIGHT" and d["side"] == "LEFT", "XACC-003", "mirror side wrong")
        for k in ("s", "q"):
            need(s["operationStack"][0]["parameters"][k] == d["operationStack"][0]["parameters"][k], "XACC-003", f"{k} changed")
        need(h(s["contentHash"]) != h(d["contentHash"]), "XACC-004", "mirror reused source revision")
        need(e["roundTripSemanticExactness"], "XACC-005", "roundtrip expectation absent")
        out = ["XACC-003", "XACC-004", "XACC-005"]
    elif fid == "roi-version-comparison":
        e = a["expected"]
        rois = {r["roiId"]: r for r in p["roiDefinitions"]}
        need(e["roiV1Id"] in rois and e["roiV2Id"] in rois, "XACC-010", "ROI history missing")
        c = next(x for x in p["outcomeComparisons"] if x["comparisonId"] == e["comparisonId"])
        need(c["compatibilityState"] == "NOT_COMPARABLE", "XACC-010", "version mismatch compared silently")
        out = ["XACC-010", "SCHEMA-012"]
    elif fid == "profile-non-transfer":
        e = a["expected"]
        need(e["decision"] == "BLOCK", "XACC-024", "cross-profile target not blocked")
        states = {x["profileRef"]["id"]: x["confirmationState"] for x in p["case"]["attachedProfiles"]}
        need("SUGGESTED_NOT_CONFIRMED" in states.values(), "XACC-023", "fixture lacks unconfirmed profile")
        out = ["XACC-023", "XACC-024", "SCHEMA-029"]
    elif fid == "prom-versioning":
        x, y = p["promMeasurements"]
        need((x["instrumentRef"]["id"], x["instrumentRef"]["version"]) != (y["instrumentRef"]["id"], y["instrumentRef"]["version"]), "XACC-025", "PROM history collapsed")
        out = ["XACC-025", "SCHEMA-016"]
    elif fid == "offload-safety-ring":
        e = a["expected"]
        required = {e["targetRoiId"], e["safetyRingRoiId"], *e["remoteRegionRoiIds"]}
        got = {r["roiId"] for r in p["roiDefinitions"]}
        need(required <= got, "XACC-027", "target/safety/remote ROI incomplete")
        out = ["XACC-027"]
    elif fid == "material-property-provenance":
        e = a["expected"]
        ms = {m["measurementId"]: m for m in p["mechanicalPropertyMeasurements"]}
        n, v = ms[e["nominalMeasurementId"]], ms[e["effectiveMeasurementId"]]
        need(n["sourceType"] == "SUPPLIER_NOMINAL" and v["sourceType"] != "SUPPLIER_NOMINAL", "XACC-031", "nominal/effective provenance collapsed")
        out = ["XACC-031", "SCHEMA-017"]
    elif fid == "blocking-qc":
        e = a["expected"]
        part = next(x for x in p["physicalOrthoses"] if x["physicalPartId"] == e["physicalPartId"])
        need("acceptedAt" not in part and part["lifecycleState"] != "ACCEPTED", "XACC-034", "blocking QC leak")
        out = ["XACC-034", "SCHEMA-020"]
    elif fid == "biomeche-result-import":
        e = a["expected"]
        acq = next(x for x in p["acquisitions"] if x["acquisitionType"] == "BIOMECHE_RESULT")
        producer = acq["payload"]["producer"]
        need(producer["commitHash"] == e["producerCommit"], "BINT-002", "producer commit not pinned")
        assets = {x["assetId"]: x for x in p["assets"]}
        need(e["resultAssetId"] in assets and assets[e["resultAssetId"]]["hash"]["algorithm"] == "sha256", "BINT-001", "result bundle not hash-addressed")
        measurements = {x["metric"]: x for x in p["outcomeMeasurements"]}
        need(e["validMetric"] in measurements and measurements[e["validMetric"]].get("value") is not None, "BINT-005", "canonical valid KPI not normalized")
        unavailable = measurements[e["unavailableMetric"]]
        need(unavailable["qualityState"].startswith("UNAVAILABLE"), "BINT-006", "unavailable quality not propagated")
        need("value" not in unavailable, "BINT-007", "unavailable KPI fabricated numeric value")
        need(acq["protocol"].get("sourceDeviceId") and acq["protocol"].get("calibrationId"), "BINT-008", "device/calibration protocol provenance missing")
        out = ["BINT-001", "BINT-002", "BINT-005", "BINT-006", "BINT-007", "BINT-008"]
    elif fid == "report-source-exactness":
        e = a["expected"]
        reports = {x["reportArtifactId"]: x for x in p["reportArtifacts"]}
        report = reports[e["reportArtifactId"]]
        need(e["reportedRevisionId"] in report["sourceRefs"], "RPT-001", "report does not pin reported revision")
        need(e["currentRevisionId"] not in report["sourceRefs"], "RPT-013", "historical report floated to current revision")
        assets = {x["assetId"]: x for x in p["assets"]}
        need(report["assetRef"] in assets and assets[report["assetRef"]]["hash"]["algorithm"] == "sha256", "RPT-002", "report bytes not hash-addressed")
        need(e["sourceManifestAssetId"] in assets and assets[e["sourceManifestAssetId"]]["role"] == "REPORT_SOURCE_MANIFEST", "RPT-003", "semantic source manifest missing")
        gens = [x for x in p["provenanceRecords"] if x["activityType"] == "REPORT_GENERATION"]
        need(gens and gens[0]["softwareBuildRefs"], "RPT-004", "report generator provenance missing")
        ms = {x["measurementId"]: x for x in p["outcomeMeasurements"]}
        report_measurements = [ms[x] for x in report["sourceRefs"] if x in ms]
        need(report_measurements and report_measurements[0]["metric"].startswith("BIOMECHE:"), "RPT-006", "canonical metric source missing")
        need(report_measurements[0]["value"] == e["reportedFullPrecisionValue"], "RPT-017", "fixture lost authoritative precision before display")
        out = ["RPT-001", "RPT-002", "RPT-003", "RPT-004", "RPT-006", "RPT-013", "RPT-017", "XACC-044", "XACC-049"]
    elif fid == "pressure-qualification-profile":
        e = a["expected"]
        profiles = p.get("extensions", {}).get("pressureAcquisitionQualificationProfiles", [])
        need(len(profiles) == 1, "PAQ-001", "fixture must contain exactly one qualification profile")
        q = profiles[0]
        need(q["profileId"] == e["profileId"] and q["version"] == e["profileVersion"] and q.get("contentHash"), "PAQ-001", "qualification profile identity/version/hash incomplete")
        need(q["intendedUse"] == e["intendedUse"] and e["intendedUse"] in q["supportedExamTypes"], "PAQ-002", "intended-use boundary mismatch")
        need(q["deviceDefinition"].get("unitId") == e["unitId"], "PAQ-003", "exact device/unit identity missing")
        need(q["calibrationProtocol"].get("calibrationId") == e["calibrationId"] and q["calibrationProtocol"].get("state") == "VALID", "PAQ-005", "calibration provenance/state mismatch")
        protocol = q["protocolQualification"]
        need(protocol.get("protocolId") == e["protocolId"] and protocol.get("activity") == e["intendedUse"], "PAQ-010", "qualified protocol identity/activity mismatch")
        need(protocol.get("minimumAcceptedSteps") is e["minimumAcceptedSteps"], "PAQ-011", "fixture introduced a hidden universal step count")
        need(q["crossDevicePolicy"].get("default") == e["crossDeviceDefault"], "PAQ-016", "cross-device default guard missing")
        open_rules = [r for r in q["acceptanceRules"] if r.get("limitState") == "OPEN_FIXTURE"]
        need(open_rules and all(r.get("numericLimit") is None for r in open_rules), "PAQ-020", "OPEN qualification limit was silently assigned a number")
        out = ["PAQ-001", "PAQ-002", "PAQ-003", "PAQ-005", "PAQ-010", "PAQ-011", "PAQ-016", "PAQ-020"]
    else:
        raise Failure(f"HARNESS: unknown fixture {fid}")
    missing = set(a.get("testIds", [])) - set(out)
    need(not missing, "HARNESS", f"declared IDs not executed: {sorted(missing)}")
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*")
    ns = ap.parse_args()
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    val = Draft202012Validator(schema, format_checker=FormatChecker())
    files = [ROOT / p for p in ns.paths] if ns.paths else sorted({p for g in GLOBS for p in ROOT.glob(g)})
    failed = 0
    aggregate = set()
    for path in files:
        p = json.loads(path.read_text(encoding="utf-8"))
        errs = sorted(val.iter_errors(p), key=lambda e: list(e.absolute_path))
        if errs:
            failed += 1
            print(f"FAIL {path.relative_to(ROOT)}")
            for e in errs:
                print(f"  JSON-SCHEMA: {e.message}")
            continue
        try:
            passed = ["SCHEMA-001", "SCHEMA-008", "SCHEMA-030"] + base_checks(p) + acceptance(p)
            aggregate.update(passed)
            print(f"PASS {path.relative_to(ROOT)} [{', '.join(sorted(set(passed)))}]")
        except Failure as exc:
            failed += 1
            print(f"FAIL {path.relative_to(ROOT)}\n  {exc}")
    print(f"\nValidated fixtures: {len(files)}; failures: {failed}")
    print("Executed IDs: " + ", ".join(sorted(aggregate)))
    print("Scope: JSON Schema + current kernel-independent rich-fixture semantics; geometry-dependent cases are out of scope.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
