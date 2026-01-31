# Governance Plane (The Constitution)

**Source:** `kiwi_ingestion.txt` lines 30-51, 287-405  
**Status:** Core Governance  
**Last Updated:** 2025-01-14

---

## Overview

The Governance Plane is the constitutional layer of Kiwi. It defines what is allowed, who has power, and how rules change. This is where the platform's values and safety requirements are codified into structural rules that cannot be easily overridden.

---

## Core Participants

### Parents Council
- **Structure:** Elected, rotating
- **Purpose:** Represent parent interests and child safety concerns
- **Power:** Veto authority on changes affecting minors
- **Selection:** Parents who actively engage with controls and platform governance

### Creators Council
- **Structure:** Tiered by contribution, not revenue
- **Purpose:** Represent creator interests and creative ecosystem health
- **Power:** Input on monetization policies, discovery algorithms, creator tools
- **Selection:** Based on contribution quality, originality, and community impact (not revenue)

### Moderators Guild
- **Structure:** Paid + credentialed professionals
- **Purpose:** Represent moderation expertise and platform safety
- **Power:** Set moderation standards, approve safety protocols
- **Selection:** Professional moderators with proven track records

### Platform Stewards
- **Structure:** Employees, limited voting power
- **Purpose:** Represent operational and technical feasibility
- **Power:** Advisory role, limited voting on technical matters
- **Selection:** Platform employees in governance roles

### Child Safety Ombudsman
- **Structure:** Independent, veto power
- **Purpose:** Ultimate authority on child safety matters
- **Power:** Veto authority on any decision affecting child safety
- **Selection:** Independent expert, appointed by multi-chamber consensus

### Investors
- **Status:** **Explicitly excluded from governance voting**
- **Role:** Capital providers only, no governance authority
- **See:** [Investor Sandboxing](./investor_sandboxing.md)

---

## Powers and Responsibilities

### Setting Safety Thresholds
- Define acceptable risk levels for different age groups
- Set moderation response time requirements
- Establish escalation protocols
- Define "red line" metrics that trigger automatic freezes

### Approving Monetization Categories
- Classify transaction types (cosmetics, loot boxes, subscriptions, etc.)
- Set age-tier restrictions on monetization
- Approve new monetization mechanisms
- Review economic manipulation risks

### Defining Age-Tier Permissions
- Establish capability boundaries for each age tier
- Define social interaction permissions
- Set content creation limits
- Determine economic participation levels

### Approving Changes to Moderation Standards
- Review moderation policy changes
- Approve new moderation tools and processes
- Set moderator training requirements
- Establish appeals processes

### Triggering Audits
- Request platform-wide safety audits
- Trigger economic system reviews
- Initiate governance effectiveness assessments
- Commission external reviews

### Vetoing Incentive Changes
- Block changes that create harm
- Prevent revenue optimization that erodes trust
- Stop feature launches that compromise safety
- Halt initiatives that violate First Principles

---

## Structural Locks

### Two-Chamber Approval for Minors

**Any rule change affecting minors requires 2-chamber approval:**
- Parents + Moderators, OR
- Parents + Ombudsman

This prevents:
- Revenue-driven changes that compromise child safety
- Single-chamber capture of child safety decisions
- Rapid changes without proper consideration

### Example Scenarios

**Scenario 1: New Monetization Feature**
- Governance must approve the feature category
- If it affects minors: Parents + Moderators must both approve
- Control Plane enforces age restrictions
- Execution Plane provides tools within constraints

**Scenario 2: Moderation Policy Change**
- Moderators propose change
- Parents review for child safety impact
- If affecting minors: Parents + Ombudsman must approve
- Control Plane implements enforcement

**Scenario 3: Age-Tier Permission Update**
- Governance reviews proposed change
- Parents + Moderators must both approve (always affects minors)
- Control Plane updates capability boundaries
- Execution Plane adapts available tools

---

## The Six Chambers of Power

Beyond the core governance participants, Kiwi recognizes six formalized chambers that acknowledge and civilize human drives:

### 1. Adult Social Chamber
- **Purpose:** Explicit adult social zones (dating, identity, desire)
- **Structure:** 18+ verified layer, separate infrastructure
- **Principle:** Contain adult behavior, don't suppress it

### 2. Attention Economy Chamber
- **Purpose:** Licensed dopamine design (engagement mechanics)
- **Structure:** Classification system, mandatory counterweights
- **Principle:** Acknowledge attention-hacking, then civilize it

### 3. Capital Chamber
- **Purpose:** Investor interests (contained)
- **Structure:** Profit rights ≠ governance rights
- **Principle:** Capital gets returns, not control

### 4. Economic Realists Chamber
- **Purpose:** Microtransactions (civilized)
- **Structure:** Transaction ethics matrix
- **Principle:** Revenue remains high, but trust compounds

### 5. Education & Culture Chamber
- **Purpose:** Cultural literacy and norms
- **Structure:** Platform education system
- **Principle:** Turn awareness into status

### 6. Edge Behavior Chamber
- **Purpose:** Scammers, griefers, hackers
- **Structure:** Bug bounties, redemption paths
- **Principle:** Convert enemies into auditors

**See:** [Chambers of Power](./chambers_of_power.md) for detailed documentation

---

## Decision-Making Process

### Standard Process
1. Proposal submitted to relevant chamber(s)
2. Impact assessment (safety, trust, economic)
3. Multi-chamber review
4. Approval/veto decision
5. Control Plane implementation
6. Execution Plane tooling
7. Monitoring and feedback loop

### Emergency Process
- Ombudsman can trigger immediate freeze
- Safety red lines trigger automatic holds
- Rapid response protocol for critical incidents

### Appeals Process
- Decisions can be appealed to multi-chamber review
- Ombudsman has final authority on safety matters
- External review available for governance disputes

---

## Why This Prevents Roblox-Style Drift

### Roblox's Failure
- Investors controlled narrative
- Revenue optimization overrode safety
- Governance was captured
- Safety was retrofitted, not structural
- Single points of failure

### Kiwi's Governance Plane
- Multiple chambers with distinct powers
- Structural locks prevent single-actor control
- Safety requires multi-chamber approval
- Investors explicitly excluded
- Constitutional structure prevents drift

---

## Related Documentation

- [Three-Plane Architecture](./three_plane_architecture.md) - How Governance fits into overall architecture
- [Chambers of Power](./chambers_of_power.md) - Detailed chamber structures
- [Investor Sandboxing](./investor_sandboxing.md) - Limits on capital influence
- [First Principles](../strategic/first_principles.md) - Axioms that inform governance

---

**Next:** [Control Plane](../technical/control_plane.md)
