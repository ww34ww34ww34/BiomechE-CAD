# BiomechE-CAD — Fixture Validation Report — 2026-08-15

**Status:** PASS — first CI-qualified kernel-independent rich-fixture batch  
**Repository:** `ww34ww34ww34/BiomechE-CAD`  
**Branch:** `main`  
**Validated commit:** `4c248a134ebc6b982ba5fbf691ddd97116fe8567`  
**GitHub Actions workflow:** `Validate project fixtures`  
**Workflow run:** `31849009930` / run number `2`  
**Job:** `validate` / job `94921063350`  
**Runner:** GitHub-hosted Ubuntu 24.04, Python 3.12.13  

---

## 1. Result

```text
Validated fixtures: 15
Failures:           0
Conclusion:         PASS
```

The workflow completed checkout, Python setup, dependency installation, Project Schema/semantic validation and validation-log artifact upload successfully.

Validation artifact:

```text
name:   fixture-validation-log
ID:     9236876009
SHA256: 97b31c1df894438d42d0d6f84457e0a820b32ae4a0d025abaef9012d13e25d77
```

The artifact stores the exact validator console result for this run.

---

## 2. Validated fixtures

Acceptance fixtures:

```text
fixtures/acceptance/biomeche-result-import.json
fixtures/acceptance/blocking-qc.json
fixtures/acceptance/material-property-provenance.json
fixtures/acceptance/mirror-semantics.json
fixtures/acceptance/offload-safety-ring.json
fixtures/acceptance/profile-non-transfer.json
fixtures/acceptance/prom-versioning.json
fixtures/acceptance/registration-known-transform.json
fixtures/acceptance/report-source-exactness.json
fixtures/acceptance/roi-version-comparison.json
```

Project fixtures:

```text
fixtures/project/bilateral-project.json
fixtures/project/manufacturing-qc-lineage.json
fixtures/project/migration-v0.1.json
fixtures/project/minimal-valid-project.json
fixtures/project/pressure-design-outcome-loop.json
```

Every listed file passed JSON Schema Draft 2020-12 validation and the kernel-independent semantic checks implemented by `tools/validate_fixtures.py` for that fixture.

---

## 3. Executed acceptance IDs

The validator reported this exact executed-ID set:

```text
BINT-001
BINT-002
BINT-005
BINT-006
BINT-007
BINT-008

RPT-001
RPT-002
RPT-003
RPT-004
RPT-006
RPT-013
RPT-017

SCHEMA-001
SCHEMA-002
SCHEMA-003
SCHEMA-005
SCHEMA-006
SCHEMA-008
SCHEMA-010
SCHEMA-011
SCHEMA-012
SCHEMA-014
SCHEMA-016
SCHEMA-017
SCHEMA-018
SCHEMA-020
SCHEMA-023
SCHEMA-026
SCHEMA-027
SCHEMA-029
SCHEMA-030

XACC-003
XACC-004
XACC-005
XACC-008
XACC-010
XACC-023
XACC-024
XACC-025
XACC-027
XACC-031
XACC-034
XACC-044
XACC-049
```

This is an **executed subset**, not a claim that every ID in `SCHEMA-001..030`, `XACC-001..050`, `BINT-001..018` or `RPT-001..018` is executable today.

---

## 4. Notable validated semantics

This run establishes executable evidence for the current fixtures that:

```text
- semantic bilateral mirror keeps side-normalized prescription semantics;
- known registration transform follows the frozen source->target convention;
- ROI-version mismatch can block comparison;
- profile non-transfer and confirmation-state guards are enforceable;
- PROM version identity is retained;
- offload target + safety-ring + remote-region structure is retained;
- nominal vs measured material-property provenance remains distinct;
- blocking QC prevents accepted-part state;
- imported BiomechE result bundle is hash-addressed and producer-pinned;
- BiomechE UNAVAILABLE KPI is not fabricated as numeric zero;
- report source refs remain pinned to the historical design revision;
- report bytes/source manifest/generator provenance are retained.
```

---

## 5. CI workflow qualification note

Run number 1 (`31848956735`) failed **before** validator execution because `actions/setup-python` pip caching did not know that the dependency file was `requirements-dev.txt`.

The workflow was corrected to use an explicit:

```yaml
cache-dependency-path: requirements-dev.txt
```

and current Node-24-based action generations:

```text
actions/checkout@v6
actions/setup-python@v6
actions/upload-artifact@v7
```

Run number 2 then completed successfully.

The first failure is retained in Actions history and is not interpreted as a fixture/schema failure.

---

## 6. Scope limitations

This PASS covers:

```text
JSON Schema Draft 2020-12
+ current kernel-independent rich-fixture semantic checks
```

It does **not** yet qualify:

```text
geometry-kernel output
clinical/device measurement accuracy
real scanner/pressure registration tolerance
manufacturing dimensional capability
all SCHEMA/XACC/BINT/RPT IDs
real hardware acquisition repeatability/reproducibility
clinical efficacy
```

Those require their own qualified fixtures/hardware/protocol evidence.

---

## 7. Next executable expansion

Priority order:

```text
1. BINT-011/012 — protocol/cross-device comparison gate
2. BINT-015 — append-only reanalysis
3. RPT-014/015 — report reissue + semantic reproducibility
4. remaining kernel-independent SCHEMA/XACC coverage
5. hardware-backed acquisition/registration qualification
```

No geometry library is required for this expansion.
