# Template Navigation System

**Purpose:** Comprehensive navigation guide for finding and accessing all template variants in the MUDP system.

**Last Updated:** [DATE]  
**Version:** 1.0

---

## Directory Structure

```
callables/templates/
├── TEMPLATE_INDEX.md                    # Master template catalog
├── TEMPLATE_SELECTION_GUIDE.md          # Decision tree for template selection
├── TEMPLATE_NAVIGATION.md               # This file - navigation system
├── boilerplate/                         # Mandatory boilerplate blocks
│   ├── BOILERPLATE_INDEX.md
│   ├── jurisdiction_disclaimer_mode_a.md
│   ├── non_waiver_of_rights.md
│   ├── preservation_of_evidence_notice.md
│   ├── good_faith_resolution_statement.md
│   └── reservation_of_escalation_rights.md
│
├── tier_1_parent_resolution/
│   ├── parent_notice/
│   │   ├── TEMPLATE_SKELETON.md
│   │   ├── mode_a/                      # 40 templates (6 LGs × 5 E-classes)
│   │   └── mode_b/                      # Pending
│   ├── deletion_confirmation/
│   │   ├── TEMPLATE_SKELETON.md
│   │   └── mode_a/                      # 1 sample
│   └── device_sweep/
│       ├── TEMPLATE_SKELETON.md
│       └── mode_a/                      # 1 sample
│
├── tier_2_school_activation/
│   ├── title_ix_notice/
│   │   ├── TEMPLATE_SKELETON.md
│   │   └── mode_a/                      # 1 sample
│   ├── safety_plan_request/
│   │   ├── TEMPLATE_SKELETON.md
│   │   └── mode_a/                      # 1 sample
│   ├── district_legal_notice/
│   │   ├── TEMPLATE_SKELETON.md
│   │   └── mode_a/                      # 1 sample
│   └── documentation_request/
│       ├── TEMPLATE_SKELETON.md
│       └── mode_a/                      # 1 sample
│
├── tier_3_platform_removal/
│   ├── urgent_removal_request/
│   │   ├── TEMPLATE_SKELETON.md
│   │   └── mode_a/                      # 1 sample
│   ├── preservation_notice/
│   │   ├── TEMPLATE_SKELETON.md
│   │   └── mode_a/                      # 1 sample
│   └── repeat_upload_suppression_request/
│       ├── TEMPLATE_SKELETON.md
│       └── mode_a/                      # 1 sample
│
├── tier_4_insurance_activation/
│   ├── carrier_incident_notice/
│   │   ├── TEMPLATE_SKELETON.md
│   │   └── mode_a/                      # 1 sample
│   ├── coverage_trigger_memo/
│   │   ├── TEMPLATE_SKELETON.md
│   │   └── mode_a/                      # 1 sample
│   └── risk_mitigation_demands/
│       ├── TEMPLATE_SKELETON.md
│       └── mode_a/                      # 1 sample
│
├── tier_5_civil_litigation/
│   ├── complaint_outline/
│   │   ├── TEMPLATE_SKELETON.md
│   │   └── mode_a/                      # 1 sample
│   ├── injunction_motion_outline/
│   │   ├── TEMPLATE_SKELETON.md
│   │   └── mode_a/                      # 1 sample
│   ├── discovery_plan/
│   │   ├── TEMPLATE_SKELETON.md
│   │   └── mode_a/                      # 1 sample
│   └── spoliation_letter/
│       ├── TEMPLATE_SKELETON.md
│       └── mode_a/                      # 1 sample
│
├── tier_6_regulatory_complaints/
│   ├── attorney_general_complaint/
│   │   ├── TEMPLATE_SKELETON.md
│   │   └── mode_a/                      # 1 sample
│   ├── ftc_complaint/
│   │   ├── TEMPLATE_SKELETON.md
│   │   └── mode_a/                      # 1 sample
│   └── privacy_authority_notice/
│       ├── TEMPLATE_SKELETON.md
│       └── mode_a/                      # 1 sample
│
└── tier_7_appellate_constitutional/
    ├── constitutional_issue_preservation/
    │   ├── TEMPLATE_SKELETON.md
    │   └── mode_a/                      # 1 sample
    ├── appeal_theory_outline/
    │   ├── TEMPLATE_SKELETON.md
    │   └── mode_a/                      # 1 sample
    └── record_build_plan/
        ├── TEMPLATE_SKELETON.md
        └── mode_a/                      # 1 sample
```

---

## Template Finder

### By Escalation Tier

