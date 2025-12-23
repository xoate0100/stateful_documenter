# SRD_DSKB Integration Plan

**⚠️ SUPERSEDED:** This document has been superseded by [`UNIFIED_PROTOCOL.md`](../UNIFIED_PROTOCOL.md)

**Date:** 2025-12-22  
**Purpose:** Resolve inconsistencies and integrate SRD_DSKB for template generation  
**Status:** COMPLETE - All inconsistencies resolved

---

## Overview

This plan addressed the inconsistencies identified between SRD_DSKB.yaml and the current MUDP system, and outlined the integration steps needed to enable precise, conditional template generation.

**Note:** All inconsistencies have been resolved. This document is preserved for historical reference. All current work should reference [`UNIFIED_PROTOCOL.md`](../UNIFIED_PROTOCOL.md).

---

## Critical Inconsistencies to Resolve

### 1. Escalation Tier Mismatch (CRITICAL)

**Issue:** Current system has 6 tiers, SRD_DSKB has 7 tiers

**Current:**
- Tier 6 = Criminal Pathways

**SRD_DSKB:**
- T6 = Regulatory Complaints
- T7 = Appellate and Constitutional

**Action Required:**
1. Update `data/enforcement_tiers.yaml` to add Tier 7
2. Update `docs/operational/crisis_playbook.md` to include Level 6 (Appellate/Constitutional)
3. Separate regulatory complaints from criminal pathways
4. Update cross-references

**Files to Update:**
- `data/enforcement_tiers.yaml`
- `docs/operational/crisis_playbook.md`
- `plans/binder_structure.yaml` (if needed)
- `data/cross_references.yaml`

---

### 2. Logic Gates System Missing (CRITICAL)

**Issue:** SRD_DSKB has formal logic gates, current system doesn't

**Action Required:**
1. Create `data/logic_gates.yaml` with all 6 logic gates
2. Document decision tree
3. Integrate into template generation system
4. Update Crisis Playbook to reference logic gates

**New File:**
- `data/logic_gates.yaml`

**Files to Update:**
- `docs/operational/crisis_playbook.md`
- `callables/templates/TEMPLATE_INDEX.md`
- `data/cross_references.yaml`

---

### 3. Evidence Classification Missing (CRITICAL)

**Issue:** SRD_DSKB has E1-E5 classification with usage rules, current system doesn't

**Action Required:**
1. Add evidence classification to `docs/technical/provenance_system.md`
2. Create `data/evidence_classification.yaml`
3. Document usage rules
4. Integrate into template generation

**New File:**
- `data/evidence_classification.yaml`

**Files to Update:**
- `docs/technical/provenance_system.md`
- `callables/templates/TEMPLATE_INDEX.md`

---

### 4. Citation Mode System Missing (HIGH)

**Issue:** SRD_DSKB has Mode A/B, current system doesn't

**Action Required:**
1. Create citation mode documentation
2. Design jurisdiction overlay system
3. Update templates to support both modes
4. Create overlay template structure

**New Files:**
- `docs/legal/citation_modes.md`
- `data/jurisdiction_overlays/` (directory)

**Files to Update:**
- All template files
- `callables/templates/TEMPLATE_INDEX.md`

---

### 5. Drafting Rules Not Formalized (HIGH)

**Issue:** SRD_DSKB has formal rules, current system has guidance only

**Action Required:**
1. Create `docs/legal/drafting_rules.md`
2. Create `callables/templates/boilerplate/` directory
3. Extract mandatory boilerplate blocks
4. Document prohibited/preferred language

**New Files:**
- `docs/legal/drafting_rules.md`
- `callables/templates/boilerplate/` (directory with boilerplate blocks)

**Files to Update:**
- All template files
- `callables/templates/TEMPLATE_INDEX.md`

---

### 6. Sexualization Level Definitions Missing (MEDIUM)

**Issue:** SRD_DSKB has 3 levels with drafting postures, current system doesn't

**Action Required:**
1. Add definitions to `data/definitions.yaml`
2. Integrate into logic gates
3. Create conditional response framework
4. Update templates to use levels

**New File:**
- `data/definitions.yaml` (or add to existing)

**Files to Update:**
- `data/logic_gates.yaml`
- `callables/templates/TEMPLATE_INDEX.md`

---

### 7. Terminology Alignment (MEDIUM)

**Issue:** Terminology differences between systems

**Action Required:**
1. Create terminology glossary
2. Align terms across all documents
3. Update cross-references

**New File:**
- `docs/TERMINOLOGY.md`

**Files to Update:**
- All documentation files
- `data/cross_references.yaml`

---

### 8. Stakeholder Objectives Not Formalized (MEDIUM)

**Issue:** SRD_DSKB has formal objectives, current system has descriptions

