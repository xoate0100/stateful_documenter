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
   ```python
   from scripts.generate_content_with_quality import generate_content, save_and_validate_content
   
   # Generate prompt and metadata
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
   
   # After AI generates content, validate it
   validation = save_and_validate_content(
       content_id=result['content_id'],
       content=generated_content,
       chapter_num=5
   )
   ```
   - Pre-generation validation (narratives, characters)
   - Automatic metadata creation
   - Content index updates
   - Quality checkpoint after every chapter

2. **Validation Systems** - Content is automatically validated for:
   - **Narrative Usage**: Only framework narratives allowed
   - **Character Consistency**: All attributes locked, controlled evolution
   - **CTA Appropriateness**: Funnel stage matching with auto-fix
   - **Emotional Arc**: Smooth transitions, sub-state tracking
   - **Chapter References**: Strict validation of all references
   - **Signature Phrase Rotation**: 3-chapter minimum distance
   - **Permission Frame Limits**: Max 2 per chapter, variety required
   - **Structure Variation**: 10-structure library with tracking
   - **Compliance Rules**: All compliance checks

3. **Quality Tracking** - Automatic quality checkpoints:
   - Runs after every chapter
   - Tracks 8+ metrics (compliance, character consistency, narrative adherence, CTA appropriateness, emotional arc, structure variation, signature phrases, technical accuracy)
   - 90% threshold enforcement
   - Hierarchical reporting with detailed metrics
   - Editor tracker flags issues for review

4. **Track Content** - All content is indexed and searchable by:
   - Funnel stage
   - Persona
   - Topic
   - Platform
   - Tags
   - Chapter number
   - Emotional state

5. **Maintain Systems** - Rebuild if needed:
   ```bash
   python scripts/rebuild_content_index.py
   python scripts/book_quality_tracker.py  # View quality statistics
   ```

## 🧩 Meta Framework Components

### Character Tracking
Characters are tracked with complete financial profiles and state management:
- **State Locking**: All attributes locked by default (name, income, situation, age)
- **Usage Tracking**: Chapters where character appears, last reference, total count
- **Controlled Evolution**: Attributes can evolve with justification and tracking
- **Additional Attributes**: New attributes can be added as story requires
- **Validation**: Character references validated against state on every use
- **Contextual Summaries**: Natural, human-like character references in prompts

Example: John Smith (single father, $100k income) tracked across all chapters with consistency validation.

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

## 🆕 Recent Updates (2025-12-28)

### Book Generation Progress
- ✅ **Chapter 1**: Retirement Reality Check (98.1% quality)
- ✅ **Chapter 2**: The Tax Leak Draining Your Wealth (98.1% quality)
- ✅ **Chapter 3**: Social Security: The Claiming Strategy Most People Miss (98.1% quality)
- ✅ **Chapter 4**: Protecting Your Legacy: Estate Planning That Works (98.1% quality)
- ✅ **Chapter 5**: Healthcare and Longevity: Planning for the Unknown (98.1% quality)
- ✅ **Chapter 6**: Real Outcomes: From Crisis to Confidence (98.1% quality)
- ✅ **BOOK COMPLETE** - All 6 chapters generated and validated

### Quality System Performance
- **Average Quality Score**: 98.1% across all chapters
- **Compliance Rate**: 100%
- **Validation Systems**: Fully operational
- **Lessons Learned**: Active and updating

## 🆕 Recent Updates (2025-12-27)

### Complete Validation & Quality System
- ✅ **Book-Level Validation**: Comprehensive validation system with 8+ checks
- ✅ **Character State Tracking**: Full character consistency tracking with controlled evolution
- ✅ **Narrative Constraint System**: AI-assisted narrative creation with approval workflow
- ✅ **CTA Funnel Validation**: Automatic CTA appropriateness checking with auto-fix
- ✅ **Emotional Arc Tracking**: Sub-state tracking with smooth transition enforcement
- ✅ **Cross-Chapter References**: Strict validation of all chapter references
- ✅ **Quality Checkpoints**: Automatic quality tracking after every chapter
- ✅ **Editor Tracker**: Issue flagging with file, line, scenario details
- ✅ **Auto-Fix System**: Automatic correction of fixable issues (CTAs, etc.)

### New Validation Systems
- **Pre-Generation Validation**: Narrative IDs, character states, framework elements
- **Post-Generation Validation**: All 8+ validation checks (narratives, characters, CTAs, emotional arc, references, signature phrases, permission frames)
- **Quality Checkpoints**: Run after every chapter with 90% threshold
- **Hierarchical Reporting**: Summary with expandable details
- **Auto-Fix**: Automatic correction of inappropriate CTAs and other fixable issues

### New Features
- **Character State Manager**: Complete character tracking with usage, evolution, and validation
- **Narrative Validator**: Pre/post-generation narrative validation with AI-assisted creation
- **Book Quality Tracker**: Quality metrics tracking across entire book
- **Structure Library**: 10 different chapter structures for maximum variability
- **Signature Phrase Repository**: Additive repository with rotation enforcement
- **Permission Frame Repository**: Variety enforcement with max limits

### Integration Complete
- ✅ All 9 fixes implemented (P0 and P1)
- ✅ Content generation script fully integrated
- ✅ All validators working together
- ✅ Character state management complete
- ✅ Quality tracking system operational

## 📝 Next Steps

1. Review `docs/MASTER_INDEX.md` for complete documentation
2. Start generating content: `docs/guides/GETTING_STARTED_WRITING.md`
3. Explore quality system: `docs/guides/CONTENT_VALIDATION_GUIDE.md`
4. Check compliance: `docs/guides/COMPLIANCE_ENFORCEMENT_GUIDE.md`

---

*This system ensures every piece of content is consistent, trackable, and optimized for conversion while maintaining the SureWealth brand voice.*

