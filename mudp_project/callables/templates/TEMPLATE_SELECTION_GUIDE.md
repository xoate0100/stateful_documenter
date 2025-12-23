# Template Selection Guide

**Purpose:** Decision tree and selection guide for choosing the appropriate template variant based on scenario characteristics.

**Last Updated:** [DATE]  
**Version:** 1.0

---

## Overview

This guide provides a systematic approach to selecting the correct template variant based on:
- **Logic Gates (LG_01A through LG_06):** Scenario categorization
- **Evidence Classes (E1 through E5):** Evidence strength and type
- **Citation Modes (Mode A/B):** Jurisdiction-agnostic vs. jurisdiction-specific
- **Escalation Tiers (T1 through T7):** Response level required
- **Stakeholders:** Target recipient of the document

---

## Step 1: Identify Logic Gates

**Logic gates categorize the scenario type. Multiple gates may apply simultaneously.**

### LG_01A: Explicit Minor Sexual Depiction

**Applies When:**
- Content explicitly depicts sexual conduct involving a minor
- Content meets legal definition of CSAM (Child Sexual Abuse Material)
- Content violates federal child protection statutes

**Template Implications:**
- High-risk language required
- Mandatory reporting preservation note
- Strong legal claims (CSAM, child protection violations)
- Criminal reporting considerations

**Common Combinations:**
- LG_01A + LG_02 (Explicit + Recognizable Likeness)
- LG_01A + LG_04 (Explicit + Education Context)
- LG_01A + LG_05 (Explicit + Platform Notice)
- LG_01A + LG_06 (Explicit + Biometric Processing)

### LG_01B: Sexualized Non-Explicit

**Applies When:**
- Content sexualizes a minor but is not explicitly sexual
- Content is suggestive, provocative, or inappropriate
- Content may violate civil laws but not necessarily criminal

**Template Implications:**
- Civil framework language
- Professional tone
- Privacy and right of publicity claims
- Less urgent than LG_01A

**Common Combinations:**
- LG_01B + LG_02 (Non-Explicit + Recognizable Likeness)
- LG_01B + LG_03 (Non-Explicit + Economic Expectancy)
- LG_01B + LG_04 (Non-Explicit + Education Context)

### LG_01C: Age Ambiguous

**Applies When:**
- Content may involve a minor but age is ambiguous
- Conservative approach requires treating as minor
- Age verification is uncertain

**Template Implications:**
- Conservative acknowledgment
- Age clarification note (if applicable)
- Professional tone
- Moderate urgency

**Common Combinations:**
- LG_01C + LG_02 (Age Ambiguous + Recognizable Likeness)
- LG_01C + LG_03 (Age Ambiguous + Economic Expectancy)

### LG_02: Recognizable Likeness

**Applies When:**
- Child's likeness is recognizable through:
  - Reasonable observer identification
  - Biometric similarity above threshold
  - Claimed or implied identity

**Template Implications:**
- Assert likeness recognition
- Use biometric evidence appropriately
- Claim right of publicity
- Privacy tort theories
- **Note:** LG_02 often combines with other gates to enhance claims

**Common Combinations:**
- LG_01A + LG_02 (Explicit + Likeness)
- LG_01B + LG_02 (Non-Explicit + Likeness)
- LG_02 + LG_03 (Likeness + Economic)
- LG_02 + LG_06 (Likeness + Biometric)

### LG_03: Economic Expectancy

**Applies When:**
- Preexisting contract or valuation exists
- Plausible devaluation or termination event
- Economic value is documented

**Template Implications:**
- Assert contractual relationship
- Claim quantifiable damages
- Avoid speculative language
- Document economic value
- Tortious interference claims

**Common Combinations:**
- LG_01A + LG_03 (Explicit + Economic)
- LG_01B + LG_03 (Non-Explicit + Economic)
- LG_02 + LG_03 (Likeness + Economic)

