# SureWealth Book Rewrite Project

A stateful, AI-assisted book writing system for creating consistent, conversion-optimized financial education content with integrated quality validation and content indexing.

## 📁 Project Structure

```
surewealth_book_rewrite/
├── docs/                    # All documentation (see docs/MASTER_INDEX.md)
│   ├── analysis/           # Content and system analysis documents
│   ├── guides/             # User guides and how-to documentation
│   ├── summaries/          # System summaries and status reports
│   ├── archive/            # Archived/deprecated documentation
│   └── templates/          # Documentation templates
├── meta_framework/        # Stateful tracking system (YAML-based)
│   ├── language/          # Language patterns, compliance, constraints
│   ├── narratives/        # Stories, allegories, case studies
│   ├── content_quality/  # Quality validation and indexing
│   └── tools_ctas/        # Conversion tools and CTAs
├── content/               # Generated content
│   ├── published/         # Published content (organized by platform/funnel)
│   ├── drafts/            # Draft content
│   ├── prompts/           # AI prompts (separated from content)
│   ├── metadata/          # Content metadata (YAML files)
│   └── index/              # Content index for searchability
├── ai_prompts/            # AI prompt building system
│   ├── prompt_builder.py  # Main prompt generation engine
│   ├── format_prompts/    # Format-specific templates
│   └── system_prompts/    # Base system prompts
├── scripts/               # Automation & tools
│   ├── generate_content_with_quality.py  # Content generation with validation
│   ├── rebuild_content_index.py        # Index maintenance
│   └── compliance_validator.py          # Compliance checking
├── tracking/              # Project management
└── templates/             # Reusable templates
```

## 🎯 Core Concept

This system maintains **stateful consistency** across all book content by tracking:
- **Characters** with complete financial profiles (e.g., John Smith - single father, $100k income)
- **Narrative elements** (allegories, metaphors, case studies, story threads)
- **Language constraints** (tone, vocabulary, signature phrases)
- **Tools & CTAs** (conversion optimization elements)
- **Chapter metadata** (emotional arcs, elements used, conversion points)

## 🚀 Getting Started

### 1. Review Documentation
- Start with **`docs/MASTER_INDEX.md`** for complete documentation navigation
- See **`PROJECT_SETUP_PLAN.md`** for the complete system architecture
- Review **`docs/guides/GETTING_STARTED_WRITING.md`** to begin generating content

### 2. Understand the Meta Framework
The `meta_framework/` directory contains all tracked elements:
- `characters/` - Character profiles with financial situations
- `narratives/` - Allegories, metaphors, case studies, story threads
- `language/` - Tone, vocabulary, and phrase constraints
- `tools_ctas/` - Conversion tools and CTA mapping
- `chapters/` - Chapter-level metadata tracking

### 3. Use Templates
Templates are in `templates/`:
- `character_template.yaml` - Create new characters
- `narrative_template.yaml` - Create new narratives
- `chapter_template.yaml` - Track chapter elements

### 4. Validate Content
After generating content, validate it:
```bash
python scripts/content_validator.py \
  --content-file content/chapters/chapter_01.md \
  --format chapter
```

See `docs/guides/CONTENT_VALIDATION_GUIDE.md` for complete validation guide.
- `ingestion_template.md` - Process new concepts

## 📚 Key Documents

### Start Here
- **`docs/MASTER_INDEX.md`** - **Master documentation index** (complete navigation)
- **`docs/guides/GETTING_STARTED_WRITING.md`** - Quick start guide for content generation
- **`docs/guides/QUICK_REFERENCE.md`** - Common workflows and quick reference

### Core Reference Documents
- **`docs/SRP_SureWealthBook.md`** - System Reference Document (core philosophy)
- **`docs/book_emotional_journey.md`** - Emotional arc and conversion map
- **`docs/persuasion_machine.md`** - Conversion optimization framework
- **`docs/storytelling_guidelines.md`** - Storytelling rules
- **`docs/writer_standards.md`** - Writing standards and voice constraints
- **`docs/GoogleContentGuidelines.md`** - SEO and content quality guidelines

