# Content Validation Guide

**Last Updated:** 2025-12-27

Complete guide to the content validation system with all quality checks, auto-fixes, and tracking.

---

## Overview

The content validation system provides comprehensive quality assurance for all generated content, with:

- **Pre-generation validation**: Check narratives, characters, framework elements before generation
- **Post-generation validation**: 8+ validation checks on generated content
- **Auto-fix system**: Automatic correction of fixable issues
- **Quality checkpoints**: Automatic quality tracking after every chapter
- **Editor tracker**: Issue flagging with file, line, scenario details

---

## Validation Systems

### 1. Narrative Validation

**Purpose**: Ensure only framework narratives are used

**Checks**:
- Pre-generation: Validate narrative IDs exist in framework
- Post-generation: Detect unauthorized narratives
- AI-assisted creation: New narratives require approval

**Files**:
- `meta_framework/narratives/narrative_validator.py`
- `meta_framework/narratives/narrative_generation_tracker.yaml`

**Usage**:
```python
from meta_framework.narratives.narrative_validator import NarrativeValidator

validator = NarrativeValidator()
is_valid, missing, suggestions = validator.validate_narrative_ids(["ALLEGORY_LEAKY_BUCKET"])
```

---

### 2. Character State Validation

**Purpose**: Ensure character consistency across all chapters

**Checks**:
- All attributes locked by default
- Character references match state
- Controlled evolution tracked
- Usage tracked across chapters

**Files**:
- `meta_framework/characters/character_state_manager.py`
- `meta_framework/characters/character_state.yaml`

**Usage**:
```python
from meta_framework.characters.character_state_manager import CharacterStateManager

manager = CharacterStateManager()
manager.record_character_usage("JOHN_SMITH", chapter_num=5, content=content)
```

---

### 3. CTA Appropriateness Validation

**Purpose**: Ensure CTAs match funnel stage

**Rules**:
- Top-funnel: Max 1 CTA (soft/question-based)
- Mid-funnel: Max 3 CTAs
- Lower-funnel: Max 4 CTAs
- Auto-fix: Replace inappropriate CTAs

**Files**:
- `meta_framework/tools_ctas/cta_funnel_rules.yaml`
- `meta_framework/content_quality/book_validator.py`

**Auto-Fix**:
- Inappropriate CTAs automatically replaced
- Pre-sell references used when needed ("Read more in Chapter X")

---

### 4. Emotional Arc Validation

**Purpose**: Ensure smooth emotional progression

