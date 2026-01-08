# Chapter Regeneration Workflow

**Date**: 2025-12-28  
**Status**: ✅ Prompts Generated, Ready for AI Content Generation

---

## Current Status

✅ **All 6 Chapter Prompts Generated**  
✅ **Enhanced Length Requirements in All Prompts**  
✅ **Validation System Active**  
✅ **Ready for AI Content Generation**

---

## Regeneration Process

### Step 1: Generate Content with AI

For each chapter, you'll need to:

1. **Open the prompt file** from `content/prompts/book/`
2. **Copy the entire prompt** to your AI (ChatGPT/Claude)
3. **Generate content** - The AI will see explicit requirements:
   - "MUST be exactly 3000-4000 words"
   - "Minimum: 3,000 words (REQUIRED - content will be rejected if shorter)"
   - Clear instructions to expand sections

4. **Save the generated content** to a file

### Step 2: Validate and Save Content

Once you have AI-generated content, validate it:

**Option A: Using regenerate_chapter.py (Recommended)**
```bash
python scripts/regenerate_chapter.py --chapter 1 --content-file path/to/generated_content.md
```

**Option B: Using generate_book.py**
```python
from scripts.generate_book import BookGenerator

generator = BookGenerator()
content = """[paste AI-generated content here]"""

result = generator.generate_chapter(
    chapter_spec=generator.book_structure[0],  # Chapter 1
    generated_content=content
)
```

### Step 3: Handle Validation Results

**If Content is Rejected**:
- Review critical issues (length, compliance, required elements)
- Regenerate with AI, emphasizing fixes needed
- Re-validate until all checks pass

**If Content is Accepted**:
- Content saved to `content/published/book/chapters/`
- Metadata updated
- Quality tracked
- Ready for next chapter

---

## Chapter-by-Chapter Guide

### Chapter 1: Retirement Reality Check
- **Prompt File**: `content/prompts/book/book_2026-01-07_the-hidden-risks-in-your-retir_top-of-funnel_engineer-retiree_7b8a878d_prompt.txt`
- **Expected**: 3,000-4,000 words
- **Current**: 1,329 words (needs 1,671+ more words)
- **Narrative**: ALLEGORY_HOUSE_OF_CARDS
- **Persona**: engineer_retiree
- **Emotional Goal**: fear

**After generating with AI**:
```bash
python scripts/regenerate_chapter.py --chapter 1 --content-file chapter_01_generated.md
```

### Chapter 2: The Tax Leak Draining Your Wealth
- **Expected**: 3,000-4,000 words
- **Current**: 1,414 words (needs 1,586+ more words)
- **Narrative**: ALLEGORY_LEAKY_BUCKET
- **Persona**: engineer_retiree
- **Emotional Goal**: concern

### Chapter 3: Social Security: The Claiming Strategy Most People Miss
- **Expected**: 3,000-4,000 words
- **Current**: 1,264 words (needs 1,736+ more words)
- **Narrative**: Case Study
- **Persona**: faith_family_builder
- **Emotional Goal**: hope

### Chapter 4: Protecting Your Legacy: Estate Planning That Works
- **Expected**: 3,000-4,000 words
- **Current**: 1,382 words (needs 1,618+ more words)
- **Narrative**: Case Study
- **Persona**: widow_caregiver
- **Emotional Goal**: confidence

### Chapter 5: Healthcare and Longevity: Planning for the Unknown
- **Expected**: 3,000-4,000 words
- **Current**: 1,514 words (needs 1,486+ more words)
- **Narrative**: Problem-first structure
- **Persona**: engineer_retiree
- **Emotional Goal**: confidence

### Chapter 6: Real Outcomes: From Crisis to Confidence
- **Expected**: 3,000-4,000 words
- **Current**: 1,624 words (needs 1,376+ more words)
- **Narrative**: Case Study
- **Persona**: engineer_retiree
- **Emotional Goal**: action

---

## Validation Checklist

Before accepting, verify:

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

---

## Tips for AI Generation

### To Meet Length Requirements

1. **Emphasize length explicitly**:
   - "This chapter MUST be 3,000-4,000 words"
   - "Do not stop until you reach at least 3,000 words"

2. **Request specific expansions**:
   - "Expand each section with detailed examples"
   - "Add case studies and real-world scenarios"
   - "Provide specific numbers and calculations"
   - "Include a 'Key Takeaways' section"
   - "Add a 'Quick Start' section"

3. **If AI stops early**:
   - "Continue writing - you're at X words, need 3,000 minimum"
   - "Expand the [section name] section with more detail"
   - "Add more examples to illustrate the concept"

---

## Expected Results

### After Regeneration

- **Total Words**: 18,000-24,000 (up from 8,527)
- **Total Pages**: 72-96 pages (up from 34.1)
- **With Introduction**: 77-101 pages
- **All Chapters**: 3,000-4,000 words each
- **Validation**: 100% pass rate on critical checks

---

## Quick Reference

### Validate Single Chapter
```bash
python scripts/regenerate_chapter.py --chapter 1 --content-file chapter_01.md
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

**Status**: Ready for AI content generation  
**Next Step**: Generate Chapter 1 content with AI using the prompt

