# Landing Page Integration Guide

## Overview

This system integrates with the **white-paper-sites** project (https://github.com/xoate0100/white-paper-sites) to generate landing pages from book content.

## How It Works

1. **Generate Site Brief** - Use `generate_site_brief.py` to create a site brief from framework elements
2. **Use with white-paper-sites** - The site brief follows `SITE_BRIEF_TEMPLATE.md` and `site_brief.schema.json`
3. **Manual Refinement** - Review and refine the brief before using it

## Quick Start

### Generate a Landing Page Brief

```bash
python marketing_automation/landing_pages/generate_site_brief.py \
  --topic tax_planning \
  --tool lifetime_tax_calculator \
  --persona engineer_retiree \
  --narratives ALLEGORY_LEAKY_BUCKET \
  --output site_briefs/tax_calculator_landing.json
```

**Note:** The script references `docs/templates/SITE_BRIEF_TEMPLATE.md` and `docs/schemas/site_brief.schema.json`

### What Gets Generated

The script pulls from your framework:
- **Persona data** - Demographics, psychographics, emotional drivers
- **Narrative elements** - Stories, metaphors, emotional arcs
- **Tool information** - Calculator details, CTAs, integration points
- **Language constraints** - Tone, vocabulary, signature phrases

### Using with white-paper-sites

1. Generate the site brief (as above)
2. Copy the JSON file to your white-paper-sites project
3. Use it according to that project's instructions
4. The brief follows the schema, so it should work directly

## Manual Entry for Top-Performing Content

Rather than trying to automate analytics integration, you can manually enter top-performing content examples:

### Entry Template

See `content_examples/manual_entry_template.md` for the full template.

### Quick Entry

```yaml
content_example:
  id: LANDING_TAX_001
  type: landing_page
  performance:
    conversion_rate: "12%"
    notes: "High conversion, calculator completion was key"
  content:
    headline: "What's Your Lifetime Tax Impact?"
    # ... rest of content
  success_factors:
    - "Clear value proposition"
    - "Calculator provided immediate value"
```

### Where to Save

- `content_examples/landing_pages/` - Landing page examples
- `content_examples/social_posts/` - Social media examples
- `content_examples/email_subjects/` - Email examples
- `content_examples/ctas/` - CTA examples

## Integration Points

### Framework → Site Brief

The generator pulls:
- Persona profiles → Target audience section
- Story vault narratives → Story framework section
- Tool/calculator info → CTA strategy, calculator integration
- Language constraints → Copy tone section

### Site Brief → Landing Page

The white-paper-sites project uses the brief to:
- Generate page structure
- Create content modules
- Set up calculator integration
- Configure CTAs and conversion points

## Workflow

1. **Identify Need** - "I need a landing page for the tax calculator"
2. **Generate Brief** - Run `generate_site_brief.py` with relevant parameters
3. **Review Brief** - Check that framework elements are correctly pulled
4. **Refine Manually** - Add any specific requirements not in framework
5. **Use with white-paper-sites** - Generate the actual landing page
6. **Track Performance** - Manually enter top performers in `content_examples/`

## Keeping It Simple

**What We Do:**
- ✅ Generate site briefs from framework
- ✅ Pull persona, narrative, tool data automatically
- ✅ Follow the schema for compatibility
- ✅ Manual entry for performance data

**What We Don't Do:**
- ❌ Auto-connect to Google Analytics
- ❌ Auto-pull performance metrics
- ❌ Over-automate the process
- ❌ Try to build the landing page here

## Focus: Content Generation

The main goal is to **generate hyper-optimized, consistent content** quickly. The landing page brief generation helps by:
- Pulling all relevant framework elements
- Maintaining consistency with book content
- Ensuring persona alignment
- Following proven templates

Then you use the white-paper-sites project to actually build the page.

---

*This keeps boundaries clear: content generation here, page building there, manual tracking for performance.*

