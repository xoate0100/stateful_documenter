# Implementation Decisions - AI Book Generation Fixes

**Date**: 2025-12-27  
**Purpose**: Document all human decisions required before implementing stress test fixes  
**Status**: ✅ **DECISIONS COMPLETE - IMPLEMENTATION IN PROGRESS**

---

## Instructions

1. Review each section below
2. Fill in your decisions in the **"YOUR DECISION"** fields
3. Add any additional notes or constraints
4. Save this document
5. Return to me for implementation

---

## P0: Critical Fixes (Must Implement Before Book Generation)

### Fix 1: Narrative Constraint Clarity

**Issue**: System doesn't explicitly forbid AI from creating new narratives/metaphors/allegories

**Question 1.1: Strictness Level**
- [ ] **Option A: STRICT** - AI can ONLY use narratives from framework. If no suitable narrative exists, AI must flag for human review and stop generation.
- [ ] **Option B: FLEXIBLE** - AI can ONLY use narratives from framework, but if no suitable narrative exists, AI can suggest a new narrative (with flag) and continue with closest match.
- [ ] **Option C: HYBRID** - AI can ONLY use narratives from framework. If no suitable narrative exists, AI stops and provides list of closest matches for human to choose.

**YOUR DECISION**: Option B. Ideally the AI will generate new narratives when required (human to review) we should build our narratives similiarly to our "lessons learned" and match specific narrative scenarios to emotional journey (what emotional state are we identifying in our reader and what emotional state are we moving them to - all to assist conversions)

**Question 1.2: Validation Approach**
- [ ] **Option A: PRE-GENERATION** - Validate narrative_ids before prompt is sent to AI
- [ ] **Option B: POST-GENERATION** - Check generated content for unauthorized narratives
- [ ] **Option C: BOTH** - Validate before AND after

**YOUR DECISION**: Validate before and after

**Question 1.3: New Narrative Approval Process**
If AI needs a new narrative (or human wants to add one):
- [ ] **Option A: MANUAL ONLY** - Human must create narrative file in framework first
- [ ] **Option B: AI ASSISTED** - AI can draft narrative, but human must approve before use
- [ ] **Option C: AUTO-APPROVE** - If narrative is flagged and approved, add to framework automatically

**YOUR DECISION**: AI Assisted, the AI should draft the narrative and request user approval (once approved it should be added to the narratives repository and an entry in our "narrative generation" tracker should be made that explicitly lines out what emotional state the narrative connects to the reader on and what emotional state the outcome of the narrative is intended )

**Additional Notes**: _________________________

---

### Fix 2: Character State Tracking

**Issue**: Character profiles change across chapters (50% failure rate)

**Question 2.1: Character State Locking**
What should be locked (cannot change)?
- [ ] **Option A: ALL ATTRIBUTES** - Name, income, situation, age, etc. - all locked
- [ ] **Option B: CORE ATTRIBUTES** - Income, situation, age locked; minor details can vary
- [ ] **Option C: CUSTOM** - Specify which attributes to lock: _________________________

**YOUR DECISION**: We should lock all attributes to maintain character consistency (attributes can be added as the "story" requires,but those should be updated in the character tracker so it maintains consistency)

**Question 2.2: Character Evolution**
Should characters be allowed to evolve over the book?
- [ ] **Option A: NO EVOLUTION** - Characters remain static throughout book
- [ ] **Option B: CONTROLLED EVOLUTION** - Characters can evolve, but changes must be tracked and approved
- [ ] **Option C: FREE EVOLUTION** - Characters can evolve naturally (tracked but not restricted)

**YOUR DECISION**: Character evolution should be done controlled, for the reason that we are attempting to garner lead conversions to sales and we need our readers to identify with the beginning state of the character and "move" with the character to the desired end emotional/logical state

**Question 2.3: Character Reference Format**
How should characters be referenced?
- [ ] **Option A: FULL PROFILE** - Always include full profile (name, income, situation)
- [ ] **Option B: CONTEXTUAL** - Include only relevant details for context
- [ ] **Option C: MINIMAL** - Just name, assume reader remembers details

**YOUR DECISION**: Contextual, copy should read natural and human. 

**Question 2.4: Character Validation Strictness**
- [ ] **Option A: STRICT** - Reject content if ANY character detail doesn't match state
- [ ] **Option B: WARN** - Flag inconsistencies but allow (with warning)
- [ ] **Option C: FLEXIBLE** - Only validate core attributes (income, situation)

**YOUR DECISION**: Flag inconsistencies for explicit review (an "editor" tracker that delivers statistics based on our comparison scripts for content generation would be great, file name, line number, scenario overview, specific issue/flag)

**Additional Notes**: _________________________

---