### LG_04: Education Context

**Applies When:**
- School-connected actors or context
- Incident involves school environment
- Title IX obligations triggered

**Template Implications:**
- Assert Title IX obligations
- Mandatory reporter analysis
- District liability theories
- Student safety focus
- **Note:** LG_04 often triggers mandatory Tier 2 activation if not resolved at Tier 1

**Common Combinations:**
- LG_01A + LG_04 (Explicit + School)
- LG_01B + LG_04 (Non-Explicit + School)
- LG_02 + LG_04 (Likeness + School)

### LG_05: Platform Notice

**Applies When:**
- Credible notice has been delivered to platform
- Platform is on notice of content
- Time-sensitive fact-dependent immunity analysis

**Template Implications:**
- Assert preservation obligations
- Time-sensitive language
- Compliance urgency
- **Do not assert immunity waiver as fact**

**Common Combinations:**
- LG_01A + LG_05 (Explicit + Platform Notice)
- LG_01B + LG_05 (Non-Explicit + Platform Notice)
- LG_02 + LG_05 (Likeness + Platform Notice)
- LG_06 + LG_05 (Biometric + Platform Notice)

### LG_06: Biometric Processing

**Applies When:**
- Biometric data processing or derivation without parental consent
- Facial recognition, embeddings, or biometric identifiers created
- Biometric privacy regime violations

**Template Implications:**
- Assert biometric privacy violations
- Demand embedding deletion
- Statutory penalty theories
- Cross-jurisdiction considerations (GDPR-like, BIPA, etc.)

**Common Combinations:**
- LG_01A + LG_06 (Explicit + Biometric)
- LG_01B + LG_06 (Non-Explicit + Biometric)
- LG_02 + LG_06 (Likeness + Biometric)
- LG_05 + LG_06 (Platform Notice + Biometric)

---

## Step 2: Classify Evidence

**Evidence classes determine language strength and what can be claimed.**

### E1: Direct Evidence

**Characteristics:**
- Original files, device copies, platform records
- Direct proof of content and distribution
- Strongest evidence class

**Language Strength:**
- **Strong language:** Definitive statements appropriate
- **Actor Identification:** Can identify actor if evidence supports
- **Claims:** Strong legal claims possible
- **Examples:** "The evidence demonstrates...", "This definitively shows..."

**Usage:**
- Use when you have direct access to content files
- Use when platform has confirmed content
- Use when device evidence is available

### E2: Platform Confirmations

**Characteristics:**
- Platform response, takedown acknowledgment, account action notice
- Official documentation from platforms or institutions
- Authoritative but not direct file access

**Language Strength:**
- **Strong language:** Authoritative statements appropriate
- **Actor Identification:** Can identify actor if platform confirms
- **Claims:** Strong attribution claims possible
- **Examples:** "Platform records confirm...", "Official documentation shows..."

**Usage:**
- Use when platform has responded or confirmed
- Use when institutional records are available
- Use when official documentation exists

### E3: Derived Similarity

**Characteristics:**
- SHA-256 match, perceptual hash similarity, embedding similarity
- Technical forensics showing derivation
- Technical evidence of similarity

**Language Strength:**
- **Moderate language:** Technical similarity claims
- **Actor Identification:** **Cannot identify actor** without correlating evidence
- **Claims:** Can support derivation and likeness claims
- **Examples:** "Technical evidence suggests...", "Hash comparison shows..."

**Usage:**
- Use when technical analysis shows similarity
- Use when hash comparisons are available
- Use when embedding similarity is detected
- **Do not identify actor** based on E3 alone

### E4: Testimonial

**Characteristics:**
- Witness statements, parent reports, teacher reports, student reports
- Third-party observations and reports
- Testimonial information

**Language Strength:**
- **Moderate language:** Reported information language
- **Actor Identification:** Conditional (only if witness has direct knowledge)
- **Claims:** Can support claims, may require corroboration
- **Examples:** "Reports indicate...", "Witnesses state...", "According to reports..."