#### Tier 1: Parent-Parent Resolution
- **Parent Notice Letters:** `tier_1_parent_resolution/parent_notice/mode_a/`
  - 40 templates (6 logic gates × 5 evidence classes)
  - Naming: `parent_notice_lg[XX]_e[Y]_modea_t1.md`
- **Deletion Confirmation Scripts:** `tier_1_parent_resolution/deletion_confirmation/mode_a/`
- **Device Sweep Requests:** `tier_1_parent_resolution/device_sweep/mode_a/`

#### Tier 2: School Activation
- **Title IX Notices:** `tier_2_school_activation/title_ix_notice/mode_a/`
- **Safety Plan Requests:** `tier_2_school_activation/safety_plan_request/mode_a/`
- **District Legal Notices:** `tier_2_school_activation/district_legal_notice/mode_a/`
- **Documentation Requests:** `tier_2_school_activation/documentation_request/mode_a/`

#### Tier 3: Platform Removal
- **Urgent Removal Requests:** `tier_3_platform_removal/urgent_removal_request/mode_a/`
- **Preservation Notices:** `tier_3_platform_removal/preservation_notice/mode_a/`
- **Repeat Upload Suppression Requests:** `tier_3_platform_removal/repeat_upload_suppression_request/mode_a/`

#### Tier 4: Insurance Activation
- **Carrier Incident Notices:** `tier_4_insurance_activation/carrier_incident_notice/mode_a/`
- **Coverage Trigger Memos:** `tier_4_insurance_activation/coverage_trigger_memo/mode_a/`
- **Risk Mitigation Demands:** `tier_4_insurance_activation/risk_mitigation_demands/mode_a/`

#### Tier 5: Civil Litigation
- **Complaint Outlines:** `tier_5_civil_litigation/complaint_outline/mode_a/`
- **Injunction Motion Outlines:** `tier_5_civil_litigation/injunction_motion_outline/mode_a/`
- **Discovery Plans:** `tier_5_civil_litigation/discovery_plan/mode_a/`
- **Spoliation Letters:** `tier_5_civil_litigation/spoliation_letter/mode_a/`

#### Tier 6: Regulatory Complaints
- **Attorney General Complaints:** `tier_6_regulatory_complaints/attorney_general_complaint/mode_a/`
- **FTC Complaints:** `tier_6_regulatory_complaints/ftc_complaint/mode_a/`
- **Privacy Authority Notices:** `tier_6_regulatory_complaints/privacy_authority_notice/mode_a/`

#### Tier 7: Appellate and Constitutional
- **Constitutional Issue Preservation Memos:** `tier_7_appellate_constitutional/constitutional_issue_preservation/mode_a/`
- **Appeal Theory Outlines:** `tier_7_appellate_constitutional/appeal_theory_outline/mode_a/`
- **Record Build Plans:** `tier_7_appellate_constitutional/record_build_plan/mode_a/`

### By Logic Gate

#### LG_01A: Explicit Minor Sexual Depiction
**Templates Available:**
- Tier 1: All 5 evidence class variants (E1-E5)
- Tier 2: E1 sample (if LG_04 also applies)
- Tier 3: E1 sample (combined with LG_05)
- Tier 4: E1 sample
- Tier 5: E1 sample
- Tier 6: E1 sample
- Tier 7: E1 sample

**Common Combinations:**
- LG_01A + LG_02: `parent_notice_lg01a_lg02_e[X]_modea_t1.md`
- LG_01A + LG_04: `title_ix_notice_lg01a_lg04_e[X]_modea_t2.md`
- LG_01A + LG_05: `urgent_removal_request_lg01a_lg05_e[X]_modea_t3.md`
- LG_01A + LG_06: `parent_notice_lg01a_lg06_e[X]_modea_t1.md`

#### LG_01B: Sexualized Non-Explicit
**Templates Available:**
- Tier 1: All 5 evidence class variants (E1-E5)
- Tier 2: E1 sample (if LG_04 also applies)
- Tier 3: E1 sample (combined with LG_05)
- Tier 4: E1 sample
- Tier 5: E1 sample
- Tier 6: E1 sample

**Common Combinations:**
- LG_01B + LG_02: `parent_notice_lg01b_lg02_e[X]_modea_t1.md`
- LG_01B + LG_03: `parent_notice_lg01b_lg03_e[X]_modea_t1.md`
- LG_01B + LG_04: `title_ix_notice_lg01b_lg04_e[X]_modea_t2.md`

#### LG_01C: Age Ambiguous
**Templates Available:**
- Tier 1: All 5 evidence class variants (E1-E5)
- Tier 2: E1 sample (if LG_04 also applies)
- Tier 3: E1 sample (combined with LG_05)

