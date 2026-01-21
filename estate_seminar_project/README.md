# Estate Seminar - Documentation Project

**Project Name:** Estate Seminar  
**Full Name:** "Legacy, Locked" Educational Seminar Knowledge Base  
**Type:** Documentation Project  
**Status:** Phase 1 - Initial Setup

---

## Overview

This project contains a comprehensive knowledge base for generating financial seminar presentations. The knowledge base enables an AI LLM to generate any seminar-related asset (slides, worksheets, one-pagers, checklists, facilitator scripts, compliant CTAs, follow-up materials) without additional instructions while maintaining a strict "no sales pitch" posture.

The seminar is a 60-minute educational event focused on estate planning, designed for "suspicious, informed buyers" who value autonomy, control, and family harmony. The content is structured to build trust through education rather than sales tactics.

---

## Project Structure

```
estate_seminar_project/
├── docs/                    # Documentation files organized by type
│   ├── core_knowledge/      # Canonical constraints, brand facts, promises
│   ├── content_modules/     # Educational curriculum modules (A-F)
│   ├── worksheets/          # Worksheet templates and generation rules
│   ├── outputs/             # Generated slides, one-pagers, scripts
│   └── compliance/          # Compliance rules, guardrails, language bank
├── data/                    # Structured data files (YAML/JSON)
├── plans/                   # Project plans and task tracking
├── evidence/                # Source analysis and extraction evidence
├── callables/               # Reusable templates and documents
│   └── templates/          # Worksheet, one-pager, slide templates
└── MVP_SPECIFICATION.yaml   # Project specification
```

---

## Core Systems

### 1. Canonical Seminar Constraints

- **Format:** 60-minute seminar (5 min intro, 5-7 min closing)
- **Compliance:** Strict "no sales" rules - education only
- **Audience:** Suspicious, informed buyers who value autonomy
- **Emotional Arc:** Safety → Clarity → Competence → Relief → Agency → Peace

### 2. Brand & Entity Facts

- **SureWealth Solutions:** Retirement planning with "guaranteed strategies" and "NO sales hype"
- **Legacy Lock:** DIY estate planning toolkit and platform with worksheets and guided steps
- **Integration:** Support spectrum (self-directed → guided validation → comprehensive coordination)

### 3. Educational Curriculum (Modules A-F)

- **Module A:** Legacy Definition (5 min)
- **Module B:** Estate Planning Basics (15 min)
- **Module C:** Pitfalls (10 min)
- **Module D:** DIY System + Worksheets (15 min)
- **Module E:** Family & Values Legacy (5 min)
- **Module F:** Objections (7 min)

### 4. Worksheet System

Six canonical worksheets:
1. Legacy Snapshot
2. Decision-Maker Map
3. Asset & Beneficiary Alignment
4. Digital Legacy Inventory
5. Annual Review Triggers
6. Trust Funding Awareness

### 5. Compliance Framework

- **Allowed:** Education, frameworks, neutral explanations, permission-based support
- **Not Allowed:** Product pitches, price anchoring, scarcity, urgency, testimonials as conversion proof
- **Language Bank:** Safety lines, neutral mentions, permission-based help

---

## Current Status

**Phase:** Phase 1 - Initial Setup  
**Progress:** Project structure created, MVP specification complete

### Completed
- [x] Project directory structure created
- [x] MVP_SPECIFICATION.yaml created
- [x] README.md created
- [x] Source material archived

### In Progress
- [ ] Extract Canonical Seminar Constraints
- [ ] Extract Brand & Entity Facts
- [ ] Extract Seminar Promise & Walk-Away Wins
- [ ] Create source analysis document

### Pending
- [ ] Educational curriculum modules
- [ ] Worksheet system
- [ ] Compliance framework
- [ ] Output generation specifications
- [ ] Master index and navigation

---

## Source Material

**File:** `evidence/source_material.md` (archived from `../estate_seminar.md`)  
**Length:** 549 lines  
**Format:** Knowledge base document  
**Content:** Comprehensive seminar knowledge base covering constraints, brand facts, curriculum, worksheets, compliance, and output specifications

---

## Usage

This project follows the stateful_documenter framework for documentation projects:

1. **Plans** are tracked in `plans/` directory
2. **Active tasks** reference `6_ai_runtime_context/ACTIVE_PLAN.yaml`
3. **Documentation** is organized by type in `docs/`
4. **Structured data** is stored in `data/` as YAML/JSON
5. **Templates** are reusable assets in `callables/`

---

## Key Principles

- **Education only** - No sales pitches, urgency, or scarcity tactics
- **Autonomy-respecting** - Permission-based support, no pressure
- **Emotional engineering** - Clear before/after states for each module
- **Compliance-first** - All content must pass "no sales" validation
- **Atomic delivery** - Each module has specific emotional outcomes
- **AI-ready** - Structured for automated content generation

---

## Next Steps

1. Extract canonical seminar constraints and compliance rules
2. Extract brand facts (SureWealth Solutions, Legacy Lock)
3. Extract educational curriculum modules (A-F)
4. Create worksheet templates and generation rules
5. Establish compliance framework and language bank
6. Create output generation specifications
7. Build master index and cross-references

---

## Notes

- This is a documentation project for content generation, not a software implementation
- All generated content must maintain strict "no sales" compliance
- Content serves seminar delivery: slides, worksheets, one-pagers, scripts, follow-up materials
- All content should be traceable to source material
- Cross-references should be maintained throughout documentation
