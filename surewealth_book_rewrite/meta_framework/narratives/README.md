# Story Vault System

## Overview

The Story Vault is a comprehensive narrative tracking system that ensures consistent, conversion-optimized storytelling across all content channels.

## Schema

All narrative entries follow the `story_vault_schema.yaml` format. See the schema file for complete field definitions.

## Entry Types

- **allegory** - Metaphorical stories that illustrate concepts (e.g., "The Leaky Bucket")
- **composite_case_study** - Real-world inspired scenarios (e.g., "Mark the Engineer")
- **foil_story** - Contrast stories showing what not to do
- **legacy_parable** - Multi-generational or legacy-focused narratives

## Key Fields

### Funnel Mapping
- `funnel_stage`: top_of_funnel | mid_funnel | conversion | post_conversion
- `user_intent_profile`: browsing | researching | comparing | ready_to_act

### Voice of Customer (VOC)
- `voc_phrases.pain_language` - Actual customer language about problems
- `voc_phrases.aspiration_language` - Customer language about goals
- `voc_phrases.decision_triggers` - Language when ready to act

### Distribution Targets
Stories can be used across multiple channels:
- book_chapter
- email_nurture
- webinar_slide
- lead_magnet_teaser
- SMS_prompt
- tool_result_page

### Asset Hooks
Link stories to conversion tools:
- calculators
- interactive_tools
- downloadable_assets
- webinar_integration

## Usage

1. **Select appropriate story** based on:
   - Target persona
   - Funnel stage
   - Awareness level
   - User intent

2. **Reference story elements**:
   - Use narrative structure (setup, conflict, realization, resolution)
   - Incorporate VOC phrases naturally
   - Link to appropriate tools via asset_hooks
   - Use signature phrases for consistency

3. **Track usage**:
   - Update `usage_tracking.used_in_chapters`
   - Update `usage_tracking.associated_characters`
   - Update `usage_tracking.last_used`

## Index Files

- `allegories/allegories_index.yaml` - Allegory registry
- `case_studies/case_studies_index.yaml` - Case study registry
- `metaphors/metaphors_index.yaml` - Metaphor registry
- `story_threads/threads_index.yaml` - Story thread registry

## Creating New Stories

1. Copy `templates/narrative_template.yaml`
2. Fill in all fields following the schema
3. Register in appropriate index file
4. Update master index (`meta_framework/index.yaml`)

---

*All stories are designed to be atomic, reusable, and conversion-optimized.*

