# Content Directory Structure Proposal

## Current Issues

1. **Mixed file types**: Prompts and content in same folder
2. **No metadata**: Can't search by funnel stage, persona, topic
3. **No versioning**: No way to track revisions
4. **No categorization**: All social posts together, no sub-folders
5. **No tagging**: Can't find content by tags

## Proposed Structure

```
content/
  published/
    social/
      facebook/
        top_funnel/
          [YYYY-MM-DD]_[topic-slug]_[persona]_[id].md
        mid_funnel/
        lower_funnel/
      linkedin/
        top_funnel/
        mid_funnel/
        lower_funnel/
    blog/
      [YYYY-MM-DD]_[topic-slug]_[funnel]_[persona]_[id].md
    email/
      nurture/
      campaigns/
  drafts/
    [same structure as published]
  prompts/
    social/
      facebook/
        [topic]_[funnel]_[persona]_prompt.txt
    blog/
    email/
  metadata/
    [content-id].yaml
  index/
    content_index.yaml  # Master index of all content
    by_funnel.yaml
    by_persona.yaml
    by_topic.yaml
```

## Metadata File Structure

Each piece of content gets a metadata YAML file:

```yaml
content_id: facebook_2025-12-27_tax-leak_engineer-retiree_001
title: "The Hidden Tax Leak Draining Your Retirement"
format: social_post
platform: facebook
funnel_stage: mid_funnel
user_intent: researching
persona: engineer_retiree
topic: tax_planning
tags:
  - taxes
  - retirement
  - 401k
  - tax_leak
emotional_goal: curiosity
narrative_used: ALLEGORY_LEAKY_BUCKET
signature_phrases:
  - "Hope is not a strategy"
  - "The cost of waiting is usually invisible… until it isn't"
cta_type: soft_cta
cta_count: 1
permission_frames_used: 2
word_count: 1354
created_date: 2025-12-27
status: published
performance:
  views: null
  engagement: null
  conversions: null
related_content:
  - content_id: facebook_2025-12-27_401k-gap_faith-family_002
  - content_id: blog_2025-12-20_tax-strategies_mid-funnel_003
```

## Content Index System

Master index file tracks all content:

```yaml
content_index:
  total_pieces: 150
  by_funnel:
    top_funnel: 60
    mid_funnel: 70
    lower_funnel: 20
  by_persona:
    engineer_retiree: 50
    faith_family_builder: 50
    widow_caregiver: 50
  by_topic:
    tax_planning: 30
    retirement_income: 40
    market_volatility: 30
    social_security: 20
    other: 30
  
  recent_content:
    - content_id: facebook_2025-12-27_tax-leak_engineer-retiree_001
      title: "The Hidden Tax Leak"
      funnel: mid_funnel
      persona: engineer_retiree
      created: 2025-12-27
```

## Implementation Steps

1. **Create new directory structure**
2. **Move existing content** to new structure
3. **Create metadata files** for existing content
4. **Build content index** system
5. **Update generation scripts** to use new structure
6. **Create search/filter tools** for content discovery

## Benefits

- **Searchable**: Find content by funnel, persona, topic, tags
- **Organized**: Clear separation of prompts, drafts, published
- **Trackable**: Metadata enables performance tracking
- **Scalable**: Structure supports thousands of pieces
- **Maintainable**: Easy to find and update content