### Fix 3: CTA Appropriateness by Funnel Stage

**Issue**: CTAs don't match funnel stage (30% failure rate)

**Question 3.1: CTA Validation Strictness**
- [ ] **Option A: STRICT** - Reject content if CTA doesn't match funnel stage
- [ ] **Option B: WARN** - Flag mismatch but allow (with warning)
- [ ] **Option C: SUGGEST** - Suggest appropriate CTA but allow override

**YOUR DECISION**: Reject content if CTA doesn't match funnel stage

**Question 3.2: CTA Count Limits**
Maximum CTAs per chapter by funnel stage:
- **Top-funnel**: [ ] 1 [ ] 2 [ ] Other: _________
- **Mid-funnel**: [ ] 1 [ ] 2 [ ] Other: _________
- **Lower-funnel**: [ ] 1 [ ] 2 [ ] Other: _________

**YOUR DECISION**: 
- Top-funnel: 1
- Mid-funnel: 3
- Lower-funnel: 4

**Question 3.3: Forbidden Phrases by Stage**
What phrases should be forbidden in top-funnel?
- [ ] "Schedule a consultation"
- [ ] "Call now"
- [ ] "Book a meeting"
- [ ] Other: _________________________

**YOUR DECISION**: This is going to have to be context dependent, sometimes it will be appropriate top of funnel. 

**Question 3.4: CTA Auto-Correction**
If CTA is inappropriate, should system:
- [ ] **Option A: REJECT** - Reject content, require regeneration
- [ ] **Option B: REPLACE** - Automatically replace with appropriate CTA
- [ ] **Option C: SUGGEST** - Suggest replacement, require approval

**YOUR DECISION**: Replace with appropriate CTA (or relevant "pre-sell" like "read more about this in chapter 6" for example)

**Additional Notes**: _________________________

---

### Fix 4: Emotional Arc Continuity

**Issue**: Emotional progression breaks (20% failure rate)

**Question 4.1: Emotional Arc Enforcement**
- [ ] **Option A: STRICT** - Reject content if emotional state doesn't match progression
- [ ] **Option B: WARN** - Flag regression but allow (with warning)
- [ ] **Option C: GUIDANCE** - Provide emotional state recommendations, but allow override

**YOUR DECISION**: Warn

**Question 4.2: Regression Handling**
If emotional state regresses (e.g., Hope → Fear):
- [ ] **Option A: FORBIDDEN** - Never allow regression
- [ ] **Option B: ALLOW WITH REASON** - Allow if AI provides justification
- [ ] **Option C: ALLOW** - Track but don't restrict

**YOUR DECISION**: Allow with reason

**Question 4.3: Emotional State Granularity**
How specific should emotional states be?
- [ ] **Option A: BROAD** - Fear, Concern, Hope, Confidence, Action (5 states)
- [ ] **Option B: MEDIUM** - Add sub-states (e.g., Mild Concern, Deep Concern)
- [ ] **Option C: CUSTOM** - Specify states: _________________________

**YOUR DECISION**: Medium, let's track sub-states and match our content granularly

**Question 4.4: Chapter-to-Chapter Transitions**
Should emotional transitions be:
- [ ] **Option A: SMOOTH** - Gradual transitions only (e.g., Fear → Concern → Hope)
- [ ] **Option B: ALLOWED JUMPS** - Can skip states (e.g., Fear → Hope) if justified
- [ ] **Option C: FLEXIBLE** - Any transition allowed, just track it

**YOUR DECISION**: Smooth

**Additional Notes**: _________________________

---

### Fix 5: Cross-Chapter Reference Validation

**Issue**: Invalid or inaccurate chapter references (25% failure rate)

**Question 5.1: Reference Validation Strictness**
- [ ] **Option A: STRICT** - Reject content if ANY reference is invalid
- [ ] **Option B: WARN** - Flag invalid references but allow (with warning)
- [ ] **Option C: VALIDATE ONLY** - Check and report, but don't block

**YOUR DECISION**: Strict

**Question 5.2: Forward Reference Handling**
If Chapter 5 references Chapter 10 (not yet written):
- [ ] **Option A: FORBIDDEN** - Never allow forward references
- [ ] **Option B: ALLOWED** - Allow if chapter is planned
- [ ] **Option C: FLAG** - Flag for review, allow if approved

**YOUR DECISION**: B: Allowed

**Question 5.3: Reference Accuracy Check**
How strict should content matching be?
- [ ] **Option A: EXACT MATCH** - Referenced topic must exactly match chapter content
- [ ] **Option B: RELATED** - Referenced topic must be related/mentioned
- [ ] **Option C: LOOSE** - Just check that chapter exists

**YOUR DECISION**: Option B: Related

