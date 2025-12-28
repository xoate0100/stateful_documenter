# 🚀 Getting Started Writing - Quick Start Guide

## Goal: Get to Writing Content Fast

This guide helps you start generating content immediately without blockers.

---

## Step 1: Generate Your First Content

### Option A: Social Media Post

```bash
python ai_prompts/prompt_builder.py \
  --format social_post \
  --topic tax_planning \
  --persona engineer_retiree \
  --narratives ALLEGORY_LEAKY_BUCKET \
  --tools lifetime_tax_calculator \
  --length 280 \
  --emotional-goal curiosity
```

**Output:** A prompt you can paste into ChatGPT/Claude that includes all constraints.

### Option B: Email

```bash
python ai_prompts/prompt_builder.py \
  --format email \
  --topic retirement_planning \
  --persona faith_family_builder \
  --narratives ALLEGORY_HOUSE_OF_CARDS \
  --length 300
```

### Option C: Book Chapter

```bash
python ai_prompts/prompt_builder.py \
  --format chapter \
  --topic tax_planning \
  --persona engineer_retiree \
  --narratives ALLEGORY_LEAKY_BUCKET \
  --tools lifetime_tax_calculator \
  --length 3000
```

---

## Step 2: Use the Prompt

1. Copy the generated prompt
2. Paste into ChatGPT/Claude
3. AI generates content following all constraints
4. Review and refine

---

## Step 3: Adapt Existing Content

If you have a chapter and want to make it a social post:

```bash
python content_adapters/length_adapters.py \
  --input content/chapters/chapter_02.md \
  --target-length 280 \
  --format social_post \
  --direction condense \
  --output content/social/tax_post.md
```

---

## Step 4: Generate Landing Page Brief

When you need a landing page:

```bash
python marketing_automation/landing_pages/generate_site_brief.py \
  --topic tax_planning \
  --tool lifetime_tax_calculator \
  --persona engineer_retiree \
  --narratives ALLEGORY_LEAKY_BUCKET \
  --output site_briefs/tax_landing.json
```

Then use with your white-paper-sites project.

---

## Step 5: Track Top Performers (Manual)

When you have content that performs well, manually enter it:

1. Copy the content
2. Use `content_examples/manual_entry_template.md`
3. Fill in performance data
4. Save to appropriate folder
5. AI will reference it in future generations

**Example locations:**
- `content_examples/social_posts/high_performing_tax_post.yaml`
- `content_examples/email_subjects/converting_subject_001.yaml`
- `content_examples/landing_pages/tax_calculator_landing.yaml`

---

## Common Workflows

### Generate Social Post from Chapter

1. Generate chapter prompt → get chapter content
2. Use `length_adapters.py` to condense to social post length
3. Add QR code if needed: `python marketing_automation/qr_generator/generate_qr.py --tool lifetime_tax_calculator --chapter 2`

### Generate Email Sequence

1. Generate email prompt for each email in sequence
2. Use same topic/persona, vary emotional goals
3. Link tools/CTAs appropriately
4. Track in `marketing_automation/email_sequences/email_automation.yaml`

### Generate Landing Page

1. Generate site brief using `generate_site_brief.py`
2. Review and refine brief
3. Use with white-paper-sites project
4. Track performance manually when you have data

---

## What You DON'T Need to Do

- ❌ Set up Google Analytics integration
- ❌ Build complex automation
- ❌ Connect to external APIs
- ❌ Over-engineer the system

**Just generate content, track manually what works, and iterate.**

---

## Quick Reference

### Available Formats
- `social_post` - LinkedIn, Twitter, Facebook, Instagram
- `email` - Nurture, conversion, follow-up
- `blog` - Blog posts (500-2000 words)
- `chapter` - Book chapters (2000-5000 words)
- `landing_page` - Site brief generation

### Available Personas
- `engineer_retiree` - Data-driven, analytical
- `faith_family_builder` - Values-driven, legacy-focused
- `widow_caregiver` - Cautious, seeking guidance

### Available Narratives
- `ALLEGORY_LEAKY_BUCKET` - Tax drag metaphor
- `ALLEGORY_HOUSE_OF_CARDS` - Market dependency
- `ALLEGORY_PRESSURE_RELIEF_VALVE` - Emergency access (NEW)
- `ALLEGORY_TWO_SIDES_OF_COIN` - Death benefit/cash value (NEW)
- `CASE_STUDY_MARK_ENGINEER` - Complexity to clarity

### Available Metaphors (NEW - From Transcript Analysis)
- `SAVINGS_ACCOUNT_METAPHOR` - Policy loans as savings account
- `WATERFALL_CASCADE_METAPHOR` - Debt paydown strategy
- `SAILBOAT_METAPHOR` - Policy structure (hull, mast, sail)
- `WAREHOUSE_OF_WEALTH_METAPHOR` - Policy as warehouse
- `LEFT_POCKET_RIGHT_POCKET_METAPHOR` - Tax efficiency
- `HICCUP_SPEED_BUMP_METAPHOR` - Temporary setbacks
- `PRESSURE_RELIEF_VALVE_METAPHOR` - Emergency access

### Available Tools
- `lifetime_tax_calculator` - Tax impact calculator
- `retirement_risk_assessment` - Risk assessment
- `social_security_optimizer` - SS claiming optimizer

---

## Next Steps

1. **Generate your first piece** using `prompt_builder.py`
2. **Refine the output** in your AI chat
3. **Save top performers** manually in `content_examples/`
4. **Iterate and improve**

**Focus on writing great content. The system handles consistency and constraints.**

---

## New Features (Transcript Integration)

The system now includes **proven patterns from 17 client service transcripts**:

### Language Patterns (Automatically Applied)
- **Normalization** - Reduces shame/anxiety ("You're not alone...")
- **Reframing** - Crisis to opportunity ("This is what it's designed for...")
- **Mathematical Proof** - Objective truth through numbers
- **Empowerment** - Control and flexibility language
- **Future Visioning** - Hope and forward momentum
- **Celebration** - Progress and achievement language
- **Confirmation** - Ensures understanding

### Friction Prevention
- Proactive clarification sections
- Information chunking (max 2 concepts per section)
- Visual breaks after complex concepts
- Summary sections for processing

### Emotional State Management
- Systematic transitions (fear→calm, confusion→clarity, etc.)
- State-appropriate language patterns
- Psychological principles applied automatically

**These patterns are automatically included in all generated content.**

---

*You're ready to start writing! 🎉*

