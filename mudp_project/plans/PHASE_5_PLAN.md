# Phase 5: Template Pre-Generation Plan

**Date:** 2025-12-23  
**Status:** In Progress  
**Purpose:** Pre-generate complete library of decision-ready template artifacts

---

## Overview

Phase 5 uses the SRD_DSKB framework to pre-generate all template variants for complete scenario coverage. This creates a comprehensive artifact library that enables human selection of appropriate templates during incidents.

**Key Principle:** Pre-generate ALL combinations, humans select and execute.

---

## Pre-Generation Framework

### Scenario Dimensions

Templates must be pre-generated for all combinations of:

1. **Logic Gates** (LG_01A, LG_01B, LG_01C, LG_02, LG_03, LG_04, LG_05, LG_06)
2. **Sexualization Levels** (Explicit, Non-Explicit, Age-Ambiguous)
3. **Evidence Classes** (E1, E2, E3, E4, E5)
4. **Stakeholders** (Parents, School, Platform, Insurance, Counsel, Regulators)
5. **Citation Modes** (Mode A - Agnostic, Mode B - Specific [per jurisdiction])
6. **Escalation Tiers** (T1, T2, T3, T4, T5, T6, T7)

### Template Types Required

Based on SRD_DSKB escalation_readiness_map:

**T1 (Parent-Parent Resolution):**
- Parent notice templates
- Deletion confirmation script
- Device sweep request

**T2 (School Activation):**
- Title IX notice
- Safety plan request
- District legal notice
- Documentation request

**T3 (Platform/App Action):**
- Urgent removal request
- Preservation notice
- Repeat upload suppression request

**T4 (Insurance Activation):**
- Carrier incident notice
- Coverage trigger memo
- Risk mitigation demands

**T5 (Civil Litigation):**
- Complaint outline
- Injunction motion outline
- Discovery plan
- Spoliation letter

**T6 (Regulatory Complaints):**
- Attorney General complaint outline
- FTC complaint outline
- Privacy authority notice

**T7 (Appellate/Constitutional):**
- Constitutional issue preservation memo
- Appeal theory outline
- Record build plan

---

## Pre-Generation Strategy

### Priority Order

1. **Tier 1 Templates** (Most commonly used)
   - Parent notification letters (all variants)
   - Deletion confirmation scripts
   - Device sweep requests

2. **Tier 2 Templates** (School context)
   - Title IX notices
   - Safety plan requests
   - District legal notices

3. **Tier 3 Templates** (Platform removal)
   - Urgent removal requests
   - Preservation notices
   - Repeat upload suppression

4. **Tier 4 Templates** (Insurance)
   - Carrier incident notices
   - Coverage trigger memos

5. **Tier 5 Templates** (Civil litigation)
   - Complaint outlines
   - Injunction motions
   - Discovery plans

6. **Tier 6 Templates** (Regulatory)
   - AG complaints
   - FTC complaints
   - Privacy authority notices

7. **Tier 7 Templates** (Appellate)
   - Constitutional preservation memos
   - Appeal theory outlines
   - Record build plans

### Variant Generation Approach

For each template type, generate:

1. **Mode A variants** (jurisdiction-agnostic)
   - All logic gate combinations
   - All evidence classes
   - All stakeholders
   - All escalation tiers

2. **Mode B variants** (jurisdiction-specific)
   - Start with Kansas and Missouri (mentioned in source)
   - Expand to other jurisdictions as needed
   - All logic gate combinations
   - All evidence classes
   - All stakeholders
   - All escalation tiers

---

## Template Structure

### Standard Template Sections

1. **Header**
   - Template identifier
   - Logic gate(s) active
   - Evidence class
   - Citation mode
   - Escalation tier
   - Stakeholder

2. **Facts Section**
   - Incident description (placeholder)
   - Evidence summary (evidence-class appropriate)
   - Timeline (placeholder)

3. **Legal Framework**
   - Applicable laws (Mode A: category, Mode B: specific)
   - Legal obligations
   - Rights and remedies

4. **Demands/Actions**
   - Immediate actions required
   - Preservation requirements
   - Response timeline

5. **Mandatory Boilerplate**
   - Jurisdiction disclaimer
   - Non-waiver of rights
   - Preservation of evidence notice
   - Good faith resolution statement
   - Reservation of escalation rights

