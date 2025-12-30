# Stress Test Recommendations: Implementation Plan

**Date**: 2025-12-27  
**Priority**: P0 (Critical) - Implement before book generation

---

## Quick Answer: Can AI Create New Narratives?

### Current State: ⚠️ **AMBIGUOUS**

The system does NOT explicitly forbid AI from creating new narratives/metaphors/allegories. The prompt says:
- "Reference framework elements when relevant"
- "Use narratives: [NARRATIVE_IDS]" (if provided)

But it does NOT say:
- "ONLY use narratives from framework"
- "Do NOT create new narratives"

### Recommendation: 🔴 **CRITICAL FIX REQUIRED**

**Answer**: AI should NOT be allowed to create new narratives without human approval. The system should:
1. Explicitly state: "ONLY use narratives/metaphors/allegories from the framework"
2. Validate that all narratives used are in framework
3. Flag if AI creates new narrative (pattern detection)
4. Require human approval for new narratives

---

## Implementation Priority

### P0: Critical - Implement Before Book Generation

1. **Narrative Constraint Clarification** (2 hours)
2. **Character State Tracking** (4 hours)
3. **CTA-to-Funnel Validation** (3 hours)
4. **Emotional Arc Tracking** (4 hours)
5. **Cross-Chapter Reference Validation** (3 hours)
6. **Book-Level Quality Tracking** (6 hours)

**Total P0 Time**: ~22 hours

### P1: Important - Implement During Book Generation

7. **Signature Phrase Rotation** (3 hours)
8. **Structure Variation System** (4 hours)
9. **Permission Frame Limits** (2 hours)

**Total P1 Time**: ~9 hours

---

## Detailed Implementation Plans

### Fix 1: Narrative Constraint Clarification

**File**: `ai_prompts/system_prompts/base_system_prompt.yaml`

**Change**:
```yaml
required_elements:
  - "ONLY use narratives, metaphors, and allegories from the framework"
  - "If no suitable narrative exists, flag for human review - DO NOT create new ones"
  - "Reference framework elements when relevant (characters, stories, tools)"
```

**File**: `ai_prompts/prompt_builder.py`

**Add Validation**:
```python
def validate_narrative_usage(self, content: str, narrative_ids: List[str]) -> List[str]:
    """Check if content uses only specified narratives"""
    violations = []
    # Pattern match to detect new narratives
    # Check against framework
    return violations
```

**File**: `meta_framework/content_quality/content_validator.py`

**Add Check**:
```python
def check_narrative_compliance(self, content: str, narrative_ids: List[str]) -> bool:
    """Validate all narratives are from framework"""
    # Implementation
```

---

### Fix 2: Character State Tracking

**New File**: `meta_framework/characters/character_state.yaml`

**Structure**:
```yaml
character_states:
  JOHN_SMITH:
    base_profile:
      name: "John Smith"
      income: 100000
      situation: "single_father"
      age: 45
    usage_tracking:
      chapters: [2, 5, 8, 12]
      last_reference: "Chapter 8"
    state_locks:
      income: 100000  # Cannot change
      situation: "single_father"  # Cannot change
```

**File**: `meta_framework/content_quality/content_validator.py`

**Add Check**:
```python
def validate_character_reference(self, content: str, character_id: str) -> Dict:
    """Validate character reference matches state"""
    # Load character state
    # Extract character details from content
    # Compare and flag inconsistencies
```

---

### Fix 3: CTA-to-Funnel Validation

**File**: `meta_framework/tools_ctas/cta_funnel_rules.yaml`

**New File**:
```yaml
cta_funnel_rules:
  top_of_funnel:
    allowed_cta_types: ["soft_cta", "question_based_cta"]
    max_count: 1
    forbidden_phrases: ["schedule", "consultation", "call now"]
  mid_funnel:
    allowed_cta_types: ["soft_cta", "question_based_cta", "curiosity_cta"]
    max_count: 1
  lower_funnel:
    allowed_cta_types: ["primary_cta", "urgency_cta"]
    max_count: 1
```