**Common Combinations:**
- LG_01C + LG_02: `parent_notice_lg01c_lg02_e[X]_modea_t1.md`
- LG_01C + LG_03: `parent_notice_lg01c_lg03_e[X]_modea_t1.md`

#### LG_02: Recognizable Likeness
**Templates Available:**
- Tier 1: All 5 evidence class variants (E1-E5)
- Tier 2: E1 sample (if LG_04 also applies)
- Tier 3: E1 sample (combined with LG_05)

**Note:** LG_02 enhances all claims and can be combined with other gates.

#### LG_03: Economic Expectancy
**Templates Available:**
- Tier 1: All 5 evidence class variants (E1-E5)
- Tier 5: E1 sample (tortious interference claims)

**Common Combinations:**
- LG_03 + LG_01A: `parent_notice_lg01a_lg03_e[X]_modea_t1.md`
- LG_03 + LG_01B: `parent_notice_lg01b_lg03_e[X]_modea_t1.md`
- LG_03 + LG_02: `parent_notice_lg02_lg03_e[X]_modea_t1.md`

#### LG_04: Education Context
**Templates Available:**
- Tier 1: All 5 evidence class variants (E1-E5)
- Tier 2: All 4 template types (Title IX, Safety Plan, District Legal, Documentation)
- Tier 4: E1 sample (district liability)

**Note:** LG_04 often triggers mandatory Tier 2 activation.

#### LG_05: Platform Notice
**Templates Available:**
- Tier 1: All 5 evidence class variants (E1-E5)
- Tier 3: All 3 template types (Urgent Removal, Preservation, Repeat Upload Suppression)

**Common Combinations:**
- LG_05 + LG_01A: `urgent_removal_request_lg01a_lg05_e[X]_modea_t3.md`
- LG_05 + LG_01B: `urgent_removal_request_lg01b_lg05_e[X]_modea_t3.md`
- LG_05 + LG_02: `urgent_removal_request_lg02_lg05_e[X]_modea_t3.md`
- LG_05 + LG_06: `urgent_removal_request_lg06_lg05_e[X]_modea_t3.md`

#### LG_06: Biometric Processing
**Templates Available:**
- Tier 1: All 5 evidence class variants (E1-E5)
- Tier 3: E1 sample (combined with LG_05)
- Tier 6: E1 sample (Privacy Authority Notice)

**Common Combinations:**
- LG_06 + LG_01A: `parent_notice_lg01a_lg06_e[X]_modea_t1.md`
- LG_06 + LG_01B: `parent_notice_lg01b_lg06_e[X]_modea_t1.md`
- LG_06 + LG_02: `parent_notice_lg02_lg06_e[X]_modea_t1.md`
- LG_06 + LG_05: `urgent_removal_request_lg06_lg05_e[X]_modea_t3.md`

### By Evidence Class

#### E1: Direct Evidence
**Available Templates:**
- **Tier 1:** All 6 logic gates (40 templates total)
- **Tier 2:** All 4 template types (LG_04)
- **Tier 3:** All 3 template types (LG_01A+LG_05)
- **Tier 4:** All 3 template types (LG_01A)
- **Tier 5:** All 4 template types (LG_01A)
- **Tier 6:** All 3 template types (LG_01A, LG_06)
- **Tier 7:** All 3 template types (LG_01A)

**Language Characteristics:**
- Strong, definitive statements
- Can identify actor (if evidence supports)
- Strong attribution claims

#### E2: Platform Confirmations
**Available Templates:**
- **Tier 1:** All 6 logic gates (40 templates total)
- **Tier 2:** Samples pending
- **Tier 3:** Samples pending
- **Tier 4:** Samples pending
- **Tier 5:** Samples pending
- **Tier 6:** Samples pending
- **Tier 7:** Samples pending

**Language Characteristics:**
- Strong, authoritative statements
- Can identify actor (if platform confirms)
- Strong attribution claims

#### E3: Derived Similarity
**Available Templates:**
- **Tier 1:** All 6 logic gates (40 templates total)
- **Tier 2:** Samples pending
- **Tier 3:** Samples pending
- **Tier 4:** Samples pending
- **Tier 5:** Samples pending
- **Tier 6:** Samples pending
- **Tier 7:** Samples pending

**Language Characteristics:**
- Moderate language
- **Cannot identify actor** (without correlating evidence)
- Technical similarity claims

#### E4: Testimonial
**Available Templates:**
- **Tier 1:** All 6 logic gates (40 templates total)
- **Tier 2:** Samples pending
- **Tier 3:** Samples pending
- **Tier 4:** Samples pending
- **Tier 5:** Samples pending
- **Tier 6:** Samples pending
- **Tier 7:** Samples pending

