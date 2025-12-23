# Documentation Sync System - Enhanced Implementation

**Date:** January 2025  
**Status:** Enhanced to support multiple projects and master reference

---

## Overview

The `docs_sync.py` script maintains a **master documentation index** (`4_docs_index/DOCUMENTATION_INDEX.md`) that serves as the central reference for:

1. **Meta-Framework Documentation** - Rules, standards, guidelines, schemas
2. **All Programming Projects** - Projects with code (frontend/backend/shared)
3. **All Documentation Projects** - Projects with documentation (docs/data/plans)
4. **Project-Specific Indexes** - Links to each project's own master index

---

## How It Works

### 1. Project Detection

The script automatically scans the repository root for project folders by looking for:
- Folders containing `MVP_SPECIFICATION.yaml`
- Excludes meta-framework directories (0_phase0_bootstrap/, 1_global_standards/, etc.)
- Excludes component directories (frontend/, backend/, shared/)

### 2. Project Type Detection

For each project found:
- Reads `MVP_SPECIFICATION.yaml`
- Detects `Project_Type` field (`programming` or `documentation`)
- Extracts project metadata (description, README, master index)

### 3. Master Index Generation

The script generates a comprehensive index with:

#### Meta-Framework Documentation Section
- Core framework files (AI_SANDBOX_RULES.md, feature_flags.yml, etc.)
- Standards & guidelines (SOLID, TDD, Security, Git, CI/CD)
- Architecture & schemas
- Scripts & tools
- Active context (ACTIVE_PLAN.yaml, etc.)

#### Programming Projects Section
- Lists all programming projects
- Links to project READMEs
- Project descriptions

#### Documentation Projects Section
- Lists all documentation projects
- Links to project READMEs
- **Links to project-specific MASTER_INDEX.md** (comprehensive project documentation)
- Project descriptions

---

## Repository Structure

```
repository/
├── 0_phase0_bootstrap/          # Meta-framework configuration
├── 1_global_standards/           # Standards and guidelines
├── 2_framework_templates/        # Project templates
├── 3_bootstrap_scripts/          # Initialization scripts
│   └── docs_sync.py              # This script
├── 4_docs_index/                 # Master documentation index
│   └── DOCUMENTATION_INDEX.md    # Master reference (auto-generated)
├── 5_reference_architectures/     # Architecture rules
├── 6_ai_runtime_context/         # Active plans and state
├── 7_schemas/                    # Validation schemas
├── 8_ci/                         # CI/CD configuration
├── frontend/                      # Frontend code (if root is programming project)
├── backend/                       # Backend code (if root is programming project)
├── shared/                        # Shared code (if root is programming project)
├── mudp_project/                 # Documentation project example
│   ├── MVP_SPECIFICATION.yaml
│   ├── README.md
│   ├── docs/
│   │   └── MASTER_INDEX.md        # Project-specific master index
│   ├── data/
│   ├── plans/
│   └── ...
└── <other_projects>/              # Additional projects
```

---

## Master Reference Structure

The master `DOCUMENTATION_INDEX.md` contains:

1. **Meta-Framework Documentation**
   - All rules, standards, and guidelines
   - Architecture and schemas
   - Scripts and tools
   - Active context

2. **Programming Projects**
   - Each project with README link
   - Project descriptions

3. **Documentation Projects**
   - Each project with README link
   - **Link to project's MASTER_INDEX.md** (comprehensive project docs)
   - Project descriptions

4. **Repository Structure**
   - Visual representation of directory structure

5. **Usage Guide**
   - How to navigate the index
   - Where to find different types of documentation

---

## Project-Specific Master Indexes

Documentation projects can have their own `docs/MASTER_INDEX.md` that provides:
- Comprehensive navigation within the project
- Project-specific organization (e.g., MUDP's strategic/legal/technical structure)
- Cross-references within the project
- Project status and completion tracking

The master `DOCUMENTATION_INDEX.md` links to these project-specific indexes.

---

## Usage

### Automatic (Pre-commit Hook)
The script runs automatically via pre-commit hook when documentation changes.

### Manual Execution
```bash
python3 3_bootstrap_scripts/docs_sync.py
```

### Output
- Updates `4_docs_index/DOCUMENTATION_INDEX.md`
- Prints summary of projects found
- Exits with status 0 on success

---

## Features

✅ **Automatic Project Detection** - Scans for projects with MVP_SPECIFICATION.yaml  
✅ **Project Type Awareness** - Distinguishes programming vs documentation projects  
✅ **Meta-Framework Reference** - Complete index of framework rules and standards  
✅ **Project Linking** - Links to project READMEs and master indexes  
✅ **Multi-Project Support** - Handles any number of projects  
✅ **Relative Paths** - Uses relative paths for portability  
✅ **Auto-Generated** - Always up-to-date with current repository state  

---

## Example Output

```markdown
# Master Documentation Index

**Last Updated:** 2025-01-22 10:30:00

## Meta-Framework Documentation
- [AI Sandbox Rules](0_phase0_bootstrap/AI_SANDBOX_RULES.md)
- [SOLID Principles](1_global_standards/SOLID_PRINCIPLES.md)
- ...

## Programming Projects
*No programming projects found*

## Documentation Projects

### [mudp_project](mudp_project/)
- **Description:** Extract and structure MUDP system...
- **README:** [README.md](mudp_project/README.md)
- **Master Index:** [MASTER_INDEX.md](mudp_project/docs/MASTER_INDEX.md)
```

---

## Integration with Meta-Framework

The `docs_sync` guardrail (`require_doc_sync`) encourages documentation updates but doesn't block commits. The master index is maintained automatically to ensure:

1. **Discoverability** - Easy to find all documentation
2. **Organization** - Clear separation of meta-framework vs projects
3. **Navigation** - Quick links to project-specific documentation
4. **Completeness** - Master reference for entire repository

---

## Future Enhancements

Potential improvements:
- [ ] Scan for project-specific documentation changes
- [ ] Generate cross-project references
- [ ] Track documentation completeness metrics
- [ ] Support for nested project structures
- [ ] Integration with Second Brain system

---

**End of Documentation**

