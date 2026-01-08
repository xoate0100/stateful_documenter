# Chapter Regeneration Guide

**Date**: 2025-12-28  
**Purpose**: Step-by-step guide for regenerating all chapters with enhanced validation

---

## Overview

All chapter prompts have been generated with enhanced length requirements and validation. This guide walks you through regenerating all 6 chapters to meet the 3,000-4,000 word requirement.

---

## Current Status

✅ **Prompts Generated**: All 6 chapters  
✅ **Validation System**: Active and enforced  
✅ **Length Requirements**: Explicit in all prompts  
✅ **Ready for**: AI content generation

---

## Regeneration Workflow

### Step 1: Generate Content with AI

For each chapter, use the generated prompt with your AI (ChatGPT/Claude):

1. **Open the prompt file**:
   - Location: `content/prompts/book/`
   - Files: `book_2026-01-07_*_prompt.txt`

2. **Copy the entire prompt** to your AI

3. **Generate content** - The AI will see explicit requirements:
   - "MUST be exactly 3000-4000 words"
   - "Minimum: 3,000 words (REQUIRED - content will be rejected if shorter)"
   - "Do not stop writing until you reach the minimum word count"

4. **Save the generated content** for validation

### Step 2: Validate Generated Content

After generating content with AI, validate it:

```python
from scripts.generate_book import BookGenerator

generator = BookGenerator()

# For Chapter 1
chapter_1_content = """[paste AI-generated content here]"""

result = generator.generate_chapter(
    chapter_spec=generator.book_structure[0],
    generated_content=chapter_1_content
)
```

**What Happens**:
1. **Pre-validation length check** - Immediate rejection if < 3,000 words
2. **Full validation** - All edge case checks
3. **Critical issue detection** - Flags problems
4. **Rejection or acceptance** - Clear feedback

### Step 3: Handle Rejections

If content is rejected:

1. **Review critical issues**:
   - Length gap (how many words short)
   - Compliance violations
   - Missing required elements

2. **Regenerate with AI**:
   - Use same prompt
   - Emphasize length requirement
   - Ask AI to expand specific sections

3. **Re-validate** until all checks pass

### Step 4: Accept Valid Content

When validation passes:
- ✅ Content saved to `content/published/book/chapters/`
- ✅ Metadata updated
- ✅ Quality tracked
- ✅ Ready for compilation

---

## Chapter-by-Chapter Regeneration

### Chapter 1: Retirement Reality Check
- **Prompt**: `book_2026-01-07_the-hidden-risks-in-your-retir_top-of-funnel_engineer-retiree_7b8a878d_prompt.txt`
- **Expected**: 3,000-4,000 words
- **Current**: 1,329 words (55.7% short)
- **Target**: Expand to 3,000+ words

### Chapter 2: The Tax Leak Draining Your Wealth
- **Expected**: 3,000-4,000 words
- **Current**: 1,414 words (52.9% short)
- **Target**: Expand to 3,000+ words

### Chapter 3: Social Security: The Claiming Strategy Most People Miss
- **Expected**: 3,000-4,000 words
- **Current**: 1,264 words (57.9% short)
- **Target**: Expand to 3,000+ words

### Chapter 4: Protecting Your Legacy: Estate Planning That Works
- **Expected**: 3,000-4,000 words
- **Current**: 1,382 words (53.9% short)
- **Target**: Expand to 3,000+ words

### Chapter 5: Healthcare and Longevity: Planning for the Unknown
- **Expected**: 3,000-4,000 words
- **Current**: 1,514 words (49.5% short)
- **Target**: Expand to 3,000+ words

### Chapter 6: Real Outcomes: From Crisis to Confidence
- **Expected**: 3,000-4,000 words
- **Current**: 1,624 words (45.9% short)
- **Target**: Expand to 3,000+ words

---

## Validation Checklist

Before accepting content, verify:

### P0 - Critical (Must Pass)
- [ ] Length: 3,000-4,000 words
- [ ] Compliance: No banned words/phrases
- [ ] Required Elements: Opening hook, body sections, CTA
- [ ] Structure: Chapter title, sections present

### P1 - High Priority (Should Pass)
- [ ] Structure variation
- [ ] Permission frames: Max 2
- [ ] Signature phrases: Rotated
- [ ] CTAs: Appropriate for funnel stage
- [ ] Story resolution: Concrete outcomes
- [ ] Dialogue: Natural (if used)
- [ ] Numbers: With context

### P2 - Medium Priority (Nice to Have)
- [ ] Citations: For statistics
- [ ] Specificity: Concrete examples
- [ ] No excessive repetition

---

## Tips for AI Generation

### To Meet Length Requirements

1. **Explicitly state length requirement**:
   - "This chapter MUST be 3,000-4,000 words"
   - "Do not stop until you reach at least 3,000 words"

2. **Ask for expansion**:
   - "Expand each section with detailed examples"
   - "Add case studies and real-world scenarios"
   - "Provide specific numbers and calculations"

3. **Request specific additions**:
   - "Add a 'Key Takeaways' section"
   - "Include a 'Quick Start' section"
   - "Add concrete examples for each concept"

### To Pass Validation

1. **Compliance**:
   - Review prompt for banned words
   - Use alternatives from compliance rules

2. **Structure**:
   - Follow required structure from prompt
   - Include all required sections

3. **Quality**:
   - Use specific examples
   - Add concrete numbers with context
   - Vary language and structure

---

## Expected Results

### After Regeneration

- **Total Words**: 18,000-24,000 (up from 8,527)
- **Total Pages**: 72-96 pages (up from 34.1)
- **With Introduction**: 77-101 pages
- **All Chapters**: 3,000-4,000 words each
- **Validation**: 100% pass rate on critical checks

---

## Quick Commands

### Generate Prompt for Specific Chapter
```bash
python scripts/generate_book.py --chapter 1
```

### Validate Existing Content
```bash
python scripts/validate_length.py --content-file content/published/book/chapters/chapter_01_retirement_reality_check.md --expected-length "3000-4000 words"
```

### Check All Chapter Lengths
```bash
python scripts/analyze_book_length.py
```

### Compile Book After Regeneration
```bash
python scripts/compile_book.py --format markdown
```

---

## Troubleshooting

### Content Still Too Short

**Problem**: AI generates < 3,000 words despite requirements

**Solutions**:
1. Emphasize length requirement more strongly
2. Ask AI to expand specific sections
3. Request additional examples or case studies
4. Break into subsections and ask AI to expand each

### Validation Failures

**Problem**: Content fails validation checks

**Solutions**:
1. Review critical issues from validation output
2. Fix compliance violations (replace banned words)
3. Add missing required elements (CTAs, structure)
4. Regenerate with fixes

### Quality Issues

**Problem**: Content passes length but has quality issues

**Solutions**:
1. Review warnings from validation
2. Address high-priority issues
3. Accept medium-priority warnings if acceptable
4. Refine content based on feedback

---

## Next Steps

1. **Generate Chapter 1** with AI using the prompt
2. **Validate** the generated content
3. **Fix** any critical issues
4. **Repeat** for all 6 chapters
5. **Compile** the complete book
6. **Verify** final length (70-90 pages)

---

**Status**: Ready for regeneration  
**Validation**: Active and enforced  
**Expected Outcome**: 18,000-24,000 words (72-96 pages)

