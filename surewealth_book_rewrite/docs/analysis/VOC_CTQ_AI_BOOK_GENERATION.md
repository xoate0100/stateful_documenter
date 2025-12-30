# Voice of the Customer (VOC) - Critical to Quality (CTQ) Analysis
## AI Book Generation System

**Date**: 2025-12-27  
**Purpose**: Identify Critical to Quality factors for AI generating an entire book and forecast consistency of expected output

---

## Executive Summary

This document identifies the Critical to Quality (CTQ) factors that determine whether our AI content generation system can consistently produce a complete book that meets brand standards, maintains consistency, and drives conversions. Based on analysis of the current system, feedback logs, and edge cases, we've identified **12 critical CTQ factors** and **8 high-risk edge cases** that could impact book generation quality.

---

## Customer Voice: What We Need

### Primary Customer Requirements

1. **Consistency Across 200+ Pages**
   - "Every chapter should sound like it was written by the same expert advisor"
   - "The book should feel cohesive, not like a collection of blog posts"

2. **Brand Voice Preservation**
   - "It should sound like SureWealth, not ChatGPT"
   - "No AI-sounding phrases that break trust"

3. **Conversion Optimization**
   - "Every chapter should move readers toward action"
   - "CTAs should be appropriate for the funnel stage"

4. **Compliance & Accuracy**
   - "Zero compliance violations across entire book"
   - "All financial concepts must be accurate"

5. **Emotional Journey Continuity**
   - "The book should take readers on a complete emotional journey"
   - "Each chapter should build on the previous one"

6. **Narrative Consistency**
   - "Characters and stories should be referenced consistently"
   - "Metaphors should reinforce, not contradict each other"

---

## Critical to Quality (CTQ) Factors

### CTQ 1: Narrative Element Constraint Clarity ⚠️ **HIGH RISK**

**Customer Need**: "We need to know if AI can create new narratives or must only use listed ones"

**Current State**:
- System prompt says: "Reference framework elements when relevant"
- Prompt builder says: "Use narratives: [NARRATIVE_IDS]"
- **AMBIGUITY**: Does not explicitly state "ONLY use these narratives" or "You may create new ones if needed"

**CTQ Specification**:
- **Must**: AI should ONLY use narratives/metaphors/allegories from the framework
- **Must**: If a new narrative is needed, AI should flag it for human review
- **Must**: All narrative references must be validated against framework

**Risk Level**: 🔴 **CRITICAL**
- **Impact**: Inconsistent metaphors could confuse readers
- **Impact**: New narratives might not align with brand voice
- **Impact**: Could create contradictions across chapters

**Forecast**: 
- **Without Fix**: 40% chance AI creates unauthorized narratives
- **With Fix**: 5% chance (only if framework is incomplete)

---

### CTQ 2: Character Consistency Across Chapters ⚠️ **HIGH RISK**

**Customer Need**: "Characters like John Smith should have the same financial situation in Chapter 2 as Chapter 8"

**Current State**:
- Characters are defined in framework
- No cross-chapter validation system
- No character state tracking

**CTQ Specification**:
- **Must**: Character financial profiles must remain consistent
- **Must**: Character references must match framework data
- **Must**: Character evolution (if any) must be tracked

**Risk Level**: 🔴 **CRITICAL**
- **Impact**: John Smith's $100k income in Chapter 2 becomes $150k in Chapter 8
- **Impact**: Breaks suspension of disbelief
- **Impact**: Damages credibility

**Forecast**:
- **Without Fix**: 60% chance of character inconsistency
- **With Fix**: 10% chance (requires state tracking system)

---

### CTQ 3: Signature Phrase Rotation & Repetition ⚠️ **MEDIUM RISK**

**Customer Need**: "We don't want 'Hope is not a strategy' in every chapter"

**Current State**:
- Lessons learned identify this as an issue
- Content index tracks signature phrases
- No automatic rotation enforcement

**CTQ Specification**:
- **Must**: No signature phrase repeated within 5 chapters
- **Must**: Signature phrases must be contextually appropriate
- **Must**: Track usage across entire book

**Risk Level**: 🟡 **MEDIUM**
- **Impact**: Repetition breaks brand voice
- **Impact**: Feels templated, not authentic

**Forecast**:
- **Without Fix**: 70% chance of over-repetition
- **With Fix**: 15% chance (requires rotation system)

---

### CTQ 4: Permission Frame Usage Limits ⚠️ **MEDIUM RISK**

**Customer Need**: "Permission frames should be strategic, not every paragraph"

**Current State**:
- Lessons learned: Max 2 per 2000-word piece
- No automatic enforcement
- AI might overuse if not explicitly constrained

**CTQ Specification**:
- **Must**: Max 2 permission frames per chapter
- **Must**: Permission frames only before sensitive questions
- **Must**: Vary permission frame language

**Risk Level**: 🟡 **MEDIUM**
- **Impact**: Overuse feels scripted
- **Impact**: Loses impact when overused