**Question 5.4: Reference Format**
Preferred reference format:
- [ ] **Option A: "As we discussed in Chapter 3..."**
- [ ] **Option B: "Remember from Chapter 3..."**
- [ ] **Option C: "In Chapter 3, we covered..."**
- [ ] **Option D: ANY** - All formats acceptable

**YOUR DECISION**: Option D: Any

**Additional Notes**: _________________________

---

### Fix 6: Book-Level Quality Tracking

**Issue**: Quality degrades at scale (25% failure rate)

**Question 6.1: Checkpoint Frequency**
When should quality checkpoints run?
- [ ] **Option A: EVERY CHAPTER** - Check after each chapter
- [ ] **Option B: EVERY 3 CHAPTERS** - Check after chapters 3, 6, 9, 12, 15
- [ ] **Option C: EVERY 5 CHAPTERS** - Check after chapters 5, 10, 15
- [ ] **Option D: CUSTOM** - Specify: _________________________

**YOUR DECISION**: Every Chapter

**Question 6.2: Quality Metrics to Track**
Which metrics should be tracked?
- [ ] Compliance rate
- [ ] Character consistency
- [ ] Narrative adherence
- [ ] CTA appropriateness
- [ ] Emotional arc continuity
- [ ] Structure variation
- [ ] Signature phrase rotation
- [ ] Technical accuracy
- [ ] Other: _________________________

**YOUR DECISION**: All of the above (and any others that will help maintain quality during content generation)

**Question 6.3: Quality Thresholds**
What quality threshold triggers action?
- [ ] **Option A: 90%** - Action if any metric drops below 90%
- [ ] **Option B: 85%** - Action if any metric drops below 85%
- [ ] **Option C: CUSTOM** - Specify: _________________________

**YOUR DECISION**: A 90% if any metric drops  below

**Question 6.4: Quality Degradation Response**
If quality degrades:
- [ ] **Option A: STOP** - Stop generation, require review
- [ ] **Option B: WARN** - Continue but flag for review
- [ ] **Option C: AUTO-FIX** - Attempt automatic corrections

**YOUR DECISION**: Option B: Warn and flag for review

**Additional Notes**: _________________________

---

## P1: Important Fixes (Implement During Book Generation)

### Fix 7: Signature Phrase Rotation

**Issue**: Same signature phrases appear in multiple chapters (40% failure rate)

**Question 7.1: Rotation Distance**
Minimum chapters between same signature phrase:
- [ ] **Option A: 5 chapters** (current recommendation)
- [ ] **Option B: 3 chapters**
- [ ] **Option C: 7 chapters**
- [ ] **Option D: CUSTOM** - Specify: _________________________

**YOUR DECISION**: At least 3 chapters (can we generate additional signature phrases to be approved and build an additive repository of these similarly to our characters and narratives?)

**Question 7.2: Rotation Enforcement**
- [ ] **Option A: STRICT** - Reject content if phrase used too recently
- [ ] **Option B: WARN** - Flag but allow (with warning)
- [ ] **Option C: SUGGEST** - Suggest alternative phrases

**YOUR DECISION**: Strict

**Question 7.3: Contextual Exceptions**
Allow exceptions if phrase is contextually perfect?
- [ ] **Option A: NO EXCEPTIONS** - Always enforce rotation
- [ ] **Option B: ALLOW WITH APPROVAL** - Flag for human review
- [ ] **Option C: AUTO-ALLOW** - Allow if context is perfect

**YOUR DECISION**: B Allow with Approval

**Additional Notes**: _________________________

---

### Fix 8: Structure Variation

**Issue**: All chapters follow same formula (60% failure rate)

**Question 8.1: Structure Library**
How many different structures should be available?
- [ ] **Option A: 5 structures** (minimum recommendation)
- [ ] **Option B: 7 structures**
- [ ] **Option C: 10 structures**
- [ ] **Option D: CUSTOM** - Specify: _________________________