6. **Footer**
   - Contact information (placeholder)
   - Date (placeholder)
   - Signature (placeholder)

---

## Quality Assurance

### Each Template Must:

- ✅ Follow drafting rules (tone, structure, language)
- ✅ Include all mandatory boilerplate blocks
- ✅ Avoid prohibited language
- ✅ Use preferred language appropriately
- ✅ Match language strength to evidence class
- ✅ Match language to sexualization level
- ✅ Follow citation mode requirements
- ✅ Be counsel-ready
- ✅ Be jurisdiction-appropriate

### Validation Checklist

- [ ] Drafting rules applied
- [ ] Boilerplate included
- [ ] Prohibited language avoided
- [ ] Preferred language used
- [ ] Evidence-appropriate language
- [ ] Sexualization-level-appropriate language
- [ ] Citation mode correct
- [ ] Logic gates reflected
- [ ] Stakeholder-appropriate
- [ ] Escalation tier appropriate

---

## File Organization

### Directory Structure

```
callables/templates/
├── tier_1_parent_resolution/
│   ├── parent_notice/
│   │   ├── mode_a/
│   │   │   ├── lg01a_e1.md
│   │   │   ├── lg01a_e2.md
│   │   │   ├── lg01a_e3.md
│   │   │   └── [all combinations]
│   │   └── mode_b/
│   │       ├── kansas/
│   │       │   └── [all combinations]
│   │       └── missouri/
│   │           └── [all combinations]
│   ├── deletion_confirmation/
│   └── device_sweep/
├── tier_2_school_activation/
├── tier_3_platform_action/
├── tier_4_insurance/
├── tier_5_civil_litigation/
├── tier_6_regulatory/
└── tier_7_appellate/
```

### Naming Convention

`{template_type}_{logic_gates}_{evidence_class}_{citation_mode}_{tier}_{stakeholder}.md`

Example:
- `parent_notice_lg01a_e1_modea_t1_custodial_parent.md`
- `title_ix_notice_lg01a_lg04_e1_modeb_kansas_t2_school.md`

---

## Implementation Steps

### Step 1: Create Template Skeleton

Create base template structure with:
- Standard sections
- Placeholders for customization
- Boilerplate blocks
- Citation mode placeholders

### Step 2: Generate Tier 1 Templates

Start with most commonly used templates:
- Parent notification letters
- All logic gate combinations
- All evidence classes
- Both citation modes

### Step 3: Generate Remaining Tiers

Proceed through T2-T7:
- Generate all template types per tier
- All combinations per template type
- Both citation modes

### Step 4: Create Selection Guide

Document decision tree for human selection:
- Logic gate assessment
- Evidence classification
- Stakeholder identification
- Citation mode selection
- Escalation tier determination

### Step 5: Validate and Organize

- Validate all templates against QA checklist
- Organize into directory structure
- Create index/navigation
- Update TEMPLATE_INDEX.md

---

## Progress Tracking

### Metrics

- Total templates to generate: [Calculate based on combinations]
- Templates generated: [Track progress]
- Templates validated: [Track validation]
- Coverage percentage: [Calculate]

### Status Tracking

Use `plans/phase_5_progress.yaml` to track:
- Templates by tier
- Templates by logic gate
- Templates by evidence class
- Templates by citation mode
- Validation status
- Completion percentage

---

## Next Actions

1. **Create template skeleton** - Base structure for all templates
2. **Generate Tier 1 templates** - Start with parent notices
3. **Validate approach** - Review sample templates
4. **Scale generation** - Generate remaining tiers
5. **Create selection guide** - Decision tree for humans
6. **Final validation** - Complete QA pass

---

## Related Documents

- [SRD_DSKB.yaml](SRD_DSKB.yaml) - Source framework
- [Logic Gates](../data/logic_gates.yaml) - Scenario mapping
- [Evidence Classification](../data/evidence_classification.yaml) - Evidence classes
- [Citation Modes](../docs/legal/citation_modes.md) - Citation system
- [Drafting Rules](../docs/legal/drafting_rules.md) - Drafting standards
- [Enforcement Tiers](../data/enforcement_tiers.yaml) - All 7 tiers
- [Boilerplate Library](../callables/templates/boilerplate/) - Mandatory blocks

