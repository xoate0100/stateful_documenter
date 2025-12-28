# Jurisdiction Overlays

**Purpose:** Provide jurisdiction-specific legal information for Mode B template generation

**Status:** Active System Component

---

## Overview

Jurisdiction overlays contain jurisdiction-specific legal information required for generating Mode B (jurisdiction-specific) templates. They provide:

- State-specific statute citations
- Legal framework information
- Court rules
- Jurisdiction-specific terminology
- Template generation requirements

---

## Available Overlays

### Kansas

**File:** `kansas.yaml`  
**Status:** Initial Version - Requires Legal Review  
**State Code:** KS  
**Citation Format:** K.S.A. §[NUMBER]

**Key Features:**
- Right of publicity statute (K.S.A. §60-3301) - VERIFY
- Mandatory reporting (K.S.A. §38-2223) - VERIFY
- Consumer protection (K.S.A. §50-626) - VERIFY
- Common law privacy torts and defamation

**Note:** All citations require legal review and verification before use.

### Missouri

**File:** `missouri.yaml`  
**Status:** Initial Version - Requires Legal Review  
**State Code:** MO  
**Citation Format:** Mo. Rev. Stat. §[NUMBER]

**Key Features:**
- Common law right of publicity - VERIFY
- Mandatory reporting (Mo. Rev. Stat. §210.115) - VERIFY
- Consumer protection (Mo. Rev. Stat. §407.020) - VERIFY
- Common law privacy torts and defamation

**Note:** All citations require legal review and verification before use.

---

## Creating New Overlays

### Step 1: Use Template

1. Copy `OVERLAY_TEMPLATE.yaml`
2. Rename to `[jurisdiction].yaml`
3. Fill in jurisdiction-specific information

### Step 2: Research Statutes

Research and document:
- Child protection statutes
- Right of publicity (statute or common law)
- Privacy torts
- Defamation
- Consumer protection
- Biometric privacy (if applicable)

### Step 3: Document Frameworks

Document:
- Title IX applicability
- FERPA applicability
- Mandatory reporting requirements
- Biometric privacy laws
- Right of publicity rules

### Step 4: Validate

Complete validation checklist:
- Verify all citations
- Verify legal frameworks
- Verify court rules
- Verify terminology
- Complete legal review

### Step 5: Test

Test overlay with sample template generation to ensure:
- Citations are correctly formatted
- Terminology is appropriate
- Requirements are met

---

## Usage

### In Template Generation

When generating Mode B templates:

1. **Load Overlay**
   - Load appropriate jurisdiction overlay
   - Verify overlay is current and validated

2. **Use Citations**
   - Include specific statute citations from overlay
   - Follow citation format specified in overlay
   - Include statute names

3. **Use Terminology**
   - Use preferred terms from overlay
   - Avoid terms listed in avoided_terms
   - Use legal terms of art appropriately

4. **Follow Requirements**
   - Reference mandatory reporting requirements
   - Include state-specific legal frameworks
   - Follow court rules if applicable

### Validation

Before using overlay:
- [ ] Overlay has been legally reviewed
- [ ] All citations verified for accuracy
- [ ] All citations verified for currency
- [ ] Legal frameworks verified
- [ ] Court rules verified
- [ ] Terminology verified

---

## Maintenance

### Regular Updates

- Review overlays annually
- Update for legislative changes
- Update for court rule changes
- Update effective dates

### Version Control

- Track overlay versions
- Document changes
- Maintain change log
- Archive old versions

---

## Related Documents

- [Overlay Template](./OVERLAY_TEMPLATE.yaml) - Template structure
- [Overlay Creation Guide](./OVERLAY_CREATION_GUIDE.md) - Step-by-step guide
- [Citation Modes](../../docs/legal/citation_modes.md) - Mode A/B system
- [Regulatory Matrix](../../data/regulatory_matrix.yaml) - State law matrix

---

## Legal Disclaimer

**IMPORTANT:** All overlays are for template generation purposes only and do not constitute legal advice. All statute citations must be verified for accuracy and currency before use in legal documents. All legal documents should be reviewed by qualified legal counsel before use.

---

**Last Updated:** 2025-12-23  
**Version:** 1.0