**YOUR DECISION**: Option C 10 Structures ( to allow for maximum variablity, alothough it shouldn't be expected that they can't be reused. For example, we may use structure 4 for both chapters 2 and 8, but in a book with 10 chapters we don't need total uniqueness for chapter structure, it should be flexible enough to appear sincere and genuine while assisting conversions to paying clients)

**Question 8.2: Structure Types**
Which structure types should be included?
- [ ] Story-first (opens with narrative)
- [ ] Question-first (opens with question)
- [ ] Statistic-first (opens with data)
- [ ] Direct-address (opens with "You...")
- [ ] Case-study-first (opens with case study)
- [ ] Problem-first (opens with problem statement)
- [ ] Other: _________________________

**YOUR DECISION**: All of the above (and any others we can create to assist in delivering the content in a high-converting format)

**Question 8.3: Structure Rotation**
- [ ] **Option A: STRICT** - No consecutive identical structures
- [ ] **Option B: ALLOW 2 IN A ROW** - Can repeat once, but not three times
- [ ] **Option C: FLEXIBLE** - Track but don't enforce

**YOUR DECISION**: Option C: Flexible track (this should show up in the "editors" review with the relevant stats)

**Question 8.4: Structure Selection**
How should structure be selected?
- [ ] **Option A: AUTO-ROTATE** - System automatically rotates
- [ ] **Option B: RECOMMEND** - System recommends, human chooses
- [ ] **Option C: MANUAL** - Human always chooses

**YOUR DECISION**: B: recommend (ai can choose this dynamically when generating the prompts)

**Additional Notes**: _________________________

---

### Fix 9: Permission Frame Limits

**Issue**: Permission frames overused (identified in lessons learned)

**Question 9.1: Permission Frame Limit**
Maximum permission frames per chapter:
- [ ] **Option A: 1** (very strict)
- [ ] **Option B: 2** (current recommendation)
- [ ] **Option C: 3** (flexible)
- [ ] **Option D: CUSTOM** - Specify: B

**YOUR DECISION**: Option B: 2*

**Question 9.2: Enforcement**
- [ ] **Option A: STRICT** - Reject if limit exceeded
- [ ] **Option B: WARN** - Flag but allow (with warning)
- [ ] **Option C: SUGGEST** - Suggest removal of excess frames

**YOUR DECISION**: Strict

**Question 9.3: Permission Frame Variety**
Should system enforce variety in permission frame language?
- [ ] **Option A: YES** - Require different phrases
- [ ] **Option B: NO** - Same phrase OK if used appropriately
- [ ] **Option C: SUGGEST** - Suggest variety but don't enforce

**YOUR DECISION**: Yes variety (permission frames can be dynamic and "chosen" by the AI or we can include a permission frame repository for our ai to choose from and suggest additions to similar to narratives, character, and signature phrase repos we will be creating)

**Additional Notes**: _________________________

---

## General Implementation Questions

### Question G1: Validation Timing
When should validations run?
- [ ] **Option A: PRE-GENERATION** - Validate before sending to AI
- [ ] **Option B: POST-GENERATION** - Validate after AI generates content
- [ ] **Option C: BOTH** - Validate before and after
- [ ] **Option D: REAL-TIME** - Validate during generation (if possible)

**YOUR DECISION**: Option D: Real-time and before and after

### Question G2: Error Handling
If validation fails:
- [ ] **Option A: REJECT** - Reject content, require regeneration
- [ ] **Option B: WARN** - Flag issues but allow (with warnings)
- [ ] **Option C: AUTO-FIX** - Attempt automatic fixes
- [ ] **Option D: HYBRID** - Reject critical issues, warn minor issues

**YOUR DECISION**: Auto-Fix, track unfixable issues for review and continue without blocking

### Question G3: Human Review Process
When should content require human review?
- [ ] **Option A: ALWAYS** - All content requires review
- [ ] **Option B: ON FAILURE** - Only if validation fails
- [ ] **Option C: RANDOM SAMPLE** - Review random sample
- [ ] **Option D: CHECKPOINTS** - Review at quality checkpoints

**YOUR DECISION**: REview at Quality Checkpoints

### Question G4: Reporting Level
How detailed should validation reports be?
- [ ] **Option A: SUMMARY** - High-level pass/fail
- [ ] **Option B: DETAILED** - Full breakdown of all checks
- [ ] **Option C: CUSTOMIZABLE** - User chooses detail level
- [ ] **Option D: HIERARCHICAL** - Summary with expandable details

**YOUR DECISION**: HIERARCHICAL

### Question G5: Implementation Priority
Which fixes should be implemented first?
- [ ] **Option A: ALL P0 FIRST** - Implement all 6 P0 fixes before any P1
- [ ] **Option B: ITERATIVE** - Implement 2-3 fixes, test, then continue
- [ ] **Option C: PARALLEL** - Implement multiple fixes simultaneously
- [ ] **Option D: CUSTOM ORDER** - Specify order: _________________________

**YOUR DECISION**: Iterative (in order of dependent priority)

---

## Additional Constraints or Requirements

**Any other constraints, requirements, or preferences not covered above?**

_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________

---

## Decision Summary

Once you've filled in all decisions, I'll use this document to:
1. Implement all fixes according to your preferences
2. Create validation systems with your chosen strictness levels
3. Build tracking systems with your specified checkpoints
4. Generate implementation code matching your decisions

**Status**: ⏳ **AWAITING YOUR DECISIONS**

**Next Step**: Fill in this document and return for implementation.

