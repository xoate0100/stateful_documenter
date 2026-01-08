# Storytelling Components Audit & Validation
**Date**: January 8, 2026  
**Purpose**: Verify and validate all storytelling components for consistency with expanded persona framework

---

## Executive Summary

**Status**: ⚠️ **Gaps Identified** - Components need updates for new persona framework

**Key Findings**:
- ✅ Allegories/Metaphors: Persona-agnostic, work with all personas
- ⚠️ Case Studies: Only 1 (engineer-focused), need 6+ for new personas
- ❌ Characters: Empty index, need characters for each persona tier
- ⚠️ CTAs: Generic, need persona-specific CTAs aligned with voice adaptations
- ⚠️ Retiree Archetypes: Need mapping to new personas

---

## Component Analysis

### 1. Case Studies

#### Current State
- **Total**: 1 case study
- **Focus**: Engineer (technical/analytical)
- **File**: `CASE_STUDY_MARK_ENGINEER.yaml`
- **Persona**: `analytical_engineer`, `data_driven_professional`

#### Gaps Identified
- ❌ No case studies for Tier 1 personas (Early Retiree, Late-Career Executive)
- ❌ No case studies for Tier 2 personas (Business Owner, Dual-Income Professional, Squeeze Parent)
- ❌ No case studies for Tier 3 personas (Public Servant)
- ❌ No multi-layered persona case studies

#### Required Additions
1. **Early Retiree Case Study**: Just retired, immediate income need, sequence risk
2. **Late-Career Executive Case Study**: Corporate executive, stock options, deferred comp
3. **Business Owner Case Study**: Exit strategy, equity conversion, legacy protection
4. **Dual-Income Professional Case Study**: No pension, creating guaranteed income
5. **Squeeze Parent Case Study**: Education + retirement balance
6. **Public Servant Case Study**: Pension gap, healthcare concerns
7. **Veteran Business Owner Case Study**: Multi-layered (exit + tuition)

---

### 2. Characters

#### Current State
- **Total**: 0 characters
- **Index**: Empty (`characters_index.yaml`)

#### Gaps Identified
- ❌ No characters defined for any persona
- ❌ No character state tracking
- ❌ No character consistency across chapters

#### Required Additions
Characters should be created for:
1. **Early Retiree**: 65-year-old who just retired, needs income strategy
2. **Late-Career Executive**: 60-year-old VP with stock options
3. **Business Owner**: 61-year-old construction owner with exit timeline
4. **Dual-Income Professional**: 58-year-old couple, no pension
5. **Squeeze Parent**: 55-year-old with college kids
6. **Public Servant**: 58-year-old teacher with pension gap
7. **Veteran Business Owner**: Multi-layered persona

**Note**: Characters can be reused across case studies and chapters for consistency.

---

### 3. CTAs (Call to Actions)

#### Current State
- **Total**: Generic CTAs, not persona-specific
- **File**: `cta_library.yaml`
- **Structure**: Question-based, soft, primary, urgency, curiosity

#### Gaps Identified
- ⚠️ CTAs are generic, not aligned with persona voice adaptations
- ⚠️ Missing persona-specific CTA angles from `persona_voice_adaptation.yaml`
- ⚠️ No mapping between personas and CTA preferences

#### Required Updates
Map persona-specific CTAs from voice adaptations:
- **Early Retiree**: "Protect your retirement now—the sequence risk is real"
- **Late-Career Executive**: "Optimize your retirement strategy before the window closes"
- **Business Owner**: "Create your exit strategy and protect what you've built"
- **Dual-Income Professional**: "Create your guaranteed income strategy—you don't have a pension, but you can build one"
- **Squeeze Parent**: "Fund their education and secure your retirement"
- **Public Servant**: "Bridge the gap safely, especially for healthcare"

---

### 4. Allegories & Metaphors

#### Current State
- **Allegories**: 4 (Leaky Bucket, House of Cards, Pressure Relief Valve, Two Sides of Coin)
- **Metaphors**: 7 (Savings Account, Waterfall, Sailboat, Warehouse, Left Pocket/Right Pocket, Hiccup/Speed Bump, Pressure Relief Valve)
- **Status**: ✅ Persona-agnostic, work with all personas

