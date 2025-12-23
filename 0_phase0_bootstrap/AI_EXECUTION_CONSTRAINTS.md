# AI Execution Constraints (L2.5)
- Single agent (Cursor) may perform autonomous plan execution inside sandbox.
- Pre-commit and CI jobs are immutable enforcement gates.
- No edits to meta-framework, standards, schemas, or CI.
- **Project-Type Aware**: Constraints automatically adapt based on project type (`programming` vs `documentation`).

## Universal Constraints (All Projects)
- All commits must satisfy: format, lint, security scan, doc sync, commit schema.
- Pre-commit and CI jobs are immutable enforcement gates.

## Programming Projects Only
- All commits must satisfy: type/static checks, arch rules (SOLID), tests+coverage.
- Multi-component aware: per-component toolchains and thresholds.

## Documentation Projects Only
- Architecture rules and test coverage checks are automatically skipped (no code to validate).
- Focus on documentation quality: structure, cross-references, completeness.
