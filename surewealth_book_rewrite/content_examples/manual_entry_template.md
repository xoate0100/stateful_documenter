# Manual Content Examples Entry Template

## Purpose
Manually enter top-performing content examples here. This helps the AI learn from your best-performing content without requiring complex analytics integration.

## How to Use
1. Copy a high-performing piece of content
2. Fill in the template below
3. Save in the appropriate folder (social_posts/, email_subjects/, landing_pages/, ctas/)
4. The AI will reference these when generating new content

---

## Entry Template

```yaml
content_example:
  id: EXAMPLE_ID
  type: social_post | email_subject | landing_page | cta | blog_post
  platform: linkedin | twitter | facebook | email | website
  
  # Performance Data (enter manually)
  performance:
    date_added: YYYY-MM-DD
    engagement_rate: "X.X%"  # Optional
    conversion_rate: "X.X%"  # Optional
    open_rate: "XX%"  # For emails
    click_rate: "XX%"  # For emails
    notes: "Any additional context about why this performed well"
  
  # Content
  content:
    headline: "The actual headline/subject line"
    body: |
      The actual content text
      (preserve formatting)
    cta: "The CTA text used"
  
  # Context
  context:
    topic: tax_planning | retirement_planning | etc.
    persona: engineer_retiree | faith_family_builder | widow_caregiver
    funnel_stage: top_of_funnel | mid_funnel | conversion
    emotional_trigger: curiosity | urgency | empathy | hope
    narrative_used: ALLEGORY_LEAKY_BUCKET | etc.  # If applicable
    character_referenced: JOHN_SMITH | etc.  # If applicable
    tool_linked: lifetime_tax_calculator | etc.  # If applicable
  
  # Why It Worked (your analysis)
  success_factors:
    - "Factor 1 - e.g., strong emotional hook"
    - "Factor 2 - e.g., specific statistic"
    - "Factor 3 - e.g., clear CTA"
```

---

## Example Entry

```yaml
content_example:
  id: SOCIAL_TAX_LEAKY_BUCKET_001
  type: social_post
  platform: linkedin
  
  performance:
    date_added: 2024-01-15
    engagement_rate: "4.2%"
    conversion_rate: "2.1%"
    notes: "High engagement, many comments asking about the calculator"
  
  content:
    headline: ""
    body: |
      What if the problem isn't how much you're saving — but what's quietly draining it?
      
      Most people never see the leak. They focus on adding more water to the bucket, never noticing the crack at the bottom.
      
      But fixing the leak matters more than pouring faster.
      
      See where your money may be leaking →
    cta: "See where your money may be leaking →"
  
  context:
    topic: tax_planning
    persona: engineer_retiree
    funnel_stage: mid_funnel
    emotional_trigger: curiosity
    narrative_used: ALLEGORY_LEAKY_BUCKET
    tool_linked: lifetime_tax_calculator
  
  success_factors:
    - "Strong opening question creates curiosity gap"
    - "Uses leaky bucket metaphor (familiar from book)"
    - "Clear, actionable CTA"
    - "Links to relevant calculator"
```

---

## File Organization

- `social_posts/` - Social media examples
- `email_subjects/` - Email subject line examples  
- `landing_pages/` - Landing page copy examples
- `ctas/` - CTA examples
- `blog_posts/` - Blog post examples

Name files: `{type}_{topic}_{date}.yaml` or `{type}_{id}.yaml`