**Language Characteristics:**
- Moderate language
- Conditional actor identification (only if witness has direct knowledge)
- Reported information language

#### E5: Contextual
**Available Templates:**
- **Tier 1:** All 6 logic gates (40 templates total)
- **Tier 2:** Samples pending
- **Tier 3:** Samples pending
- **Tier 4:** Samples pending
- **Tier 5:** Samples pending
- **Tier 6:** Samples pending
- **Tier 7:** Samples pending

**Language Characteristics:**
- Weak/suggestive language
- **Cannot identify actor**
- Pattern and circumstantial claims

### By Citation Mode

#### Mode A: Jurisdiction-Agnostic
**Available Templates:**
- All tiers have Mode A templates
- Default mode for most scenarios
- Uses general legal framework language
- Avoids specific statutory citations

**Location:** `mode_a/` subdirectory in each template type

#### Mode B: Jurisdiction-Specific
**Available Templates:**
- Pending generation
- Will include specific statutory citations
- Will reference state-specific laws
- Will include jurisdiction-specific procedures

**Planned Jurisdictions:**
- Kansas
- Missouri
- Additional jurisdictions as needed

**Location:** `mode_b/[JURISDICTION]/` subdirectory (e.g., `mode_b/kansas/`)

---

## Quick Access Links

### Most Common Templates

**Tier 1 Parent Notices (Complete):**
- [LG_01A, E1](tier_1_parent_resolution/parent_notice/mode_a/parent_notice_lg01a_e1_modea_t1.md)
- [LG_01B, E1](tier_1_parent_resolution/parent_notice/mode_a/parent_notice_lg01b_e1_modea_t1.md)
- [LG_01C, E1](tier_1_parent_resolution/parent_notice/mode_a/parent_notice_lg01c_e1_modea_t1.md)
- [LG_02, E1](tier_1_parent_resolution/parent_notice/mode_a/parent_notice_lg02_e1_modea_t1.md)
- [LG_03, E1](tier_1_parent_resolution/parent_notice/mode_a/parent_notice_lg03_e1_modea_t1.md)
- [LG_04, E1](tier_1_parent_resolution/parent_notice/mode_a/parent_notice_lg04_e1_modea_t1.md)
- [LG_05, E1](tier_1_parent_resolution/parent_notice/mode_a/parent_notice_lg05_e1_modea_t1.md)
- [LG_06, E1](tier_1_parent_resolution/parent_notice/mode_a/parent_notice_lg06_e1_modea_t1.md)

**Tier 2 School Activation:**
- [Title IX Notice, LG_04, E1](tier_2_school_activation/title_ix_notice/mode_a/title_ix_notice_lg04_e1_modea_t2.md)
- [Safety Plan Request, LG_04, E1](tier_2_school_activation/safety_plan_request/mode_a/safety_plan_request_lg04_e1_modea_t2.md)

**Tier 3 Platform Removal:**
- [Urgent Removal Request, LG_01A+LG_05, E1](tier_3_platform_removal/urgent_removal_request/mode_a/urgent_removal_request_lg01a_lg05_e1_modea_t3.md)
- [Preservation Notice, LG_01A+LG_05, E1](tier_3_platform_removal/preservation_notice/mode_a/preservation_notice_lg01a_lg05_e1_modea_t3.md)

---

## Template Naming Convention

**Format:** `[template_type]_[logic_gates]_[evidence_class]_[citation_mode]_[tier].md`

**Components:**
- `template_type`: Type of template (e.g., `parent_notice`, `title_ix_notice`)
- `logic_gates`: Logic gate(s) applicable (e.g., `lg01a`, `lg01a_lg02`)
- `evidence_class`: Evidence class (e.g., `e1`, `e2`, `e3`, `e4`, `e5`)
- `citation_mode`: Citation mode (e.g., `modea`, `modeb_kansas`)
- `tier`: Escalation tier (e.g., `t1`, `t2`, `t3`)

**Examples:**
- `parent_notice_lg01a_e1_modea_t1.md` - Single logic gate
- `parent_notice_lg01a_lg02_e1_modea_t1.md` - Combined logic gates
- `title_ix_notice_lg04_e2_modea_t2.md` - Tier 2, E2 evidence
- `urgent_removal_request_lg01a_lg05_e1_modeb_kansas_t3.md` - Mode B, Kansas

---

## Cross-Reference Map

### Template Relationships

