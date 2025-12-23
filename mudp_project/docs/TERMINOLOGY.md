# MUDP System Terminology Glossary

**Purpose:** Comprehensive glossary of all key terms used in the MUDP system  
**Status:** Core System Component  
**Last Updated:** 2025-12-23

---

## Overview

This glossary provides definitions and usage guidance for all key terms used throughout the MUDP system. It ensures consistent terminology across all documentation and templates.

---

## System Terms

### MUDP

**Full Name:** Maximum Upfront Defensible Position  
**Alternative Name:** MudPie Protocol  
**Variant:** MUDP-CM (Crisis-Management Edition)

**Definition:** A comprehensive child digital personhood protection system that creates maximum upfront defensible position through economic, technical, legal, and institutional protections.

**Usage:**
- Use "MUDP" as the primary term
- "MudPie Protocol" is an informal nickname
- "MUDP-CM" refers specifically to the crisis-management edition

**Cross-References:**
- [MUDP Philosophy](../strategic/mudp_philosophy.md)
- [Four-Pillar Architecture](../strategic/four_pillars.md)

---

### Digital Personhood

**Definition:** The comprehensive protection of a child's digital identity, likeness, biometric presence, and all derivatives.

**Components:**
- Digital identity
- Likeness (visual representation)
- Biometric presence (facial recognition, embeddings)
- Derivatives (AI-generated, deepfakes, synthetic media)

**Usage:** Use "Digital Personhood" when referring to the comprehensive concept. Use specific terms (likeness, biometric data) when referring to specific components.

**Cross-References:**
- [Four-Pillar Architecture](../strategic/four_pillars.md)
- [Technical Provenance System](../technical/provenance_system.md)

---

### Likeness Asset

**Definition:** An economically valued representation of a child's likeness, protected under right of publicity and contractual frameworks.

**Characteristics:**
- Has quantifiable economic value
- Protected by right of publicity laws
- Subject to contractual licensing
- Can be valued for damages claims

**Usage:** Use "Likeness Asset" when referring to the economic/legal concept. Use "likeness" when referring to the visual representation itself.