**Action Required:**
1. Create `data/stakeholders.yaml`
2. Map objectives to templates
3. Enable stakeholder-specific generation

**New File:**
- `data/stakeholders.yaml`

**Files to Update:**
- `callables/templates/TEMPLATE_INDEX.md`
- `docs/operational/crisis_playbook.md`

---

## Integration Steps

### Phase 1: Critical Fixes (Before Template Generation)

1. **Add Tier 7**
   - Update enforcement_tiers.yaml
   - Update crisis_playbook.md
   - Update cross-references

2. **Create Logic Gates System**
   - Create logic_gates.yaml
   - Document decision tree
   - Integrate into playbook

3. **Add Evidence Classification**
   - Create evidence_classification.yaml
   - Update provenance_system.md
   - Document usage rules

### Phase 2: Template Generation Infrastructure

4. **Implement Citation Modes**
   - Create citation_modes.md
   - Design overlay system
   - Update template structure

5. **Formalize Drafting Rules**
   - Create drafting_rules.md
   - Build boilerplate library
   - Document prohibited/preferred language

6. **Add Sexualization Levels**
   - Create definitions.yaml
   - Integrate into logic gates
   - Create conditional framework

### Phase 3: Enhancement

7. **Align Terminology**
   - Create TERMINOLOGY.md
   - Update all documents
   - Align cross-references

8. **Formalize Stakeholders**
   - Create stakeholders.yaml
   - Map to templates
   - Enable customization

---

## Template Generation Architecture

### With SRD_DSKB Integration

```
Template Generation Flow:

1. Incident Assessment
   ├─ Evaluate Logic Gates (LG_01A-C, LG_02-06)
   ├─ Classify Evidence (E1-E5)
   ├─ Determine Sexualization Level
   └─ Identify Stakeholders

2. Template Selection
   ├─ Activate based on Logic Gates
   ├─ Select Citation Mode (A or B)
   ├─ Choose Stakeholder-Specific Version
   └─ Apply Sexualization Level Language

3. Template Generation
   ├─ Apply Drafting Rules
   ├─ Insert Mandatory Boilerplate
   ├─ Use Preferred Language
   ├─ Avoid Prohibited Language
   ├─ Match Evidence Strength to Claims
   └─ Apply Citation Mode

4. Output
   ├─ Jurisdiction-Agnostic (Mode A) or Specific (Mode B)
   ├─ Stakeholder-Customized
   ├─ Evidence-Appropriate
   └─ Counsel-Ready
```

---

## Benefits of Integration

### Template Generation
- ✅ Conditional generation based on situation
- ✅ Evidence-appropriate language
- ✅ Jurisdiction-agnostic or specific
- ✅ Stakeholder-customized
- ✅ Professional, legally sound
- ✅ Avoids prohibited language
- ✅ Includes mandatory boilerplate

### System Consistency
- ✅ Aligned terminology
- ✅ Complete escalation paths
- ✅ Formal decision logic
- ✅ Evidence classification
- ✅ Citation modes
- ✅ Drafting standards

### Legal Safety
- ✅ Prevents over-claiming
- ✅ Evidence-appropriate language
- ✅ Jurisdiction-appropriate citations
- ✅ Professional tone
- ✅ Required disclaimers

---

## Risk Assessment

### Without Integration
- ❌ Templates may be inappropriate for situation
- ❌ Language may not match evidence strength
- ❌ Citations may be wrong for jurisdiction
- ❌ Missing required boilerplate
- ❌ May use prohibited language
- ❌ Incomplete escalation paths

### With Integration
- ✅ Templates conditionally appropriate
- ✅ Language matches evidence
- ✅ Citations jurisdiction-appropriate
- ✅ All boilerplate included
- ✅ Prohibited language avoided
- ✅ Complete escalation paths

---

## Recommendation

**DO NOT proceed to Phase 5 template generation without resolving critical inconsistencies.**

**Priority Order:**
1. Fix Tier 7 mismatch (30 min)
2. Create Logic Gates system (1-2 hours)
3. Add Evidence Classification (1 hour)
4. Then proceed to template generation with SRD_DSKB as engine

**Estimated Time:** 3-4 hours to resolve critical issues before template generation.

---

## Next Steps

1. **Review this analysis** with stakeholders
2. **Prioritize fixes** based on template generation needs
3. **Execute Phase 1 fixes** (Critical)
4. **Execute Phase 2 infrastructure** (High)
5. **Then proceed to Phase 5** with SRD_DSKB integration

---

## Related Documents

- [SRD_DSKB Analysis](../evidence/SRD_DSKB_ANALYSIS.md)
- [SRD_DSKB File](../plans/SRD_DSKB.yaml)
- [Enforcement Tiers](../data/enforcement_tiers.yaml)
- [Crisis Playbook](../docs/operational/crisis_playbook.md)