**Forecast**:
- **Without Fix**: 50% chance of overuse
- **With Fix**: 10% chance (requires validation)

---

### CTQ 5: CTA Appropriateness by Funnel Stage ⚠️ **HIGH RISK**

**Customer Need**: "Early chapters shouldn't have hard-sell CTAs"

**Current State**:
- Funnel stage can be specified
- CTA library has different types
- No automatic validation of CTA-to-funnel match

**CTQ Specification**:
- **Must**: Top-funnel chapters: 1 soft CTA only
- **Must**: Mid-funnel chapters: 1 soft CTA, question-based
- **Must**: Lower-funnel chapters: 1 primary CTA
- **Must**: No conversion-stage CTAs in early chapters

**Risk Level**: 🔴 **CRITICAL**
- **Impact**: Too aggressive = breaks trust
- **Impact**: Too soft = missed opportunities

**Forecast**:
- **Without Fix**: 45% chance of CTA mismatch
- **With Fix**: 8% chance (requires validation)

---

### CTQ 6: Compliance Violation Prevention ⚠️ **CRITICAL**

**Customer Need**: "Zero compliance violations across entire book"

**Current State**:
- Compliance enforcer exists
- Validates against 70+ rules
- Can check content after generation

**CTQ Specification**:
- **Must**: 100% compliance rate
- **Must**: All banned words/phrases caught
- **Must**: All alternatives used correctly

**Risk Level**: 🔴 **CRITICAL**
- **Impact**: Compliance violations = legal risk
- **Impact**: Could require book recall/reprint

**Forecast**:
- **Current System**: 5% chance of violation (good)
- **With Pre-Generation Check**: 1% chance

---

### CTQ 7: Structure Variation Across Chapters ⚠️ **MEDIUM RISK**

**Customer Need**: "Chapters shouldn't all follow the same formula"

**Current State**:
- Lessons learned identify repetitive structure
- Content index tracks structure patterns
- No structure variation enforcement

**CTQ Specification**:
- **Must**: At least 5 different chapter structures
- **Must**: Rotate between: story-first, question-first, statistic-first, direct-address, case-study
- **Must**: No identical structure in consecutive chapters

**Risk Level**: 🟡 **MEDIUM**
- **Impact**: Formulaic feel = loses authenticity
- **Impact**: Readers notice pattern

**Forecast**:
- **Without Fix**: 80% chance of repetitive structure
- **With Fix**: 20% chance (requires structure library)

---

### CTQ 8: Emotional Arc Continuity ⚠️ **HIGH RISK**

**Customer Need**: "The book should take readers on a complete emotional journey"

**Current State**:
- Emotional journey map exists
- Chapters can specify emotional goals
- No cross-chapter emotional arc tracking

**CTQ Specification**:
- **Must**: Emotional progression across chapters matches journey map
- **Must**: Chapter emotional states build on previous
- **Must**: No emotional regression without reason

**Risk Level**: 🔴 **CRITICAL**
- **Impact**: Broken emotional arc = lost engagement
- **Impact**: Readers don't complete journey

**Forecast**:
- **Without Fix**: 55% chance of broken arc
- **With Fix**: 12% chance (requires arc tracking)

---

### CTQ 9: Technical Accuracy & Consistency ⚠️ **CRITICAL**

**Customer Need**: "All financial concepts must be accurate and consistent"

**Current State**:
- No technical accuracy validation
- No concept consistency checking
- Relies on AI knowledge

**CTQ Specification**:
- **Must**: All numbers/calculations accurate
- **Must**: Financial concepts consistent across chapters
- **Must**: No contradictory statements

**Risk Level**: 🔴 **CRITICAL**
- **Impact**: Inaccuracy = credibility loss
- **Impact**: Contradictions = confusion

**Forecast**:
- **Current System**: 25% chance of inconsistency
- **With Validation**: 8% chance (requires fact-checking)

---

### CTQ 10: Language Pattern Application ⚠️ **LOW RISK**

**Customer Need**: "Use proven language patterns from transcripts"

**Current State**:
- 7+ language pattern categories loaded
- Patterns included in prompts
- No validation of pattern usage

**CTQ Specification**:
- **Must**: Apply appropriate patterns contextually
- **Must**: Don't overuse any single pattern
- **Must**: Patterns feel natural, not forced

**Risk Level**: 🟢 **LOW**
- **Impact**: Patterns are guidance, not strict rules
- **Impact**: Minor if patterns underused

**Forecast**:
- **Current System**: 30% chance of underuse
- **Acceptable**: Patterns are supportive, not critical

---

### CTQ 11: Word Count & Length Consistency ⚠️ **LOW RISK**

**Customer Need**: "Chapters should be consistent length"

**Current State**:
- Length can be specified
- Format templates have ranges
- No enforcement

**CTQ Specification**:
- **Must**: Chapters within 10% of target length
- **Must**: Consistent pacing across book
- **Must**: No chapters significantly shorter/longer