### System Documentation
- **`docs/guides/CONTENT_GENERATION_SYSTEM.md`** - Complete content generation guide
- **`docs/guides/CONTENT_VALIDATION_GUIDE.md`** - Content quality validation
- **`docs/guides/COMPLIANCE_ENFORCEMENT_GUIDE.md`** - Compliance system guide
- **`docs/METADATA_AND_INDEX_INTEGRATION.md`** - Content indexing system
- **`docs/FINAL_INTEGRATION_STATUS.md`** - Latest integration status

### Analysis Documents
- **`docs/analysis/ANALYSIS_INDEX.md`** - Analysis documents index
- **`docs/analysis/CONTENT_QUALITY_ANALYSIS.md`** - Content quality analysis
- **`docs/analysis/MARKDOWN_EXPORT_CONVERSION_ANALYSIS.md`** - Conversion pattern analysis
- **`docs/analysis/PATTERN_INTEGRATION_VALIDATION_REPORT.md`** - Pattern integration report

### System Summaries
- **`docs/summaries/COMPREHENSIVE_SYSTEM_SUMMARY.md`** - Complete system overview
- **`docs/summaries/IMPLEMENTATION_COMPLETE.md`** - Implementation status
- **`docs/summaries/TRANSCRIPT_INTEGRATION_COMPLETE.md`** - Transcript integration status

## 🔄 Content Generation Workflow

1. **Generate Content** - Use `scripts/generate_content_with_quality.py`:
   ```bash
   python scripts/generate_content_with_quality.py
   ```
   - Automatically creates metadata
   - Validates against lessons learned
   - Updates content index
   - Organizes files properly

2. **Validate Content** - Content is automatically validated for:
   - Compliance rules
   - Quality standards (permission frames, CTAs, signature phrases)
   - Structure variation
   - Funnel appropriateness

3. **Track Content** - All content is indexed and searchable by:
   - Funnel stage
   - Persona
   - Topic
   - Platform
   - Tags

4. **Maintain Index** - Rebuild index if needed:
   ```bash
   python scripts/rebuild_content_index.py
   ```

## 🧩 Meta Framework Components

### Character Tracking
Characters are tracked with complete financial profiles. Example: John Smith (single father, $100k income) can be referenced consistently across chapters.

### Story Vault System
Comprehensive narrative tracking using `story_vault_schema.yaml`:
- **Allegories** - Metaphorical stories (e.g., "The Leaky Bucket")
- **Composite Case Studies** - Real-world scenarios (e.g., "Mark the Engineer")
- **Foil Stories** - Contrast narratives
- **Legacy Parables** - Multi-generational stories

Each story includes:
- Funnel mapping (top/mid/conversion/post)
- Voice of Customer (VOC) phrases
- Distribution targets (book, email, webinar, etc.)
- Asset hooks (calculators, tools, webinars)
- Compliance flags
- Linguistic patterns

### Language Constraints
Tone, vocabulary, and phrases are locked in to ensure consistent voice.

### Tool/CTA Mapping
Financial concepts are mapped to appropriate tools and CTAs for conversion.

## 🆕 Recent Updates (2025-12-27)

### Content Quality System
- ✅ Lessons learned integration (prevents repetition)
- ✅ Content validation system
- ✅ Metadata and indexing system
- ✅ Quality checklist enforcement

### New Features
- **Content Index**: Searchable index by funnel, persona, topic, tags
- **Quality Validation**: Automatic validation against lessons learned
- **Metadata System**: Automatic metadata creation for all content
- **Compliance Enforcement**: Integrated compliance checking

### Integration Complete
- ✅ All patterns integrated (question frameworks, permission frames, presuppositions)
- ✅ Content quality system integrated
- ✅ Metadata and indexing integrated
- ✅ YAML syntax errors fixed

## 📝 Next Steps

1. Review `docs/MASTER_INDEX.md` for complete documentation
2. Start generating content: `docs/guides/GETTING_STARTED_WRITING.md`
3. Explore quality system: `docs/guides/CONTENT_VALIDATION_GUIDE.md`
4. Check compliance: `docs/guides/COMPLIANCE_ENFORCEMENT_GUIDE.md`

---

*This system ensures every piece of content is consistent, trackable, and optimized for conversion while maintaining the SureWealth brand voice.*

