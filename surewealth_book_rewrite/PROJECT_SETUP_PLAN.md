# 📋 SureWealth Book Rewrite - Project Setup Plan

## 🎯 Project Overview

This document outlines the initialization and structure for the **SureWealth Book Rewrite** project—a stateful, AI-assisted book writing system that maintains consistency through a comprehensive meta-framework.

**Core Objective:** Build a book writing system that tracks and constrains all narrative elements (characters, metaphors, story threads, financial scenarios) in a stateful YAML-based index system, enabling consistent AI-generated content that references and builds upon established elements.

---

## 📁 Proposed Folder Structure

```
surewealth_book_rewrite/
│
├── 📚 docs/                          # Core reference documents
│   ├── SRP_SureWealthBook.md         # System Reference Document
│   ├── book_emotional_journey.md     # Emotional journey map
│   ├── persuasion_machine.md         # Conversion optimization
│   ├── storytelling_guidelines.md    # Storytelling rules
│   ├── writer_standards.md           # Writing standards
│   └── GoogleContentGuidelines.md    # SEO/content guidelines
│
├── 🗂️ meta_framework/                 # Stateful tracking system
│   ├── index.yaml                    # Master index of all tracked elements
│   ├── characters/                   # Character profiles & financial situations
│   │   ├── characters_index.yaml     # Character registry
│   │   ├── john_smith.yaml           # Example: John's profile
│   │   └── [character_name].yaml     # Individual character files
│   │
│   ├── narratives/                   # Story threads & narrative elements
│   │   ├── narratives_index.yaml     # Narrative registry
│   │   ├── allegories/               # Allegory library
│   │   │   └── allegories_index.yaml
│   │   ├── metaphors/                # Metaphor library
│   │   │   └── metaphors_index.yaml
│   │   ├── case_studies/             # Composite case studies
│   │   │   └── case_studies_index.yaml
│   │   └── story_threads/            # Running narrative threads
│   │       └── threads_index.yaml
│   │
│   ├── language/                     # Linguistic constraints
│   │   ├── tone_guide.yaml           # Voice & tone rules
│   │   ├── vocabulary.yaml           # Approved/banned words
│   │   ├── signature_phrases.yaml    # Brand phrases
│   │   └── linguistic_patterns.yaml  # Sentence structures
│   │
│   ├── tools_ctas/                   # Conversion tools & CTAs
│   │   ├── tools_index.yaml          # Tool registry
│   │   ├── cta_library.yaml          # CTA templates by context
│   │   └── toolhook_map.yaml         # Concept → Tool → CTA mapping
│   │
│   ├── visuals/                      # Visual language system
│   │   ├── charts_index.yaml         # Chart types & usage
│   │   ├── illustrations_index.yaml   # Illustration concepts
│   │   └── visual_grammar.yaml       # Color/symbol system
│   │
│   └── chapters/                     # Chapter-level tracking
│       ├── chapters_index.yaml       # Chapter registry
│       └── [chapter_number]_[title].yaml  # Individual chapter metadata
│
├── 📖 content/                       # Generated book content
│   ├── drafts/                       # Working drafts
│   ├── chapters/                     # Finalized chapters
│   │   └── chapter_01_retirement_reality_check.md
│   ├── appendices/                   # Supporting content
│   └── worksheets/                   # Interactive elements
│
├── 🔧 scripts/                        # Automation & ingestion tools
│   ├── ingest.py                     # Ingestion function (concepts → elements)
│   ├── validate.py                   # Validation against framework
│   ├── reference_check.py            # Check character/narrative consistency
│   └── generate_index.py             # Rebuild indexes from elements
│
├── 📊 tracking/                       # Project management
│   ├── content_matrix.yaml           # Content objectives matrix
│   ├── conversion_map.yaml           # Funnel stage tracking
│   └── progress_log.md               # Writing progress
│
└── 🧪 templates/                     # Reusable templates
    ├── character_template.yaml
    ├── narrative_template.yaml
    ├── chapter_template.yaml
    └── ingestion_template.md         # Template for ingesting new concepts
```

---

## 🧩 Meta-Framework Components

### 1. **Character Tracking System**

**Purpose:** Track all characters (like John) with their complete financial profiles, ensuring consistency when referenced across chapters.

**Structure:**
```yaml
# characters/john_smith.yaml
character:
  id: JOHN_SMITH
  name: John Smith
  type: composite_case_study
  first_appearance: chapter_01
  last_referenced: chapter_06
  
  demographics:
    age: 58
    marital_status: single_father
    occupation: engineer
    education: college_degree
    
  financial_profile:
    annual_income: 100000
    savings: 450000
    retirement_accounts:
      - type: 401k
        balance: 320000
        contribution_rate: 0.15
      - type: ira
        balance: 130000
    home_equity: 180000
    debt: 45000
    
  emotional_profile:
    primary_fears: [market_crash, outliving_savings]
    aspirations: [financial_security, legacy_for_children]
    awareness_level: problem-aware
    buyer_sophistication: medium
    
  narrative_arc:
    - chapter: 01
      situation: Introduced as single father concerned about retirement
      financial_focus: 401k contributions
    - chapter: 03
      situation: Social Security claiming decision
      financial_focus: Optimal claiming strategy
    - chapter: 06
      situation: Final outcome - peace of mind achieved
      financial_focus: Complete strategy implementation
      
  references:
    - chapter_01_line_45: "John, a single father making $100,000 annually..."
    - chapter_03_line_120: "Remember John? His 401k contributions..."
```