**Usage:**
- Use when witness statements are available
- Use when reports from third parties exist
- Use when testimonial evidence is primary source
- Verify witness statements before sending

### E5: Contextual

**Characteristics:**
- Pattern of harassment, timeline inference, circumstantial evidence
- Behavioral patterns, contextual indicators
- Weakest evidence class

**Language Strength:**
- **Weak/Suggestive language:** Pattern and circumstantial claims
- **Actor Identification:** **Cannot identify actor** - E5 cannot identify actor
- **Claims:** Can support pattern claims, limits asserted certainty
- **Examples:** "Patterns suggest...", "Timeline indicates...", "This may indicate..."

**Usage:**
- Use when only circumstantial evidence is available
- Use when patterns suggest but don't prove
- Use when timeline inference is primary evidence
- **Do not identify actor** - E5 evidence insufficient
- **Does NOT limit preservation or removal requests**

---

## Step 3: Determine Citation Mode

### Mode A: Jurisdiction-Agnostic

**Use When:**
- Jurisdiction is unknown or may vary
- Multi-jurisdiction scenarios
- Default mode for most templates
- General legal principles apply

**Characteristics:**
- Avoids specific statutory citations
- Uses general legal framework language
- Applicable across jurisdictions
- May reference "applicable federal and state laws"

**Template Location:**
- `mode_a/` subdirectory

### Mode B: Jurisdiction-Specific

**Use When:**
- Specific jurisdiction is known (e.g., Kansas, Missouri)
- Jurisdiction-specific laws apply
- Statutory citations are required
- State-specific requirements exist

**Characteristics:**
- Includes specific statutory citations
- References state-specific laws
- Uses jurisdiction-specific language
- May include state-specific procedures

**Template Location:**
- `mode_b/[JURISDICTION]/` subdirectory (e.g., `mode_b/kansas/`, `mode_b/missouri/`)

**Available Jurisdictions:**
- Kansas (pending)
- Missouri (pending)
- Additional jurisdictions as needed

---

## Step 4: Determine Escalation Tier

**Escalation tiers determine which template types are needed.**

### Tier 1: Parent-Parent Resolution

**Use When:**
- Initial response to incident
- Direct parent-to-parent communication
- Attempting resolution without institutional involvement
- Most incidents should resolve here

**Template Types:**
- Parent Notice Letters
- Deletion Confirmation Scripts
- Device Sweep Requests

**Success Indicators:**
- Content removed
- Issue resolved
- No further action needed

**Failure Triggers:**
- No response within 24 hours
- Refusal to cooperate
- Continued distribution
- Escalate to Tier 2 or Tier 3

### Tier 2: School Activation

**Use When:**
- Tier 1 fails OR incident involves school context
- School-connected actors or context
- Title IX obligations triggered
- Mandatory reporting required

**Template Types:**
- Title IX Notices
- Safety Plan Requests
- District Legal Notices
- Documentation Requests

**Success Indicators:**
- School takes disciplinary action
- Title IX process initiated
- District legal review
- Student safety measures implemented

**Failure Triggers:**
- School delays or downplays
- Failure to follow mandatory reporting
- Inadequate disciplinary action
- Escalate to Tier 4 (Insurance before Platform)

### Tier 3: Platform Removal

**Use When:**
- Content on platforms/apps
- Tier 1-2 insufficient
- Platform removal required
- CSAM compliance needed

**Template Types:**
- Urgent Removal Requests
- Preservation Notices
- Repeat Upload Suppression Requests

**Success Indicators:**
- Content removed within hours
- Account suspended/deleted
- Platform compliance
- Evidence preserved

**Failure Triggers:**
- Platform delays removal
- Inadequate response
- Continued availability
- Escalate to Tier 4 or Tier 5

### Tier 4: Insurance Activation

