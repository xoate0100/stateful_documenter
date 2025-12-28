# Jurisdiction Overlay Creation Guide

**Purpose:** Step-by-step guide for creating jurisdiction-specific overlays for Mode B template generation

**Status:** Active Documentation

---

## Overview

Jurisdiction overlays provide jurisdiction-specific legal information required for Mode B (jurisdiction-specific) template generation. They contain:

- State-specific statute citations
- Legal framework information
- Court rules
- Jurisdiction-specific terminology
- Template generation requirements

---

## Creation Process

### Step 1: Copy Template

1. Copy `OVERLAY_TEMPLATE.yaml`
2. Rename to `[jurisdiction].yaml` (e.g., `kansas.yaml`, `missouri.yaml`)
3. Place in `callables/jurisdiction_overlays/` directory

### Step 2: Fill Basic Information

```yaml
jurisdiction: "Kansas"
state_code: "KS"
country: "United States"
effective_date: "2025-12-23"
last_verified: "2025-12-23"
```

### Step 3: Research State Statutes

Research and document state-specific statutes for:

1. **Child Protection**
   - Sexual exploitation of minors
   - Mandatory reporting requirements
   - Child abuse statutes

2. **Right of Publicity**
   - State right of publicity statute (if exists)
   - Common law right of publicity (if no statute)
   - Post-mortem rights
   - Duration of rights

3. **Privacy Torts**
   - Invasion of privacy statutes
   - False light statutes
   - Intrusion upon seclusion

4. **Defamation**
   - Defamation statutes
   - Per se defamation categories
   - Defenses and privileges

5. **Consumer Protection**
   - Deceptive practices statutes
   - Unfair practices statutes
   - Consumer protection acts

6. **Biometric Privacy**
   - BIPA equivalent (if exists)
   - Biometric data protection statutes

### Step 4: Document Legal Frameworks

Document applicability of:

- **Title IX:** Federal law, applies in all states
- **FERPA:** Federal law, applies in all states
- **Mandatory Reporting:** State-specific requirements
- **Biometric Privacy:** State-specific (if applicable)
- **Right of Publicity:** State-specific (statute or common law)

### Step 5: Document Court Rules

Research and document:

- Filing requirements
- Service requirements
- Local court rules (if applicable)

### Step 6: Document Terminology

Document:

- Preferred terms for jurisdiction
- Terms to avoid
- Legal terms of art specific to jurisdiction

### Step 7: Validation

Complete validation checklist:

- [ ] All statute citations verified for accuracy
- [ ] All statute citations verified for currency
- [ ] Legal frameworks verified
- [ ] Court rules verified
- [ ] Terminology verified
- [ ] Legal review completed
- [ ] Overlay tested with sample template

---

## Research Resources

### State Statutes

- State legislature websites
- State code databases
- Legal research databases (Westlaw, LexisNexis)
- State bar association resources

### Court Rules

- State court websites
- State court rules databases
- Local court rules (if applicable)

### Legal Frameworks

- State attorney general opinions
- Case law summaries
- Legal treatises
- State bar publications

---

## Quality Assurance

### Citation Accuracy

- Verify all statute numbers are correct
- Verify statute names are accurate
- Check for recent amendments or repeals
- Verify effective dates

### Currency

- Check for recent legislative changes
- Verify statutes are still in effect
- Check for pending legislation
- Update effective dates

### Completeness

- Ensure all relevant statutes are included
- Ensure all legal frameworks are documented
- Ensure court rules are complete
- Ensure terminology is comprehensive

### Legal Review

- Have qualified legal counsel review overlay
- Verify citations are appropriate for use
- Ensure compliance with legal requirements
- Confirm terminology is accurate

---

## Template Generation Integration

### Mode B Template Requirements

When generating Mode B templates using overlay:

1. **Include Statute Citations**
   - Use exact citations from overlay
   - Follow citation format specified in overlay
   - Include statute names

2. **Use Jurisdiction-Specific Terminology**
   - Use preferred terms from overlay
   - Avoid terms listed in avoided_terms
   - Use legal terms of art appropriately

3. **Follow State-Specific Requirements**
   - Reference mandatory reporting requirements
   - Include state-specific legal frameworks
   - Follow court rules if applicable

4. **Maintain Professional Tone**
   - Follow drafting rules
   - Maintain crisis management professional tone
   - Use appropriate language strength

---

## Maintenance

### Regular Updates

- Review overlays annually
- Update for legislative changes
- Update for court rule changes
- Update effective dates

### Version Control

- Track overlay versions
- Document changes
- Maintain change log
- Archive old versions

### Validation

- Re-validate citations periodically
- Re-verify legal frameworks
- Re-check court rules
- Update terminology as needed

---

## Related Documents

- [Citation Modes](../../docs/legal/citation_modes.md) - Mode A/B system
- [Overlay Template](./OVERLAY_TEMPLATE.yaml) - Template structure
- [Regulatory Matrix](../../data/regulatory_matrix.yaml) - State law matrix
- [Drafting Rules](../../docs/legal/drafting_rules.md) - Template drafting requirements

---

## Notes

- All overlays must be reviewed by qualified legal counsel
- Statute citations must be verified for accuracy and currency
- Overlays are for template generation only, not legal advice
- Users must verify citations before using in legal documents

---

**Last Updated:** 2025-12-23  
**Version:** 1.0



