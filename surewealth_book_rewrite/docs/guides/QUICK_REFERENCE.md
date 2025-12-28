# Quick Reference Guide

## 🚀 Common Workflows

### Creating a New Character

1. **Copy template:**
   ```bash
   cp templates/character_template.yaml meta_framework/characters/JOHN_SMITH.yaml
   ```

2. **Fill in character details:**
   - Demographics (age, occupation, marital status)
   - Financial profile (income, savings, accounts)
   - Emotional profile (fears, aspirations, awareness level)

3. **Register in index:**
   - Add entry to `meta_framework/characters/characters_index.yaml`
   - Update `meta_framework/index.yaml` cross-references

### Creating a New Narrative Element

1. **Choose type:** allegory, metaphor, case_study, or story_thread

2. **Copy appropriate template:**
   ```bash
   cp templates/narrative_template.yaml meta_framework/narratives/allegories/NEW_ALLEGORY.yaml
   ```

3. **Fill in narrative details:**
   - Narrative structure (setup, conflict, realization, resolution)
   - Emotional journey
   - Linguistic hooks
   - CTAs and tool integration

4. **Register in appropriate index:**
   - `allegories_index.yaml`, `metaphors_index.yaml`, etc.

### Writing a Chapter

1. **Create chapter metadata:**
   ```bash
   cp templates/chapter_template.yaml meta_framework/chapters/chapter_01_retirement_reality_check.yaml
   ```

2. **Plan chapter elements:**
   - Select narratives to use (allegories, metaphors, case studies)
   - Choose characters to reference
   - Map tools/CTAs using `toolhook_map.yaml`
   - Define emotional arc

3. **Generate content with AI:**
   - Reference framework constraints
   - Use tracked elements (character IDs, narrative IDs)
   - Follow language constraints from `language/` directory

4. **Update tracking:**
   - Add chapter to `chapters_index.yaml`
   - Update character `references` and `narrative_arc`
   - Update narrative `usage_tracking`

### Ingesting a New Concept

1. **Use ingestion template:**
   - Fill out `templates/ingestion_template.md`
   - Or use `scripts/ingest.py` (when enhanced)

2. **Extract elements:**
   - Identify if new character needed
   - Identify if new narrative needed
   - Map to existing tools/CTAs or create new ones

3. **Create framework entries:**
   - Create character/narrative files
   - Update indexes
   - Update cross-references

## 📍 File Locations

### Where to Find Things

| What You Need | Location |
|---------------|----------|
| Character profiles | `meta_framework/characters/` |
| Allegories | `meta_framework/narratives/allegories/` |
| Metaphors | `meta_framework/narratives/metaphors/` |
| Case studies | `meta_framework/narratives/case_studies/` |
| Story threads | `meta_framework/narratives/story_threads/` |
| Tone rules | `meta_framework/language/tone_guide.yaml` |
| Banned words | `meta_framework/language/vocabulary.yaml` |
| Signature phrases | `meta_framework/language/signature_phrases.yaml` |
| Tool/CTA mapping | `meta_framework/tools_ctas/toolhook_map.yaml` |
| Chapter metadata | `meta_framework/chapters/` |
| Master index | `meta_framework/index.yaml` |

## 🔍 Finding References

### Check Character Usage
```bash
# Search for character references
grep -r "JOHN_SMITH" meta_framework/chapters/
```

### Check Narrative Usage
```bash
# Search for narrative references
grep -r "ALLEGORY_LEAKY_BUCKET" meta_framework/chapters/
```

### Validate Framework
```bash
python scripts/validate.py --framework-dir meta_framework/
```

## 📝 Naming Conventions

- **Character IDs:** `UPPERCASE_WITH_UNDERSCORES` (e.g., `JOHN_SMITH`)
- **Narrative IDs:** `TYPE_DESCRIPTIVE_NAME` (e.g., `ALLEGORY_LEAKY_BUCKET`)
- **Chapter files:** `chapter_XX_title.yaml` (e.g., `chapter_01_retirement_reality_check.yaml`)

## 🎯 AI Prompt Template

When generating content, include framework constraints:

```
You are writing for the SureWealth Book. Follow these constraints:

CHARACTERS: Reference [CHARACTER_ID] with their established profile:
- Name: [name]
- Situation: [financial situation]
- Previous mentions: [chapters where referenced]

NARRATIVES: Use [NARRATIVE_ID] - [brief description]

LANGUAGE:
- Tone: [from tone_guide.yaml]
- Use signature phrases: [from signature_phrases.yaml]
- Avoid: [from vocabulary.yaml banned words]

TOOLS/CTAS: For [concept], use [tool] with CTA: "[cta_copy]"

Generate [content type] that...
```

## ✅ Checklist Before Finalizing Chapter

- [ ] All character references use correct IDs
- [ ] All narrative elements are from framework
- [ ] Language follows tone guide
- [ ] No banned words/phrases used
- [ ] CTAs match toolhook_map
- [ ] Chapter metadata file updated
- [ ] Character/narrative usage tracking updated
- [ ] Cross-references in index.yaml updated

---

*Keep this guide handy while writing!*