**Checks**:
- Sub-state tracking (mild/moderate/deep)
- Smooth transitions preferred
- Regression allowed with justification
- Warnings (doesn't block)

**Files**:
- `meta_framework/chapters/emotional_arc_tracker.yaml`
- `meta_framework/content_quality/book_validator.py`

---

### 5. Chapter Reference Validation

**Purpose**: Validate all cross-chapter references

**Checks**:
- Strict validation: Reject if invalid
- Forward references allowed if chapter planned
- Related content matching (not exact)
- Any reference format acceptable

**Files**:
- `meta_framework/chapters/chapter_references.yaml`
- `meta_framework/content_quality/book_validator.py`

---

### 6. Signature Phrase Rotation

**Purpose**: Prevent over-repetition of signature phrases

**Rules**:
- Minimum 3 chapters between uses
- Strict enforcement: Reject if too recent
- Allow with approval if contextually perfect

**Files**:
- `meta_framework/language/signature_phrases_repository.yaml`
- `meta_framework/content_quality/book_validator.py`

---

### 7. Permission Frame Limits

**Purpose**: Prevent overuse of permission frames

**Rules**:
- Max 2 per chapter
- Strict enforcement: Reject if limit exceeded
- Require variety: Different phrases if using multiple

**Files**:
- `meta_framework/language/permission_frames_repository.yaml`
- `meta_framework/content_quality/book_validator.py`

---

### 8. Structure Variation Tracking

**Purpose**: Track structure usage for variety

**Features**:
- 10-structure library
- Flexible tracking (doesn't enforce strict rotation)
- AI recommends dynamically
- Shows in editor review

**Files**:
- `meta_framework/chapters/structure_library.yaml`
- `ai_prompts/prompt_builder.py`

---

## Quality Checkpoints

### Automatic Checkpoints

Quality checkpoints run automatically after every chapter:

**Metrics Tracked**:
- Compliance rate
- Character consistency
- Narrative adherence
- CTA appropriateness
- Emotional arc continuity
- Structure variation
- Signature phrase rotation
- Technical accuracy
- Overall consistency

**Threshold**: 90% - Warns if any metric drops below

**Reporting**: Hierarchical (summary with expandable details)

**Files**:
- `scripts/book_quality_tracker.py`
- `content/book_quality_tracker.yaml`

---

## Editor Tracker

### Issue Flagging

The editor tracker flags issues for review with:
- File path
- Line number (when available)
- Scenario overview
- Specific issue/flag
- Timestamp

**Files**:
- `content/editor_tracker/issues.yaml`
- `meta_framework/content_quality/book_validator.py` (EditorTracker class)

---

## Usage Examples

### Full Validation Workflow

```python
from scripts.generate_content_with_quality import generate_content, save_and_validate_content

# 1. Generate content
result = generate_content(
    topic="Tax Planning for Retirement",
    format_type="chapter",
    platform="book",
    funnel_stage="mid_funnel",
    persona="engineer_retiree",
    emotional_goal="curiosity",
    narrative_id="ALLEGORY_LEAKY_BUCKET",
    character_ids=["JOHN_SMITH"],
    chapter_num=5,
    emotional_state="hope"
)

# 2. AI generates content (external step)
generated_content = "..."  # From ChatGPT/Claude

# 3. Validate content
validation = save_and_validate_content(
    content_id=result['content_id'],
    content=generated_content,
    chapter_num=5
)

# 4. Check results
if validation['is_valid']:
    print("✅ Content passed all validations")
else:
    print("❌ Issues found:")
    for issue in validation['issues']:
        print(f"  - {issue}")

# 5. Review quality metrics
if validation['checkpoint']:
    metrics = validation['checkpoint']['metrics']
    print(f"Overall Consistency: {metrics['overall_consistency']:.1%}")
    print(f"Character Consistency: {metrics['character_consistency']:.1%}")
    print(f"CTA Appropriateness: {metrics['cta_appropriateness']:.1%}")
```

### Manual Validation

```python
from meta_framework.content_quality.book_validator import BookValidator

validator = BookValidator()

results = validator.validate_all(
    content=content,
    metadata=metadata,
    chapter_num=5
)

print(f"Valid: {results['is_valid']}")
print(f"Issues: {results['issues']}")
print(f"Warnings: {results['warnings']}")
print(f"Auto-Fixes: {results['auto_fixes']}")
```

---

## Validation Results

### Result Structure

```python
{
    'is_valid': bool,  # True if passes all critical checks
    'issues': List[str],  # Critical issues (blocking)
    'warnings': List[str],  # Warnings (non-blocking)
    'auto_fixes': List[str],  # Auto-fixes applied
    'corrected_content': str,  # Content after auto-fixes
    'checkpoint': Dict,  # Quality checkpoint results (if chapter)
    'content_file': str,  # Path to saved content
    'metadata_file': str  # Path to metadata file
}
```

### Quality Checkpoint Structure

```python
{
    'chapter_num': int,
    'timestamp': str,
    'metrics': {
        'compliance_rate': float,
        'character_consistency': float,
        'narrative_adherence': float,
        'cta_appropriateness': float,
        'emotional_arc_continuity': float,
        'structure_variation': float,
        'signature_phrase_rotation': float,
        'technical_accuracy': float,
        'overall_consistency': float
    },
    'validation_results': {
        'is_valid': bool,
        'issues_count': int,
        'warnings_count': int,
        'auto_fixes_count': int
    }
}
```

---

## Best Practices

1. **Always use `generate_content_with_quality.py`** for book chapters
2. **Review validation results** before publishing
3. **Check quality checkpoints** after every chapter
4. **Review editor tracker** for flagged issues
5. **Fix critical issues** before continuing
6. **Monitor quality trends** across chapters

---

## Troubleshooting

### Common Issues

**Issue**: "Narrative not found in framework"
- **Solution**: Use existing narrative or request AI-assisted creation

**Issue**: "Character inconsistency detected"
- **Solution**: Check character state, update if evolution is intentional

**Issue**: "CTA doesn't match funnel stage"
- **Solution**: Auto-fix will replace, but review appropriateness

**Issue**: "Too many permission frames"
- **Solution**: Reduce to max 2, vary language

**Issue**: "Signature phrase used too recently"
- **Solution**: Use different phrase or request approval exception

---

## Related Documentation

- `docs/analysis/IMPLEMENTATION_STATUS.md` - Implementation details
- `docs/analysis/INTEGRATION_COMPLETE.md` - System integration
- `docs/analysis/STRESS_TEST_ANALYSIS.md` - Edge case testing
- `README.md` - Project overview

---

*For questions or issues, review the implementation documentation or check the editor tracker for flagged issues.*