#### Analysis
- ✅ **Leaky Bucket**: Works for all personas (tax drag universal)
- ✅ **House of Cards**: Works for all personas (market dependency universal)
- ✅ **Pressure Relief Valve**: Works for all personas (emergency access universal)
- ✅ **Metaphors**: All are concept-based, not persona-specific

#### Recommendation
- ✅ **Keep as-is**: Allegories and metaphors are persona-agnostic
- ✅ **Verify usage**: Ensure they're used appropriately across all personas
- ✅ **Add persona context**: When using, add persona-specific framing

---

### 5. Retiree Archetypes

#### Current State
- **Total**: 4 archetypes (Saver, Risk-Taker, DIY Investor, Overwhelmed)
- **File**: `retiree_archetypes.yaml`
- **Status**: ✅ Still useful, but need mapping to new personas

#### Gaps Identified
- ⚠️ Archetypes are behavior-based, not persona-based
- ⚠️ Need mapping: Which archetypes fit which personas?
- ⚠️ Need persona-specific archetype variations

#### Mapping Recommendations
- **Early Retiree**: Often "Saver" or "Overwhelmed" (immediate need)
- **Late-Career Executive**: Often "DIY Investor" or "Risk-Taker" (strategic)
- **Business Owner**: Often "DIY Investor" or "Risk-Taker" (independent)
- **Dual-Income Professional**: Often "Saver" or "DIY Investor" (security-focused)
- **Squeeze Parent**: Often "Saver" or "Overwhelmed" (family-focused)
- **Public Servant**: Often "Saver" (security-focused)

---

## Consistency Validation

### Persona → Component Mapping

| Persona | Case Study | Character | CTA | Archetype | Status |
|---------|-----------|-----------|-----|-----------|--------|
| Early Retiree | ❌ Missing | ❌ Missing | ⚠️ Needs update | ✅ Saver/Overwhelmed | ❌ Incomplete |
| Late-Career Executive | ❌ Missing | ❌ Missing | ⚠️ Needs update | ✅ DIY/Risk-Taker | ❌ Incomplete |
| Business Owner | ❌ Missing | ❌ Missing | ⚠️ Needs update | ✅ DIY/Risk-Taker | ❌ Incomplete |
| Dual-Income Professional | ❌ Missing | ❌ Missing | ⚠️ Needs update | ✅ Saver/DIY | ❌ Incomplete |
| Squeeze Parent | ❌ Missing | ❌ Missing | ⚠️ Needs update | ✅ Saver/Overwhelmed | ❌ Incomplete |
| Public Servant | ❌ Missing | ❌ Missing | ⚠️ Needs update | ✅ Saver | ❌ Incomplete |
| Engineer (Legacy) | ✅ Exists | ❌ Missing | ⚠️ Generic | ✅ DIY | ⚠️ Partial |

---

## Implementation Plan

### Phase 1: Create Case Studies (Priority: High)
1. Create case study for each Tier 1 persona
2. Create case study for each Tier 2 persona
3. Create case study for Tier 3 persona
4. Create multi-layered persona case study

### Phase 2: Create Characters (Priority: High)
1. Create character for each persona tier
2. Define character attributes (age, occupation, financial situation)
3. Create character state tracking
4. Map characters to case studies

### Phase 3: Update CTAs (Priority: Medium)
1. Add persona-specific CTA section to `cta_library.yaml`
2. Map CTAs from `persona_voice_adaptation.yaml`
3. Create persona → CTA mapping guide
4. Update prompt builder to use persona-specific CTAs

### Phase 4: Map Archetypes (Priority: Low)
1. Create persona → archetype mapping
2. Add persona-specific archetype variations
3. Update prompt builder to use archetype mapping

### Phase 5: Validation (Priority: High)
1. Verify all components work together
2. Test persona selection → component selection
3. Create validation document
4. Update prompt builder integration

---

## Next Steps

1. ✅ **Audit Complete** - This document
2. ⏳ **Create Case Studies** - 7 new case studies
3. ⏳ **Create Characters** - 7 new characters
4. ⏳ **Update CTAs** - Persona-specific CTAs
5. ⏳ **Map Archetypes** - Persona → archetype mapping
6. ⏳ **Integration** - Update prompt builder
7. ⏳ **Validation** - Test end-to-end

---

**Status**: Audit Complete - Ready for Implementation

