# Content Update Plan - 2026 Current Scenarios and Citations

**Date**: January 8, 2026  
**Status**: Implementation Ready  
**Priority**: P0 - Critical

---

## Executive Summary

This document outlines the plan to update all retirement content to use current, relatable scenarios (2026) instead of outdated 2008 financial crisis references, and to significantly enhance citation requirements for credibility.

---

## Problem Statement

### Current Issues

1. **Outdated References**: Content references "retired in 2008 after financial crisis" - this is 18 years old and not relatable to current readers
2. **Lack of Citations**: Statistical claims lack authoritative source citations
3. **Not Current**: Scenarios don't reflect current concerns (COVID-19, inflation, housing crisis, etc.)

### Impact

- Content feels dated and irrelevant
- Lacks credibility without citations
- Doesn't resonate with current retirees/pre-retirees
- Misses opportunity to address current psychological concerns

---

## Solution Components

### 1. Current Scenarios Library

**File**: `meta_framework/references/current_scenarios_2026.yaml`

**Scenarios to Use**:
- COVID-19 early retirement (2020-2021)
- High inflation retirement (2022-2023)
- Planning to retire in 2026-2027
- Recent retirement (2024-2025)
- Market volatility impact (2024-2025)

**Outdated (DO NOT USE)**:
- ❌ "Retired in 2008 after financial crisis"

### 2. Enhanced Citation Library

**File**: `meta_framework/references/citation_library_2026.yaml`

**Required Citations For**:
- Statistical claims (percentages, dollar amounts)
- Legislative changes (Secure Act 2.0)
- Industry leader quotes (Jamie Dimon, etc.)
- Research findings (DALBAR, Morningstar, Fidelity)
- Economic data (BLS, Federal Reserve, Census Bureau)

**Minimum Requirements**:
- 2-3 citations per chapter for statistical claims
- Cite authoritative sources for major claims
- Use multiple sources when possible

### 3. Prompt Builder Updates

**File**: `ai_prompts/prompt_builder.py`

**Changes**:
- Load current scenarios and add to prompt
- Load enhanced citation library
- Add explicit guidance: "NEVER reference 2008 financial crisis"
- Require citations for statistical claims

---

## Implementation Steps

### Phase 1: System Updates (Complete)

✅ Created `current_scenarios_2026.yaml`
✅ Created `citation_library_2026.yaml`
✅ Updated `prompt_builder.py` to load new resources
✅ Created analysis document `CURRENT_RETIREMENT_CONCERNS_2026.md`

### Phase 2: Content Updates (In Progress)

**Chapters to Update**:
1. ✅ Chapter 1: Retirement Reality Check (needs scenario updates)
2. ✅ Chapter 2: Tax Leak (needs scenario updates)
3. ⏳ Chapter 3: Social Security (pending)
4. ⏳ Chapter 4: Estate Planning (pending)
5. ⏳ Chapter 5: Healthcare (pending)
6. ⏳ Chapter 6: Real Outcomes (pending)

**Update Process**:
1. Replace 2008 references with current scenarios
2. Add citations for all statistical claims
3. Update examples to be 2026-relevant
4. Verify citations are from authoritative sources

### Phase 3: Validation

- Review all chapters for outdated references
- Verify all statistical claims have citations
- Check citation sources are authoritative
- Ensure scenarios are psychologically relevant

---

## Citation Examples

### Healthcare Costs
- ✅ "According to Fidelity's annual retirement healthcare cost studies, a 65-year-old couple retiring in 2026 can expect to spend approximately $315,000 on healthcare costs throughout retirement."
- ✅ "Based on Centers for Medicare & Medicaid Services data, Medicare Part B premiums are projected to reach $206.50 per month in 2026."

### Market Volatility
- ✅ "DALBAR's Quantitative Analysis of Investor Behavior consistently shows that investor returns lag market returns due to poor timing decisions."
- ✅ "Morningstar research indicates that sequence of returns risk can reduce retirement income by 20-30% for retirees who experience a market downturn in their first five years of retirement."

### Retirement Readiness
- ✅ "When Congress passed Secure Act 2.0, legislators expressed serious concerns about retirement readiness, noting that many Americans are not prepared for retirement."
- ✅ "According to Federal Reserve consumer research, the median retirement savings for Americans aged 55-64 is approximately $185,000—far below what's needed for a secure retirement."

### Inflation Impact
- ✅ "Bureau of Labor Statistics data shows that inflation has remained elevated following the pandemic, significantly impacting retirees on fixed incomes."
- ✅ "According to U.S. Census Bureau Consumer Expenditure Survey data, retirees spend a larger portion of their income on healthcare, housing, and food—categories that have seen significant price increases."

---

## Scenario Replacement Examples

### Replace This:
❌ "A couple came to see me a few years ago. They'd retired in 2007, right before the financial crisis. They had about $800,000 saved..."

### With This:
✅ "A couple came to see me recently. They'd retired in 2020, right when COVID-19 hit. They had about $800,000 saved, but they'd had to tap into it during the pandemic when one of them lost their job..."

OR

✅ "A couple came to see me in 2022. They'd retired in 2021, right when inflation started surging. They had about $800,000 saved, but their fixed income wasn't keeping up with rising costs..."

---

## Next Steps

1. **Update Existing Chapters 1-2**: Replace outdated references and add citations
2. **Continue Chapter Generation**: Use new system for Chapters 3-6
3. **Review and Validate**: Ensure all content meets new standards
4. **Document Process**: Update generation workflow documentation

---

**Status**: System updates complete, content updates in progress  
**Priority**: P0 - Critical for content relevance and credibility