**Cross-References:**
- [Four-Pillar Architecture - Pillar 1](../strategic/four_pillars.md#pillar-1-economic--contractual-protection)
- [Causes of Action - Right of Publicity](../legal/causes_of_action.md#1-right-of-publicity-ropa)

---

## Technical Terms

### Provenance Ledger / Provenance Registry

**Primary Term:** Provenance Registry (use this in documentation)  
**Alternative Term:** Provenance Ledger (used in SRD_DSKB.yaml)

**Definition:** A hash-based registry system that tracks originals, versions, publication locations, and chain of custody for all digital assets.

**Components:**
- Hash-based identification
- Version tracking
- Publication location tracking
- Chain of custody documentation

**Usage:** Use "Provenance Registry" as the primary term. "Provenance Ledger" is acceptable but less preferred.

**Cross-References:**
- [Technical Provenance System](../technical/provenance_system.md)
- [Four-Pillar Architecture - Pillar 2](../strategic/four_pillars.md#pillar-2-technical--evidentiary-infrastructure)

---

### Hash Boundary System (HBS)

**Full Name:** Hash Boundary System  
**Abbreviation:** HBS

**Definition:** A comprehensive framework combining SHA-256 cryptographic hashes, perceptual hashes (pHash, dHash, aHash), and embedding vector similarity for identifying and tracking digital assets.

**Components:**
- SHA-256 cryptographic hashes
- Perceptual hashes (pHash, dHash, aHash)
- Embedding vectors (FaceNet, ArcFace)
- Similarity thresholds

**Usage:** Use "Hash Boundary System" or "HBS" when referring to the complete framework.

**Cross-References:**
- [Technical Provenance System](../technical/provenance_system.md)
- [Evidence Classification](../../data/evidence_classification.yaml)

---

### Perceptual Hashing

**Definition:** Fuzzy image matching techniques that can identify similar images even after minor modifications.

**Types:**
- **pHash:** Perceptual hash
- **dHash:** Difference hash
- **aHash:** Average hash

**Usage:** Use "perceptual hashing" for the general concept. Use specific types (pHash, dHash, aHash) when referring to specific algorithms.

**Cross-References:**
- [Technical Provenance System](../technical/provenance_system.md)

---

### Embedding Vectors

**Definition:** AI-based similarity detection using neural network embeddings to identify likeness and similarity.

**Types:**
- **FaceNet:** Facial recognition embeddings
- **ArcFace:** Advanced facial recognition embeddings

**Usage:** Use "embedding vectors" for the general concept. Use specific types (FaceNet, ArcFace) when referring to specific models.

**Cross-References:**
- [Technical Provenance System](../technical/provenance_system.md)
- [Evidence Classification - E3](../../data/evidence_classification.yaml)

---

### Biometric Non-Consent License

**Definition:** A policy notice and evidentiary artifact that limits machine learning and AI processing of biometric data without explicit consent.

**Purpose:**
- Create digital property perimeter
- Establish consent requirements
- Provide evidentiary basis for claims
- Activate biometric privacy laws

**Usage:** Use "Biometric Non-Consent License" as the formal term.

**Cross-References:**
- [Four-Pillar Architecture - Pillar 1](../strategic/four_pillars.md#pillar-1-economic--contractual-protection)
- [Regulatory Matrix](../../data/regulatory_matrix.yaml)

---

## Legal Terms

### Right of Publicity (ROPA)

**Full Name:** Right of Publicity  
**Abbreviation:** ROPA

**Definition:** Legal right to control the commercial use of one's name, likeness, or other identifying characteristics.

**Usage:** Use "Right of Publicity" or "ROPA" when referring to this legal doctrine.

**Cross-References:**
- [Causes of Action - Right of Publicity](../legal/causes_of_action.md#1-right-of-publicity-ropa)
- [Regulatory Matrix](../../data/regulatory_matrix.yaml)

---

### CSAM

**Full Name:** Child Sexual Abuse Material  
**Abbreviation:** CSAM

**Definition:** Material that depicts sexual conduct involving a minor, including AI-generated content.

**Legal Framework:**
- 18 U.S.C. §2252 (Distribution)
- 18 U.S.C. §2256 (Definition)
- Includes AI-generated content (2024-2025 updates)

**Usage:** Use "CSAM" as the abbreviation. Spell out "Child Sexual Abuse Material" on first use in formal documents.

**Cross-References:**
- [Causes of Action - Federal CSAM Law](../legal/causes_of_action.md#3-federal-csam-law)
- [Regulatory Matrix](../../data/regulatory_matrix.yaml)

---

### DMCA

**Full Name:** Digital Millennium Copyright Act  
**Abbreviation:** DMCA

**Definition:** Federal law providing copyright-based takedown procedures for online content.

**Usage:** Use "DMCA" as the abbreviation. Spell out "Digital Millennium Copyright Act" on first use in formal documents.

**Cross-References:**
- [Causes of Action - DMCA Takedown](../legal/causes_of_action.md#4-dmca-takedown-copyright)
- [Implementation Phases - Phase 1](../../plans/implementation_phases.yaml)

---

### BIPA

**Full Name:** Biometric Information Privacy Act  
**Abbreviation:** BIPA

**Definition:** Illinois state law (and similar laws in other states) regulating the collection and use of biometric data.

**Usage:** Use "BIPA" as the abbreviation. Note that not all states have BIPA equivalents.

**Cross-References:**
- [Regulatory Matrix](../../data/regulatory_matrix.yaml)
- [Biometric Non-Consent License](#biometric-non-consent-license)

---

### IIED / NIED

**IIED:** Intentional Infliction of Emotional Distress  
**NIED:** Negligent Infliction of Emotional Distress

**Definition:** Tort claims for emotional harm caused by intentional or negligent conduct.

**Usage:** Use abbreviations "IIED" and "NIED" after first use.

**Cross-References:**
- [Causes of Action - Emotional Distress](../legal/causes_of_action.md#5-emotional-distress--privacy-tort)

---

### Title IX

**Definition:** Federal law prohibiting sex discrimination in educational programs receiving federal funding.

**Key Provisions:**
- Requires investigation of sexual harassment
- Mandates safety planning
- Triggers district legal involvement

**Usage:** Use "Title IX" as the standard term.

**Cross-References:**
- [Enforcement Tiers - Tier 2](../../data/enforcement_tiers.yaml)
- [Regulatory Matrix](../../data/regulatory_matrix.yaml)

---

### FERPA

**Full Name:** Family Educational Rights and Privacy Act  
**Abbreviation:** FERPA

**Definition:** Federal law protecting student educational records and privacy.

**Usage:** Use "FERPA" as the abbreviation.

**Cross-References:**
- [Regulatory Matrix](../../data/regulatory_matrix.yaml)

---

## System Framework Terms

### Four-Pillar Defense Architecture

**Also Known As:** Four-Pillar System, Four Pillars

**Definition:** The core defensive architecture of MUDP, consisting of four integrated protection pillars.

**Pillars:**
1. **Pillar 1:** Economic & Contractual Protection
2. **Pillar 2:** Technical & Evidentiary Infrastructure
3. **Pillar 3:** Legal & Regulatory Framework
4. **Pillar 4:** Institutional Advance Positioning

**Usage:** Use "Four-Pillar Defense Architecture" or "Four Pillars" as the standard terms.

**Cross-References:**
- [Four-Pillar Architecture](../strategic/four_pillars.md)

---

### Enforcement Tiers / Escalation Readiness Map

**Primary Term:** Enforcement Tiers (use this in documentation)  
**Alternative Term:** Escalation Readiness Map (used in SRD_DSKB.yaml)

**Definition:** A seven-tier escalation system for responding to incidents, from parent-parent resolution to appellate/constitutional review.

**Tiers:**
- **Tier 1:** Parent-Parent Resolution
- **Tier 2:** School Activation
- **Tier 3:** Platform/App Removal
- **Tier 4:** Insurance Activation
- **Tier 5:** Civil Litigation
- **Tier 6:** Regulatory Complaints
- **Tier 7:** Appellate/Constitutional

**Usage:** Use "Enforcement Tiers" as the primary term. "Escalation Readiness Map" refers to the comprehensive mapping of all lawful paths.

**Cross-References:**
- [Enforcement Tiers](../../data/enforcement_tiers.yaml)
- [Crisis Playbook](../operational/crisis_playbook.md)

---

### Rapid Response Packet

**Definition:** Pre-compiled legal notices for parents, school, platform, insurers, and counsel, ready for immediate deployment.

**Components:**
- Parent notification letters
- School district notices
- Platform removal requests
- Insurance incident reports
- Legal counsel summaries

**Usage:** Use "Rapid Response Packet" as the standard term.

**Cross-References:**
- [Four-Pillar Architecture - Pillar 3](../strategic/four_pillars.md#pillar-3-legal--regulatory-framework)
- [Implementation Phases - Phase 4](../../plans/implementation_phases.yaml)

---

## Logic Gate Terms

### Logic Gates (LG_01A through LG_06)

**Definition:** Scenario categorization system that determines which pre-generated templates and legal pathways are available.

**Gates:**
- **LG_01A:** Explicit Minor Sexual Depiction
- **LG_01B:** Sexualized Non-Explicit
- **LG_01C:** Age Ambiguous
- **LG_02:** Recognizable Likeness
- **LG_03:** Economic Expectancy
- **LG_04:** Education Context
- **LG_05:** Platform Notice
- **LG_06:** Biometric Processing

**Usage:** Use "Logic Gate" or "LG" with the identifier (e.g., "LG_01A", "Logic Gate LG_01A").

**Cross-References:**
- [Logic Gates](../../data/logic_gates.yaml)
- [Template Selection Guide](../../callables/templates/TEMPLATE_SELECTION_GUIDE.md)

---

## Evidence Classification Terms

### Evidence Classes (E1 through E5)

**Definition:** Classification system for evidence strength that determines appropriate language strength in templates.

**Classes:**
- **E1:** Direct Evidence
- **E2:** Platform Confirmations
- **E3:** Derived Similarity
- **E4:** Testimonial
- **E5:** Contextual

**Usage:** Use "Evidence Class" or "E" with the class number (e.g., "E1", "Evidence Class E1").

**Cross-References:**
- [Evidence Classification](../../data/evidence_classification.yaml)
- [Template Selection Guide](../../callables/templates/TEMPLATE_SELECTION_GUIDE.md)

---

## Citation Mode Terms

### Mode A / Mode B

**Mode A:** Jurisdiction-Agnostic  
**Mode B:** Jurisdiction-Specific

**Definition:** Two citation modes for template generation, determining whether templates use generic legal references (Mode A) or specific statute citations (Mode B).

**Usage:** Use "Mode A" and "Mode B" as the standard terms.

**Cross-References:**
- [Citation Modes](../legal/citation_modes.md)
- [Jurisdiction Overlays](../../callables/jurisdiction_overlays/)

---

## Sexualization Level Terms

### Explicit Minor Sexual Depiction

**Definition:** Apparent minor + explicit sexual content or nudity.

**Drafting Posture:** Treat as high-risk; preserve reporting/removal pathways; avoid guilt assertions.

**Usage:** Use "Explicit Minor Sexual Depiction" or "LG_01A" when referring to this level.

**Cross-References:**
- [Logic Gates - LG_01A](../../data/logic_gates.yaml)
- [SRD_DSKB Definitions](../../plans/SRD_DSKB.yaml)

---

### Sexualized Non-Explicit

**Definition:** Apparent minor + sexualized pose/context/implication without explicit nudity.

**Drafting Posture:** Assert civil/school frameworks strongly; criminal framing conditional.

**Usage:** Use "Sexualized Non-Explicit" or "LG_01B" when referring to this level.

**Cross-References:**
- [Logic Gates - LG_01B](../../data/logic_gates.yaml)
- [SRD_DSKB Definitions](../../plans/SRD_DSKB.yaml)

---

### Age Ambiguous

**Definition:** Age not provable; plausible minor.

**Drafting Posture:** Treat as high-risk; conservative; preserve options pending clarification.

**Usage:** Use "Age Ambiguous" or "LG_01C" when referring to this level.

**Cross-References:**
- [Logic Gates - LG_01C](../../data/logic_gates.yaml)
- [SRD_DSKB Definitions](../../plans/SRD_DSKB.yaml)

---

## Likeness Recognition Terms

### Recognizable Likeness Standard

**Definition:** Standard for determining when a child's likeness is recognizable.

**Tests:**
- Reasonable observer identification
- Biometric similarity above threshold
- Claimed or implied identity

**Usage:** Use "Recognizable Likeness Standard" when referring to the standard. Use "recognizable likeness" when referring to the fact.

**Cross-References:**
- [Logic Gates - LG_02](../../data/logic_gates.yaml)
- [SRD_DSKB Definitions](../../plans/SRD_DSKB.yaml)

---

### Credible Notice Minimum

**Definition:** Minimum requirements for providing credible notice to platforms or institutions.

**Required Elements:**
- Affected minor identifier
- Content description
- Locator or identifier (URL, account handle, message ID, hash)
- Good faith assertion of harm

**Usage:** Use "Credible Notice Minimum" when referring to the requirements.

**Cross-References:**
- [Logic Gates - LG_05](../../data/logic_gates.yaml)
- [SRD_DSKB Definitions](../../plans/SRD_DSKB.yaml)

---

## Stakeholder Terms

### Custodial Parents

**Definition:** Primary decision-makers and legal guardians of the child.

**Role:** Primary stakeholder with decision authority.

**Usage:** Use "Custodial Parents" as the standard term.

**Cross-References:**
- [Stakeholders](../../data/stakeholders.yaml)

---

### Opposing Parents

**Definition:** Parents of the child who created or distributed harmful content.

**Role:** Target of Tier 1 resolution.

**Usage:** Use "Opposing Parents" as the standard term.

**Cross-References:**
- [Stakeholders](../../data/stakeholders.yaml)
- [Enforcement Tiers - Tier 1](../../data/enforcement_tiers.yaml)

---

## Template Terms

### Template Skeleton

**Definition:** Base template structure that serves as the foundation for all template variants.

**Usage:** Use "Template Skeleton" when referring to the base structure.

**Cross-References:**
- [Template System](../../callables/templates/)

---

### Boilerplate

**Definition:** Mandatory reusable blocks that must be included in all templates.

**Required Boilerplate:**
1. Jurisdiction Disclaimer
2. Non-Waiver of Rights
3. Preservation of Evidence Notice
4. Good Faith Resolution Statement
5. Reservation of Escalation Rights

**Usage:** Use "Boilerplate" or "Mandatory Boilerplate" when referring to these blocks.

**Cross-References:**
- [Boilerplate Library](../../callables/templates/boilerplate/)
- [Drafting Rules](../legal/drafting_rules.md)

---

## Implementation Terms

### Implementation Phases

**Definition:** Five-phase roadmap for implementing the MUDP system.

**Phases:**
1. Phase 1: Copyright Registration
2. Phase 2: Likeness Licensing Framework
3. Phase 3: Technical Provenance System
4. Phase 4: Rapid Response Legal Packet
5. Phase 5: Economic Harm Documentation

**Usage:** Use "Implementation Phases" or "Phase [X]" when referring to the phases.

**Cross-References:**
- [Implementation Phases](../../plans/implementation_phases.yaml)

---

### Binder Structure

**Definition:** 15-tab organizational system for comprehensive MUDP documentation.

**Usage:** Use "Binder Structure" or "15-Tab Binder" when referring to this system.

**Cross-References:**
- [Binder Structure](../../plans/binder_structure.yaml)

---

## Doctrine Terms

### Human-Governed Crisis-Management Doctrine

**Definition:** The system type and philosophy of MUDP, emphasizing human decision authority and battlefield mapping rather than autonomous execution.

**Key Principles:**
- Worst-case ready
- Roadmap to appellate review
- Human decision authority
- Purpose is battlefield mapping, not autonomous execution

**Usage:** Use "Human-Governed Crisis-Management Doctrine" when referring to the system type.

**Cross-References:**
- [SRD_DSKB System Type](../../plans/SRD_DSKB.yaml)
- [MUDP Philosophy](../strategic/mudp_philosophy.md)

---

## Terminology Alignment Notes

### Preferred Terms

Use these terms consistently across all documentation:

- **MUDP** (not "MudPie Protocol" in formal contexts)
- **Provenance Registry** (preferred over "Provenance Ledger")
- **Enforcement Tiers** (preferred over "Escalation Readiness Map" in general documentation)
- **Digital Personhood** (for comprehensive concept)
- **Likeness Asset** (for economic/legal concept)
- **Hash Boundary System** or **HBS** (for technical framework)

### Terms Requiring Context

Some terms have specific meanings in different contexts:

- **Escalation Readiness Map:** Use when referring to the comprehensive mapping of all lawful paths (SRD_DSKB context)
- **Enforcement Tiers:** Use when referring to the escalation system (general documentation)
- **Provenance Ledger:** Acceptable alternative to "Provenance Registry" but less preferred

### Terms to Avoid

Avoid these terms or use with caution:

- **"MudPie Protocol"** - Use only as informal nickname, not in formal documentation
- **"Autonomous system"** - System is human-governed, not autonomous
- **"Automated enforcement"** - System provides decision-ready artifacts, not automated enforcement

---

## Cross-Reference Map

### By Category

**System Terms:**
- MUDP → [MUDP Philosophy](../strategic/mudp_philosophy.md)
- Digital Personhood → [Four-Pillar Architecture](../strategic/four_pillars.md)
- Likeness Asset → [Causes of Action - ROPA](../legal/causes_of_action.md)

**Technical Terms:**
- Provenance Registry → [Technical Provenance System](../technical/provenance_system.md)
- Hash Boundary System → [Technical Provenance System](../technical/provenance_system.md)
- Perceptual Hashing → [Technical Provenance System](../technical/provenance_system.md)

**Legal Terms:**
- ROPA → [Causes of Action](../legal/causes_of_action.md)
- CSAM → [Causes of Action](../legal/causes_of_action.md)
- DMCA → [Causes of Action](../legal/causes_of_action.md)
- Title IX → [Enforcement Tiers - Tier 2](../../data/enforcement_tiers.yaml)

**Framework Terms:**
- Four-Pillar Architecture → [Four-Pillar Architecture](../strategic/four_pillars.md)
- Enforcement Tiers → [Enforcement Tiers](../../data/enforcement_tiers.yaml)
- Logic Gates → [Logic Gates](../../data/logic_gates.yaml)
- Evidence Classes → [Evidence Classification](../../data/evidence_classification.yaml)

---

## Usage Guidelines

### First Use

On first use in a document:
- Spell out abbreviations (e.g., "Child Sexual Abuse Material (CSAM)")
- Provide full definitions for technical terms
- Link to relevant documentation

### Consistency

- Use preferred terms consistently
- Avoid mixing terminology variants
- Update terminology when system evolves

### Cross-References

- Link to this glossary from all major documents
- Update cross-references when terminology changes
- Maintain consistency across all documentation

---

## Related Documents

- [SRD_DSKB.yaml](../../plans/SRD_DSKB.yaml) - Source definitions and terms of art
- [MUDP Philosophy](../strategic/mudp_philosophy.md) - Core concepts
- [Four-Pillar Architecture](../strategic/four_pillars.md) - System architecture
- [Logic Gates](../../data/logic_gates.yaml) - Scenario categorization
- [Evidence Classification](../../data/evidence_classification.yaml) - Evidence strength
- [Stakeholders](../../data/stakeholders.yaml) - Stakeholder definitions

---

**Last Updated:** 2025-12-23  
**Version:** 1.0

