# Citation Mode System

**Source:** SRD_DSKB.yaml  
**Purpose:** Define jurisdiction-agnostic (Mode A) and jurisdiction-specific (Mode B) citation approaches  
**Status:** Core System Component

---

## Overview

The citation mode system enables pre-generation of templates in two modes:

- **Mode A (Jurisdiction-Agnostic):** Category-level references, no statute numbers
- **Mode B (Jurisdiction-Specific):** Statute numbers, state-specific rules (requires overlay)

All templates must be pre-generated in both modes to ensure complete coverage.

---

## Mode A: Jurisdiction-Agnostic

### Purpose

Generate templates that work across all jurisdictions without specific statute citations. This is the default mode for maximum portability.

### Characteristics

- **Category-level references only**
- **No statute numbers**
- **Generic legal framework references**
- **Works in any jurisdiction**

### Allowed Phrases

- "federal child sexual exploitation frameworks"
- "state privacy and misappropriation doctrines"
- "education harassment and Title IX obligations"
- "biometric privacy regimes where applicable"
- "consumer protection laws"
- "unfair or deceptive practices statutes"
- "right of publicity laws"
- "defamation and false light doctrines"

### Prohibited

- Specific statute numbers (e.g., "18 U.S.C. §2252")
- State-specific citations (e.g., "K.S.A. §...")
- Jurisdiction-specific terminology
- Local court rules

### Use Cases

- Initial template generation
- Multi-jurisdiction situations
- Jurisdiction not yet determined
- Generic legal notices
- Universal applicability

### Template Variants Required

All templates must have Mode A variants:
- Parent Notification Letter (Mode A)
- Platform Removal Request (Mode A)
- School Activation Notice (Mode A)
- Insurance Incident Report (Mode A)
- Civil Litigation Documents (Mode A)
- Regulatory Complaints (Mode A)
- All other templates (Mode A)

---

## Mode B: Jurisdiction-Specific

### Purpose

Generate templates with specific statute citations and jurisdiction-specific legal references. Requires jurisdiction overlay to be loaded.

### Prerequisites

- **Jurisdiction overlay loaded:** Must have overlay file for specific jurisdiction
- **Verified citations:** Statute numbers must be verified for accuracy
- **State-specific rules:** Must follow state-specific legal requirements

### Characteristics

- **Statute numbers included**
- **State-specific right of publicity rules**
- **Local mandatory reporting citations**
- **Jurisdiction-specific terminology**
- **Local court rules (if applicable)**

### Allowed

- Specific statute numbers (e.g., "18 U.S.C. §2252")
- State-specific citations (e.g., "K.S.A. §60-3301")
- Jurisdiction-specific legal frameworks
- Local court rules
- State-specific terminology

### Hard Rule

**"Do not cite numbers unless overlay loaded"**

Templates must not include statute numbers unless:
1. Jurisdiction overlay is loaded
2. Citations are verified
3. Mode B is explicitly selected

### Overlay System

Jurisdiction overlays provide:
- Statute numbers for specific jurisdiction
- State-specific legal frameworks
- Local court rules
- Jurisdiction-specific terminology
- Mandatory reporting requirements
- Right of publicity rules
- Privacy law specifics

### Use Cases

- Specific jurisdiction known
- State-specific legal requirements
- Local court filings
- Jurisdiction-specific enforcement
- Verified legal citations needed

### Template Variants Required

All templates must have Mode B variants for each jurisdiction overlay:
- Parent Notification Letter (Mode B - Kansas)
- Parent Notification Letter (Mode B - Missouri)
- Platform Removal Request (Mode B - [Jurisdiction])
- School Activation Notice (Mode B - [Jurisdiction])
- All other templates (Mode B - [Jurisdiction])

---

## Overlay System Structure

### Directory Structure

```
callables/
└── jurisdiction_overlays/
    ├── kansas.yaml
    ├── missouri.yaml
    ├── california.yaml
    └── [other_jurisdictions].yaml
```

### Overlay File Format

```yaml
jurisdiction: "Kansas"
state_code: "KS"
statutes:
  child_protection:
    - "K.S.A. §21-5506 (Sexual exploitation of a child)"
  right_of_publicity:
    - "K.S.A. §60-3301 (Right of publicity)"
  privacy:
    - "K.S.A. §50-7a01 (Consumer privacy)"
  mandatory_reporting:
    - "K.S.A. §38-2223 (Mandatory reporting)"
  
legal_frameworks:
  title_ix: "Federal Title IX applies"
  biometric_privacy: "No specific BIPA equivalent"
  
court_rules:
  filing_requirements: "Kansas state court rules"
  
terminology:
  preferred_terms: ["specific Kansas terminology"]
```

---

## Template Pre-Generation Requirements

### All Templates Must Have

1. **Mode A variant (jurisdiction-agnostic)**
   - Category-level references
   - No statute numbers
   - Universal applicability

2. **Mode B variants (jurisdiction-specific)**
   - One variant per jurisdiction overlay
   - Specific statute citations
   - Jurisdiction-specific terminology

### Pre-Generation Matrix

For each template type:
- Template Name (Mode A)
- Template Name (Mode B - Kansas)
- Template Name (Mode B - Missouri)
- Template Name (Mode B - [Other Jurisdictions])

### Example

```
Parent Notification Letter:
  - parent_notice_mode_a.md
  - parent_notice_mode_b_kansas.md
  - parent_notice_mode_b_missouri.md
  - parent_notice_mode_b_california.md
  - [etc. for each overlay]
```

---

## Human Selection Process

### Step 1: Determine Jurisdiction

- Is jurisdiction known?
- Is jurisdiction-specific template needed?
- Is overlay available?

### Step 2: Select Mode

- **Mode A:** If jurisdiction unknown or multi-jurisdiction
- **Mode B:** If jurisdiction known and overlay loaded

### Step 3: Select Variant

- **Mode A:** Select generic variant
- **Mode B:** Select jurisdiction-specific variant

### Step 4: Verify Citations (Mode B only)

- Verify statute numbers are current
- Verify citations are accurate
- Verify jurisdiction-specific rules apply

---

## Integration with Other Systems

### Logic Gates

- Logic gates determine which templates are available
- Citation mode determines which variant to use
- All combinations must be pre-generated

### Evidence Classification

- Evidence class determines language strength
- Citation mode determines legal references
- Both factors affect template selection

### Drafting Rules

- Drafting rules apply to both modes
- Mode A: Generic legal references
- Mode B: Specific statute citations
- Both must follow drafting rules

---

## Quality Assurance

### Mode A Templates

- ✅ No statute numbers
- ✅ Category-level references only
- ✅ Universal applicability
- ✅ Professional tone maintained

### Mode B Templates

- ✅ Statute numbers verified
- ✅ Jurisdiction-specific rules followed
- ✅ Overlay loaded and verified
- ✅ Citations accurate and current
- ✅ Professional tone maintained

---

## Implementation Status

- ✅ Mode A framework defined
- ✅ Mode B framework defined
- ✅ Overlay system structure designed
- ⏳ Overlay files to be created (Phase 5)
- ⏳ Template variants to be pre-generated (Phase 5)

---

## Related Documents

- [SRD_DSKB.yaml](../../plans/SRD_DSKB.yaml) - Source definition
- [Drafting Rules](drafting_rules.md) - Rules that apply to both modes
- [Logic Gates](../../data/logic_gates.yaml) - Scenario mapping
- [Evidence Classification](../../data/evidence_classification.yaml) - Evidence-based selection

