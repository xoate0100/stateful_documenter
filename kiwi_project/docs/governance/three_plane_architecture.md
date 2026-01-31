# Three-Plane Architecture

**Source:** `kiwi_ingestion.txt` lines 28-94  
**Status:** Core Architecture  
**Last Updated:** 2025-01-14

---

## Overview

The Three-Plane Architecture is the backbone of Kiwi's governance system. It separates concerns into three distinct planes: Governance (the Constitution), Control (Rules → Enforcement), and Execution (Where Games Live). This separation prevents the failures that plague platforms like Roblox.

---

## The Three Planes

```
┌─────────────────────────────────────┐
│   Governance Plane (Constitution)   │
│   Defines: What, Who, How           │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   Control Plane (Enforcement)       │
│   Translates: Rules → Constraints   │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   Execution Plane (Games/Creators)  │
│   Provides: Sandboxed Tools         │
└─────────────────────────────────────┘
```

---

## 1. Governance Plane (The Constitution)

### Purpose

Defines what is allowed, who has power, and how rules change.

### Participants

- **Parents Council** (elected, rotating)
- **Creators Council** (tiered by contribution, not revenue)
- **Moderators Guild** (paid + credentialed)
- **Platform Stewards** (employees, limited voting power)
- **Child Safety Ombudsman** (independent, veto power)

**Investors explicitly excluded from governance voting.**

### Powers

- Set safety thresholds
- Approve monetization categories
- Define age-tier permissions
- Approve changes to moderation standards
- Trigger audits
- Veto incentive changes that create harm

### Structural Lock

**Any rule change affecting minors requires 2-chamber approval:**
- Parents + Moderators, OR
- Parents + Ombudsman

This alone prevents Roblox-style drift.

### Why This Matters

Roblox failed because governance was captured by investors and revenue optimization. Kiwi's governance plane ensures that:
- Safety decisions require parent + safety expert approval
- Revenue optimization cannot override safety
- Multiple stakeholders must agree on changes affecting children
- No single actor can dominate decision-making

---

## 2. Control Plane (Rules → Enforcement)

### Purpose

Translate governance into machine-enforced constraints.

**This is where Roblox failed.**

Instead of policy docs, we use enforced capability boundaries.

### Examples

- A 9-year-old cannot technically receive DMs from anyone outside their whitelisted social graph
- A game flagged as "economically manipulative" cannot enable microtransactions, period
- Age tiers determine which APIs exist, not just settings

### Parent Controls (Granular & Incentivized)

Parents get:
- **Economic controls:** Spend caps, cooldowns, transaction categories
- **Social controls:** Who can talk, how, when
- **Time topology:** Time-of-day + duration logic
- **Escalation paths:** Priority review for issues involving their child

**Incentive:** Parents who engage with controls earn:
- Fee rebates
- Platform credits
- Voting weight boosts (within limits)

**Engaged parents = safer platform.**

### Why This Matters

Roblox had "parental controls" but they were:
- Buried in settings
- Easy to bypass
- Not incentivized
- Not connected to platform safety metrics

Kiwi's control plane makes safety controls:
- Visible and accessible
- Architecturally enforced (not just settings)
- Economically incentivized
- Directly connected to platform health

---

## 3. Execution Plane (Where Games Live)

### Purpose

Let creators build without endangering users or the ecosystem.

### Key Principle

**Creators never touch raw social power.**

They interact only with mediated systems:
- Structured chat
- Predefined interaction patterns
- Sandboxed economies

This prevents accidental or malicious harm.

### What Creators Get

- Game development tools
- Asset creation systems
- Economy tools (within constraints)
- Discovery mechanisms
- Analytics (aggregated, privacy-preserving)

### What Creators Don't Get

- Direct access to user social graphs
- Unmediated communication channels
- Unrestricted monetization
- User identity data
- Behavioral tracking for manipulation

### Why This Matters

Roblox gave creators too much power, leading to:
- Predatory games
- Social manipulation
- Economic exploitation
- Safety incidents

Kiwi's execution plane ensures creators can be creative and successful while being structurally prevented from causing harm.

---

## How the Planes Interact

### Governance → Control

Governance Plane sets rules:
- "Minors under 13 cannot receive DMs from non-whitelisted users"

Control Plane enforces it:
- API-level restrictions
- Database constraints
- Permission checks

### Control → Execution

Control Plane defines capabilities:
- "This game is flagged as high-engagement, must include cooldown nudges"

Execution Plane provides tools:
- Cooldown nudge API
- Playtime awareness widgets
- Break reminders

### Execution → Governance

Execution Plane generates data:
- Safety incident reports
- Moderation metrics
- Trust signals

Governance Plane uses data:
- Adjusts safety thresholds
- Updates moderation standards
- Triggers audits

---

## Why This Architecture Prevents Enshittification

### Traditional Platforms

1. Revenue optimization drives decisions
2. Safety is retrofitted
3. Governance is captured
4. Trust erodes
5. Platform dies

### Kiwi's Three-Plane Architecture

1. Governance sets safety-first rules
2. Control enforces them structurally
3. Execution provides safe creative tools
4. Trust compounds
5. Platform improves

### The Virtuous Cycle

```
Safer defaults
    ↓
Parent trust increases
    ↓
Better kids + better creators join
    ↓
Less moderation load per user
    ↓
Moderators improve quality, not firefighting
    ↓
Discovery trust improves
    ↓
Less clone spam, more originality
    ↓
Platform reputation strengthens
    ↓
Lower external fees + regulatory pressure
    ↓
More resources reinvested into safety & quality
```

---

## Related Documentation

- [Governance Plane](./governance_plane.md) - Detailed governance structure
- [Control Plane](../technical/control_plane.md) - Technical enforcement mechanisms
- [Execution Plane](../technical/execution_plane.md) - Creator tools and APIs
- [First Principles](../strategic/first_principles.md) - Axioms that inform this architecture

---

**Next:** [Governance Plane](./governance_plane.md)