### 2. **Narrative Elements Index**

**Purpose:** Track all allegories, metaphors, case studies, and story threads for reuse and consistency.

**Categories:**
- **Allegories:** Complete stories (e.g., "Leaky Bucket", "House of Cards")
- **Metaphors:** Short comparisons (e.g., "retirement as a garden")
- **Case Studies:** Composite client stories (e.g., "Mark the Engineer")
- **Story Threads:** Running themes across chapters (e.g., "The Conventional Wisdom Trap")

### 3. **Language Constraint System**

**Purpose:** Lock in tone, vocabulary, and linguistic patterns to ensure consistent voice.

**Components:**
- Tone rules (empathetic expert, not guru)
- Approved vocabulary (power words)
- Banned words (compliance/positioning)
- Signature phrases
- Sentence structure patterns

### 4. **Tool & CTA Mapping**

**Purpose:** Map financial concepts to appropriate tools and CTAs for conversion optimization.

**Structure:**
```yaml
# tools_ctas/toolhook_map.yaml
concepts:
  - concept: roth_conversion
    emotional_hook: fear_of_tax_spikes
    awareness_level: solution-aware
    recommended_tool: lifetime_tax_calculator
    cta_copy: "What's your conversion sweet spot?"
    urgency_trigger: "Every year you wait, taxes compound"
```

### 5. **Chapter Metadata Tracking**

**Purpose:** Track each chapter's emotional arc, narrative elements used, characters referenced, and conversion elements.

**Structure:**
```yaml
# chapters/01_retirement_reality_check.yaml
chapter:
  number: 1
  title: Retirement Reality Check
  emotional_arc:
    start: vulnerability
    end: urgency
  awareness_level: unaware_to_problem-aware
  
  narrative_elements:
    allegories: [ALLEGORY_HOUSE_OF_CARDS]
    metaphors: [market_as_storm]
    characters: [JOHN_SMITH]
    story_threads: [CONVENTIONAL_WISDOM_TRAP]
    
  tools_ctas:
    embedded_tool: retirement_risk_assessment
    primary_cta: "Is your portfolio built on sand?"
    
  content_insertions:
    - type: chart
      name: market_volatility_chart
      location: after_paragraph_3
    - type: tool_link
      name: retirement_risk_assessment
      location: end_of_chapter
```

---

## 🔄 Ingestion Function Design

**Purpose:** Break down principles/concepts into trackable elements (characters, scenes, plots, outcomes, tools).

**Process Flow:**
1. **Input:** Concept/principle (e.g., "Roth conversion strategy for high earners")
2. **Analysis:** Extract:
   - Potential character scenarios
   - Applicable metaphors/allegories
   - Emotional triggers
   - Tool/CTA opportunities
   - Chapter placement suggestions
3. **Output:** Structured YAML elements ready for integration

**Example Ingestion:**
```
Input: "Single parent with $100k income needs to optimize 401k contributions"

Output:
- New character profile (if not exists)
- Financial scenario data
- Chapter placement recommendation
- Tool recommendation (401k optimizer)
- CTA suggestion
```

---

## 🔗 Cross-Reference System

**Master Index (`meta_framework/index.yaml`):**
- Central registry of all element IDs
- Cross-references between elements
- Usage tracking (where elements appear)
- Dependency mapping (which elements reference others)

**Example:**
```yaml
index:
  characters:
    JOHN_SMITH:
      referenced_in: [chapter_01, chapter_03, chapter_06]
      uses_narratives: [ALLEGORY_LEAKY_BUCKET]
      uses_tools: [lifetime_tax_calculator]
      
  narratives:
    ALLEGORY_LEAKY_BUCKET:
      used_in_chapters: [chapter_02, chapter_05]
      associated_characters: [JOHN_SMITH, MARK_ENGINEER]
      emotional_trigger: tax_drag_fear
```

---

## ✅ Implementation Steps

### Phase 1: Folder Structure & Base Templates
1. Create folder structure
2. Move existing docs to `docs/` folder
3. Create base YAML templates for all element types
4. Initialize master index

### Phase 2: Framework Population
1. Extract existing elements from `story_vault_template.yaml`
2. Create character profiles from existing case studies
3. Build narrative elements index
4. Create language constraint files
5. Map tools/CTAs from emotional journey doc

### Phase 3: Ingestion System
1. Build Python ingestion function
2. Create validation scripts
3. Build reference checking system
4. Create index generation automation

### Phase 4: Chapter Integration
1. Create chapter metadata templates
2. Build chapter tracking system
3. Integrate with content generation workflow

---

## 🎯 Success Criteria

The system is ready when:
- ✅ All existing elements are tracked in YAML
- ✅ Character references are consistent across chapters
- ✅ Narrative elements can be queried and reused
- ✅ Language constraints are enforced
- ✅ Ingestion function can process new concepts
- ✅ Cross-references are maintained automatically
- ✅ AI can generate content that references tracked elements

---

## 📝 Next Steps

1. **Review this plan** - Confirm structure and approach
2. **Initialize folders** - Create directory structure
3. **Extract existing data** - Populate framework from current docs
4. **Build ingestion function** - Create automation tools
5. **Test with first chapter** - Validate system with real content

---

*This plan serves as the blueprint for building a stateful, constraint-driven book writing system that ensures consistency and enables iterative AI-assisted content generation.*