**File**: `meta_framework/content_quality/content_validator.py`

**Add Check**:
```python
def validate_cta_funnel_match(self, content: str, funnel_stage: str) -> bool:
    """Validate CTA matches funnel stage"""
    # Extract CTAs from content
    # Check against funnel rules
    # Flag mismatches
```

---

### Fix 4: Emotional Arc Tracking

**New File**: `meta_framework/chapters/emotional_arc_tracker.yaml`

**Structure**:
```yaml
book_emotional_arc:
  target_progression:
    - chapter_1: "fear"
    - chapter_2: "concern"
    - chapter_3: "hope"
    - chapter_4: "confidence"
    - chapter_5: "action"
  actual_progression: []
  validation_rules:
    - "No regression without reason"
    - "Must progress toward action"
```

**File**: `meta_framework/content_quality/content_validator.py`

**Add Check**:
```python
def validate_emotional_progression(self, chapter_num: int, emotional_state: str) -> bool:
    """Validate emotional state matches progression"""
    # Load arc tracker
    # Check against previous chapters
    # Validate progression
```

---

### Fix 5: Cross-Chapter Reference Validation

**New File**: `meta_framework/chapters/chapter_references.yaml`

**Structure**:
```yaml
chapter_references:
  chapter_8:
    references:
      - target: "chapter_3"
        text: "as we discussed in Chapter 3"
        topic: "tax leak"
        validated: true
  chapter_10:
    references:
      - target: "chapter_2"
        text: "Remember from Chapter 2"
        topic: "John Smith"
        validated: false  # John not in Chapter 2
```

**File**: `meta_framework/content_quality/content_validator.py`

**Add Check**:
```python
def validate_chapter_references(self, content: str, chapter_num: int) -> List[str]:
    """Extract and validate all chapter references"""
    # Extract "Chapter X" references
    # Check if target chapter exists
    # Check if referenced content matches
    # Flag invalid references
```

---

### Fix 6: Book-Level Quality Tracking

**New File**: `scripts/book_quality_tracker.py`

**Features**:
- Track quality metrics across all chapters
- Generate book-level consistency reports
- Flag degradation trends
- Provide quality checkpoints

**Integration**:
- Run after every 5 chapters
- Generate cumulative reports
- Flag issues before they compound

---

## Testing Plan

### Phase 1: Unit Tests (P0 Fixes)

1. Test narrative constraint enforcement
2. Test character state validation
3. Test CTA-to-funnel matching
4. Test emotional arc progression
5. Test chapter reference validation

### Phase 2: Integration Tests

1. Generate 3 test chapters with all fixes
2. Validate consistency across chapters
3. Check all validations work together
4. Measure improvement vs. baseline

### Phase 3: Full Book Test

1. Generate 15-chapter book
2. Run all validations
3. Measure success rate
4. Compare to forecast

---

## Success Metrics

### Before Fixes (Baseline)
- Narrative compliance: 60%
- Character consistency: 50%
- CTA appropriateness: 70%
- Emotional arc continuity: 80%
- Overall consistency: 65%

### After P0 Fixes (Target)
- Narrative compliance: 95%
- Character consistency: 90%
- CTA appropriateness: 92%
- Emotional arc continuity: 88%
- Overall consistency: 85%

---

## Risk Mitigation

### If Fixes Not Implemented

**Risk**: 40% chance of major issues requiring significant editing

**Mitigation**:
- Manual review of every chapter
- Post-generation validation scripts
- Human editor required for all content

### If Fixes Implemented

**Risk**: 5% chance of minor issues

**Mitigation**:
- Automated validation catches most issues
- Human review for polish only
- Faster book completion

---

**Status**: Ready for implementation  
**Next Step**: Begin P0 fixes before book generation starts