**Use When:**
- Tiers 1-3 insufficient OR concurrent with Tier 2-3
- Liability exposure exists
- Insurance coverage may apply
- Financial leverage needed

**Template Types:**
- Carrier Incident Notices
- Coverage Trigger Memos
- Risk Mitigation Demands

**Success Indicators:**
- Insurance carrier involvement
- Immediate remediation push
- Coverage confirmed
- Legal cost support

**Failure Triggers:**
- Coverage denial
- Carrier delays
- Inadequate coverage
- Escalate to Tier 5

### Tier 5: Civil Litigation

**Use When:**
- Tiers 1-4 insufficient
- Ongoing harm
- Egregious conduct
- Legal action required

**Template Types:**
- Complaint Outlines
- Injunction Motion Outlines
- Discovery Plans
- Spoliation Letters

**Success Indicators:**
- Legal counsel engaged
- Formal demands sent
- Strong legal position
- Settlement negotiations

**Failure Triggers:**
- Ongoing harm
- Refusal to settle
- Egregious conduct
- Escalate to Tier 6

### Tier 6: Regulatory Complaints

**Use When:**
- Platform/institution failures
- Regulatory violations
- Consumer protection concerns
- Administrative enforcement needed

**Template Types:**
- Attorney General Complaints
- FTC Complaints
- Privacy Authority Notices

**Success Indicators:**
- Regulatory complaint filed
- Investigation initiated
- Compliance required
- Remedies obtained

**Failure Triggers:**
- Regulatory inaction
- Insufficient remedies
- Ongoing violations
- Escalate to Tier 7

### Tier 7: Appellate and Constitutional

**Use When:**
- Lower court adverse decisions
- Constitutional violations
- Need for appellate review
- Federal appellate review required

**Template Types:**
- Constitutional Issue Preservation Memos
- Appeal Theory Outlines
- Record Build Plans

**Success Indicators:**
- Constitutional issues preserved
- Appeal filed
- Appellate review obtained
- Constitutional arguments advanced

**Failure Triggers:**
- Issues not preserved
- Appeal denied
- Constitutional arguments rejected
- Final resolution

---

## Step 5: Identify Stakeholders

**Stakeholders determine the target recipient and tone of the document.**

### Common Stakeholders

- **Custodial Parent:** Primary decision-maker
- **Opposing Parent:** Tier 1 target
- **School District:** Tier 2 target (Title IX Coordinator, District Legal)
- **Platform/App:** Tier 3 target (Legal, Trust & Safety)
- **Insurance Carrier:** Tier 4 target (Claims Department)
- **Court:** Tier 5-7 target (Trial Court, Appellate Court)
- **Regulatory Agencies:** Tier 6 target (Attorney General, FTC, Privacy Authority)

---

## Decision Tree Example

**Scenario:** Explicit minor sexual depiction content on social media platform, recognizable likeness, school context, direct evidence available, jurisdiction unknown.

**Step 1: Logic Gates**
- LG_01A (Explicit Minor Sexual Depiction) ✓
- LG_02 (Recognizable Likeness) ✓
- LG_04 (Education Context) ✓
- LG_05 (Platform Notice) ✓ (if notice delivered)

**Step 2: Evidence Class**
- E1 (Direct Evidence) ✓

**Step 3: Citation Mode**
- Mode A (Jurisdiction-Agnostic) ✓

**Step 4: Escalation Tier**
- Start with Tier 1 (Parent-Parent Resolution)
- If fails, escalate to Tier 2 (School Activation) - mandatory due to LG_04
- Also activate Tier 3 (Platform Removal) - content on platform

**Step 5: Stakeholders**
- Tier 1: Opposing Parent
- Tier 2: School District (Title IX Coordinator, District Legal)
- Tier 3: Platform (Legal, Trust & Safety)