**Risk Level**: 🟢 **LOW**
- **Impact**: Minor pacing issues
- **Impact**: Easy to fix in editing

**Forecast**:
- **Current System**: 20% chance of length variance
- **Acceptable**: Can be adjusted post-generation

---

### CTQ 12: Cross-Chapter Reference Consistency ⚠️ **MEDIUM RISK**

**Customer Need**: "References to previous chapters should be accurate"

**Current State**:
- No cross-chapter reference tracking
- AI might reference non-existent content
- No validation of "as we discussed in Chapter X"

**CTQ Specification**:
- **Must**: All chapter references must be valid
- **Must**: References must match actual content
- **Must**: No forward references to unwritten chapters

**Risk Level**: 🟡 **MEDIUM**
- **Impact**: Confusion if references wrong
- **Impact**: Breaks continuity

**Forecast**:
- **Without Fix**: 35% chance of invalid reference
- **With Fix**: 10% chance (requires reference validation)

---

## CTQ Priority Matrix

| CTQ | Risk Level | Impact | Likelihood | Priority |
|-----|------------|--------|------------|----------|
| CTQ 1: Narrative Constraints | 🔴 Critical | High | 40% | **P0** |
| CTQ 2: Character Consistency | 🔴 Critical | High | 60% | **P0** |
| CTQ 5: CTA Appropriateness | 🔴 Critical | High | 45% | **P0** |
| CTQ 6: Compliance | 🔴 Critical | High | 5% | **P0** |
| CTQ 8: Emotional Arc | 🔴 Critical | High | 55% | **P0** |
| CTQ 9: Technical Accuracy | 🔴 Critical | High | 25% | **P0** |
| CTQ 3: Signature Phrase Rotation | 🟡 Medium | Medium | 70% | **P1** |
| CTQ 4: Permission Frames | 🟡 Medium | Medium | 50% | **P1** |
| CTQ 7: Structure Variation | 🟡 Medium | Medium | 80% | **P1** |
| CTQ 12: Cross-Chapter References | 🟡 Medium | Medium | 35% | **P1** |
| CTQ 10: Language Patterns | 🟢 Low | Low | 30% | **P2** |
| CTQ 11: Word Count | 🟢 Low | Low | 20% | **P2** |

---

## Forecast: System Performance

### Overall Consistency Forecast

**Without Fixes**:
- **High Consistency** (90%+): 25% of chapters
- **Medium Consistency** (70-90%): 50% of chapters
- **Low Consistency** (<70%): 25% of chapters

**With P0 Fixes**:
- **High Consistency** (90%+): 75% of chapters
- **Medium Consistency** (70-90%): 20% of chapters
- **Low Consistency** (<70%): 5% of chapters

### Book Completion Forecast

**Probability of Successfully Generating Complete Book**:
- **Without Fixes**: 60% (high risk of inconsistencies requiring major edits)
- **With P0 Fixes**: 85% (minor edits needed)
- **With All Fixes**: 95% (polish edits only)

---

## Recommendations

### Immediate Actions (P0)

1. **Clarify Narrative Constraints**
   - Update system prompt: "ONLY use narratives/metaphors/allegories from framework"
   - Add validation: Flag if AI creates new narrative
   - Create process: New narratives require human approval

2. **Implement Character State Tracking**
   - Create character state database
   - Validate character references against state
   - Track character evolution across chapters

3. **Add CTA-to-Funnel Validation**
   - Validate CTA type matches funnel stage
   - Reject content with mismatched CTAs
   - Provide CTA recommendations by stage

4. **Implement Cross-Chapter Reference Validation**
   - Track all chapter references
   - Validate "as discussed in Chapter X" statements
   - Prevent forward references

5. **Add Technical Accuracy Checks**
   - Fact-check financial calculations
   - Validate concept consistency
   - Flag contradictions

### Short-Term Actions (P1)

6. **Implement Signature Phrase Rotation**
   - Track usage across book
   - Enforce 5-chapter separation
   - Provide rotation schedule

7. **Add Permission Frame Limits**
   - Enforce max 2 per chapter
   - Validate strategic placement
   - Track usage

8. **Create Structure Variation System**
   - Build structure library (5+ templates)
   - Rotate structures across chapters
   - Prevent consecutive identical structures

### Long-Term Actions (P2)

9. **Language Pattern Usage Tracking** (optional)
10. **Word Count Validation** (optional)

---

## Success Criteria

### Minimum Viable Book Generation

✅ **Must Achieve**:
- 100% compliance rate
- 90%+ character consistency
- 90%+ narrative framework adherence
- 85%+ CTA appropriateness
- 80%+ emotional arc continuity

### Target Book Generation

✅ **Should Achieve**:
- 95%+ overall consistency
- 90%+ structure variation
- 90%+ signature phrase rotation
- 95%+ technical accuracy

---

**Next Step**: See `STRESS_TEST_ANALYSIS.md` for detailed edge case testing.

