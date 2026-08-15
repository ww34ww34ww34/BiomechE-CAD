# BiomechE-CAD — Technical Debt Register

**Status:** ACTIVE  
**Date:** 2026-08-15  
**Purpose:** keep explicitly deferred engineering/verification debt visible without allowing it to silently redefine the product specification.

---

## TD-CI-001 — GitHub Actions / fixture-validation reliability

**Status:** DEFERRED BY PROJECT OWNER — NON-BLOCKING FOR DOCUMENTATION WORK  
**Recorded:** 2026-08-15  
**Area:** CI / validation harness / documentation truthfulness  
**Product-domain impact:** none on frozen semantic contracts; affects confidence in executable verification status only.

### Known condition

The repository currently contains 19 project/acceptance fixtures. Three newer fixtures are not recognized by the current `tools/validate_fixtures.py` harness:

```text
fixtures/acceptance/biomeche-protocol-cross-device-non-comparable.json
fixtures/acceptance/biomeche-reanalysis-append-only.json
fixtures/acceptance/report-reissue-semantic-reproducibility.json
```

The intended acceptance coverage is:

```text
BINT-011/012  protocol + cross-device compatibility
BINT-015      append-only reanalysis
RPT-014/015   report reissue + semantic reproducibility
```

A strict validation attempt on commit `334ba4ce6f6d51c23c9f9c8394eca60046d54263` reported:

```text
Validated fixtures: 19
failures: 3
reason: HARNESS unknown fixture
```

The ordinary workflow also uses a shell pipeline of the form:

```bash
python tools/validate_fixtures.py | tee fixture-validation.log
```

without an explicit `pipefail` guard, so a failing validator can be masked by the exit status of `tee` depending on shell behavior/workflow configuration.

### Project-owner decision

Until this debt is explicitly reopened:

```text
GitHub CI SHALL NOT block documentation/specification progress.
CI green status SHALL NOT be used as evidence that current main is fully qualified.
The historical 16/16 PASS report remains historical evidence for its exact commit only.
No current-main qualification claim may be inferred from it.
```

This decision does **not** waive future executable validation. It only separates product/domain specification work from temporarily unreliable automation infrastructure.

### What continues despite this debt

Documentation work proceeds normally for:

```text
requirement traceability
geometry authoring semantics
workflow/preset/macro semantics
numerical/tolerance governance
scientific evidence integration
manufacturing/device qualification planning
architecture-independent acceptance definitions
```

### What is prohibited while debt is open

Do not:

- advertise current `main` as fully CI-qualified;
- change semantic requirements merely to make an unreliable harness green;
- delete the three newer fixtures because the harness does not know them;
- convert missing executable coverage into a semantic PASS;
- use CI status as the gate for freezing architecture-independent documentation.

### Exit criteria

`TD-CI-001` may be CLOSED only when all of the following are true:

1. `tools/validate_fixtures.py` recognizes all intended current fixtures.
2. The workflow propagates validator failures reliably (`pipefail` or equivalent direct exit-code preservation).
3. Temporary/self-modifying checkpoint workflows are reviewed and removed or normalized as appropriate.
4. Validation is executed against the then-current `main` commit.
5. The resulting fixture count, failures and executed acceptance IDs are recorded in a new validation report.
6. `RESUME_HERE.md` and `SPEC_INDEX.md` are updated to point to that exact qualified state.

### Restart note

When CI work is resumed, begin from this debt item rather than re-auditing the product-domain documentation. The semantic documentation is intentionally allowed to advance independently in the meantime.