**Selected Templates:**
- `tier_1_parent_resolution/parent_notice/mode_a/parent_notice_lg01a_lg02_lg04_e1_modea_t1.md` (if combined template exists)
- OR: `parent_notice_lg01a_e1_modea_t1.md` (primary gate) + note other gates
- `tier_2_school_activation/title_ix_notice/mode_a/title_ix_notice_lg04_e1_modea_t2.md`
- `tier_3_platform_removal/urgent_removal_request/mode_a/urgent_removal_request_lg01a_lg05_e1_modea_t3.md`

---

## Template Naming Convention

**Format:** `[template_type]_[logic_gates]_[evidence_class]_[citation_mode]_[tier].md`

**Examples:**
- `parent_notice_lg01a_e1_modea_t1.md` - Single logic gate
- `parent_notice_lg01a_lg02_e1_modea_t1.md` - Combined logic gates
- `title_ix_notice_lg04_e2_modea_t2.md` - Tier 2, E2 evidence
- `urgent_removal_request_lg01a_lg05_e1_modeb_kansas_t3.md` - Mode B, Kansas

**Logic Gate Combinations:**
- Multiple gates separated by underscores: `lg01a_lg02_lg04`
- Order: Primary gate first, then supporting gates

---

## Quick Reference Matrix

| Logic Gate | Primary Use | Common Combinations | Tier Trigger |
|------------|-------------|---------------------|--------------|
| LG_01A | Explicit CSAM | LG_02, LG_04, LG_05, LG_06 | All tiers |
| LG_01B | Non-explicit sexualization | LG_02, LG_03, LG_04 | T1-T6 |
| LG_01C | Age ambiguous | LG_02, LG_03 | T1-T5 |
| LG_02 | Recognizable likeness | LG_01A, LG_01B, LG_03, LG_06 | All tiers |
| LG_03 | Economic expectancy | LG_01A, LG_01B, LG_02 | T1-T5 |
| LG_04 | Education context | LG_01A, LG_01B | **T2 mandatory** |
| LG_05 | Platform notice | LG_01A, LG_01B, LG_02, LG_06 | T3 |
| LG_06 | Biometric processing | LG_01A, LG_01B, LG_02, LG_05 | T1-T6 |

| Evidence Class | Language Strength | Actor ID | Usage |
|----------------|-------------------|----------|-------|
| E1 | Strong | Yes (if supported) | Direct files, platform records |
| E2 | Strong | Yes (if platform confirms) | Platform confirmations |
| E3 | Moderate | **No** | Technical similarity |
| E4 | Moderate | Conditional | Testimonial reports |
| E5 | Weak/Suggestive | **No** | Contextual patterns |

---

## Important Notes

1. **Multiple Logic Gates:** Many scenarios involve multiple logic gates. Use the primary gate for template selection, but incorporate all applicable gates in the document.

2. **Evidence Class Limitations:** E3, E4, and E5 have limitations on actor identification. Always respect these limitations.

3. **Escalation Path:** Not all incidents require all tiers. Most should resolve at Tier 1. Escalate only when necessary.

4. **Mode Selection:** Default to Mode A unless specific jurisdiction is known and Mode B templates exist.

5. **Template Customization:** All templates require customization with actual facts and information. Templates are frameworks, not final documents.

6. **Legal Review:** All templates should be reviewed by licensed attorneys before use. Templates are planning tools, not legal advice.

---

## Related Documents

- [Logic Gates](../../data/logic_gates.yaml)
- [Evidence Classification](../../data/evidence_classification.yaml)
- [Enforcement Tiers](../../data/enforcement_tiers.yaml)
- [Citation Modes](../../docs/legal/citation_modes.md)
- [Drafting Rules](../../docs/legal/drafting_rules.md)
- [Template Index](./TEMPLATE_INDEX.md)
- [UNIFIED_PROTOCOL](../../UNIFIED_PROTOCOL.md)

---

## Version History

- **v1.0** - Initial version with all 7 tiers and 6 logic gates documented

