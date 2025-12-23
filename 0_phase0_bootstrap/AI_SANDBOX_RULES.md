# AI Sandbox Execution Rules (L2.5 Single-Agent)

You are the single authorized agent (Cursor Code). You may execute multi-step plans end-to-end.

**Project-Type Awareness:** These rules automatically adapt based on project type (`programming` vs `documentation`). The system detects project type from `MVP_SPECIFICATION.yaml` or `ACTIVE_PLAN.yaml`.

## Allowed

### Programming Projects
- Read `6_ai_runtime_context/ACTIVE_PLAN.yaml` and execute tasks sequentially.
- Write/refactor/delete only in: `frontend/`, `backend/`, `shared/`, `tests/`, `docs/`, `scripts/`.

### Documentation Projects
- Read `6_ai_runtime_context/ACTIVE_PLAN.yaml` and execute tasks sequentially.
- Write/refactor/delete only in: `docs/`, `data/`, `plans/`, `evidence/`, `callables/`, and project root files (`.md`, `.yaml`, `.yml`).

### All Projects
- Run and fix pre-commit failures autonomously.
- Commit autonomously **only** if all pre-commit hooks pass.

## Required (MANDATORY - BLOCKING)

### TDD (Test-Driven Development) - BLOCKING (Programming Projects Only)
- **MANDATORY** (Programming Projects): Every code change MUST include corresponding test files in the same commit.
- **BLOCKING** (Programming Projects): Commits are **BLOCKED** if code files are modified without tests.
- **NOT APPLICABLE** (Documentation Projects): Documentation projects don't have code files, so TDD doesn't apply.
- **Process** (Programming Projects): Follow Red → Green → Refactor → Document cycle:
  1. **Red**: Write failing test first
  2. **Green**: Implement minimal code to pass test
  3. **Refactor**: Improve code while keeping tests green
  4. **Document**: Update documentation as needed
- **Test File Patterns** (Programming Projects): 
  - Python: `*_test.py`, `test_*.py`, files in `tests/` directories
  - TypeScript/JavaScript: `*.test.ts`, `*.test.tsx`, `*.spec.ts`, `*.spec.tsx`, files in `test/` directories
- **Reference**: See `1_global_standards/TEST_STRATEGY_TDD.md` for detailed guidance.

### SOLID Principles - BLOCKING (Programming Projects Only)
- **MANDATORY** (Programming Projects): All code MUST comply with SOLID design principles.
- **BLOCKING** (Programming Projects): Commits are **BLOCKED** on SOLID violations:
  - **SRP (Single Responsibility)**: Functions must be ≤ 50 lines
  - **ISP (Interface Segregation)**: Interfaces/types must be ≤ 10 methods/properties
  - **DIP (Dependency Inversion)**: Depend on abstractions (interfaces), not concrete implementations
- **NOT APPLICABLE** (Documentation Projects): Documentation projects don't have code architecture, so SOLID doesn't apply.
- **Enforcement**: Pre-commit `architecture-check` hook validates SOLID compliance (automatically skipped for documentation projects).
- **Reference**: See `1_global_standards/SOLID_PRINCIPLES.md` for comprehensive guide.

### Commit Frequency - INCREMENTAL COMMITS REQUIRED
- **MANDATORY**: Commit incrementally to prevent large uncommitted changesets.
- **Commit Triggers**:
  - **After completing each phase** (logical task group) OR **every 3-5 tasks**
  - **When file count threshold exceeded**: If `auto_commit: false` but code changes exceed threshold (default: 10 files), commit via checkpoint
  - **When completing logical unit of work**: Always attempt commit when completing a cohesive feature/module
- **Checkpoint Override**: If `commit_checkpoints.force_commit_on_checkpoint: true` is set, commit checkpoints override `auto_commit: false`
- **Large Changeset Warning**: If >20 files changed since last commit, pre-commit hook will warn (non-blocking)
- **Commit Message Format**: MUST include `plan:<plan_id> component:<component> task:<id>`
- **Reference**: See `docs/COMMIT_STRATEGY.md` for detailed commit frequency best practices

### Other Requirements (All Projects)
- Every commit message MUST include: `plan:<plan_id> component:<component> task:<id>` (or `task:<id>` for documentation projects).
- **Programming Projects**: Keep docs in sync; update `docs/*` and regenerate indexes when code changes.
- **Programming Projects**: Obey `5_reference_architectures/LAYER_RULES.yaml` (no cross-component violations).
- **Documentation Projects**: Maintain documentation structure, cross-references, and completeness tracking.
- **All Projects**: Stay inside current plan's scope; do not add new directories unless listed in plan.

## Forbidden
- Editing any files in: `0_phase0_bootstrap/`, `1_global_standards/`, `7_schemas/`, `.github/`, `8_ci/`, `4_docs_index/`, `5_reference_architectures/`.
- Changing governance, CI/CD, or feature flags.
- Pushing to protected branches (PRs only).

## Failure Protocol
- If a hook fails: attempt local corrective changes within current task.
- If failure persists after two attempts: append an entry to `6_ai_runtime_context/ai_feedback_log.json` and stop.