**Tier 1 → Tier 2:**
- Parent Notice (LG_04) → Title IX Notice
- Parent Notice (LG_04) → Safety Plan Request
- Parent Notice (LG_04) → District Legal Notice

**Tier 1 → Tier 3:**
- Parent Notice (LG_05) → Urgent Removal Request
- Parent Notice (LG_05) → Preservation Notice

**Tier 2 → Tier 4:**
- District Legal Notice → Carrier Incident Notice (district liability)

**Tier 3 → Tier 4:**
- Urgent Removal Request → Carrier Incident Notice (platform liability)

**Tier 4 → Tier 5:**
- Coverage Trigger Memo → Complaint Outline
- Risk Mitigation Demands → Discovery Plan

**Tier 5 → Tier 6:**
- Complaint Outline → Attorney General Complaint
- Complaint Outline → FTC Complaint

**Tier 5 → Tier 7:**
- Complaint Outline → Constitutional Issue Preservation
- Discovery Plan → Record Build Plan

**Tier 6 → Tier 7:**
- Regulatory Complaints → Appeal Theory Outline

### Logic Gate Combinations

**Common Multi-Gate Templates:**
- LG_01A + LG_02: Explicit + Recognizable Likeness
- LG_01A + LG_04: Explicit + Education Context
- LG_01A + LG_05: Explicit + Platform Notice
- LG_01A + LG_06: Explicit + Biometric Processing
- LG_01B + LG_02: Non-Explicit + Recognizable Likeness
- LG_01B + LG_03: Non-Explicit + Economic Expectancy
- LG_01B + LG_04: Non-Explicit + Education Context
- LG_02 + LG_03: Recognizable Likeness + Economic Expectancy
- LG_02 + LG_06: Recognizable Likeness + Biometric Processing
- LG_05 + LG_06: Platform Notice + Biometric Processing

**Note:** Combined templates may be generated as needed, or use primary gate template with notes about additional gates.

---

## Search Strategies

### Find Template by Scenario

1. **Identify Logic Gates:** Use [TEMPLATE_SELECTION_GUIDE.md](./TEMPLATE_SELECTION_GUIDE.md) to identify applicable logic gates
2. **Classify Evidence:** Determine evidence class (E1-E5)
3. **Select Citation Mode:** Choose Mode A (default) or Mode B (if jurisdiction known)
4. **Determine Tier:** Identify appropriate escalation tier
5. **Navigate to Directory:** Use directory structure above to locate template

### Find Template by Name

1. **Parse Template Name:** Extract components from naming convention
2. **Navigate by Tier:** Go to `tier_[X]_[name]/[template_type]/mode_[X]/`
3. **Locate File:** Find file matching naming pattern

### Find Related Templates

1. **Check Cross-Reference Map:** See template relationships above
2. **Check Template Notes:** Each template includes "Related Templates" section
3. **Check Logic Gate Combinations:** See common combinations above

---

## Template Status

### Complete (Mode A, E1-E5)
- ✅ Tier 1 Parent Notices: All 6 logic gates × 5 evidence classes = 40 templates

### Structure Established (Mode A, E1 samples)
- ✅ Tier 1: Deletion Confirmation, Device Sweep
- ✅ Tier 2: All 4 template types
- ✅ Tier 3: All 3 template types
- ✅ Tier 4: All 3 template types
- ✅ Tier 5: All 4 template types
- ✅ Tier 6: All 3 template types
- ✅ Tier 7: All 3 template types

### Pending
- ⏳ Mode B (jurisdiction-specific) templates
- ⏳ Additional evidence class variants (E2-E5) for Tiers 2-7
- ⏳ Logic gate combination templates
- ⏳ Additional template types as needed

---

## Related Documents

- [Template Index](./TEMPLATE_INDEX.md) - Master template catalog
- [Template Selection Guide](./TEMPLATE_SELECTION_GUIDE.md) - Decision tree
- [Logic Gates](../../data/logic_gates.yaml) - Logic gate definitions
- [Evidence Classification](../../data/evidence_classification.yaml) - Evidence class definitions
- [Enforcement Tiers](../../data/enforcement_tiers.yaml) - Tier definitions
- [Citation Modes](../../docs/legal/citation_modes.md) - Citation mode documentation
- [Drafting Rules](../../docs/legal/drafting_rules.md) - Drafting requirements
- [Boilerplate Index](./boilerplate/BOILERPLATE_INDEX.md) - Boilerplate library
- [Cross References](../../data/cross_references.yaml) - System cross-references
- [Master Index](../../docs/MASTER_INDEX.md) - Master navigation

---

## Version History

- **v1.0** - Initial navigation system with all 7 tiers documented

