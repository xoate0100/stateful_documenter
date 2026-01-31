# Control Plane (Rules → Enforcement)

**Source:** `kiwi_ingestion.txt` lines 53-78  
**Status:** Core Technical Architecture  
**Last Updated:** 2025-01-14

---

## Overview

The Control Plane translates governance into machine-enforced constraints. This is where Roblox failed—instead of policy docs, Kiwi uses enforced capability boundaries.

**Core Principle:** Rules are not suggestions. They are architectural constraints.

---

## Purpose

Translate governance into machine-enforced constraints.

**This is where Roblox failed.**

Instead of policy docs, we use enforced capability boundaries.

---

## Examples of Enforced Constraints

### Example 1: Age-Based DM Restrictions
- **Governance Rule:** "Minors under 13 cannot receive DMs from non-whitelisted users"
- **Control Plane Enforcement:**
  - API-level restrictions
  - Database constraints prevent non-whitelisted DMs
  - UI prevents DM initiation
  - Cannot be bypassed by settings

### Example 2: Economic Manipulation Prevention
- **Governance Rule:** "Games flagged as economically manipulative cannot enable microtransactions"
- **Control Plane Enforcement:**
  - Game economy API checks flag status
  - Transaction system blocks flagged games
  - Cannot be overridden by creators
  - Automatic enforcement, not optional

### Example 3: Age-Tier API Availability
- **Governance Rule:** "Age tiers determine which APIs exist"
- **Control Plane Enforcement:**
  - API endpoints check age tier
  - Unavailable APIs return 403 (not just hidden)
  - Capability boundaries are architectural
  - Settings cannot override

---

## Parent Controls (Granular & Incentivized)

### What Parents Get

#### Economic Controls
- Spend caps (daily, weekly, monthly)
- Cooldowns between transactions
- Transaction category restrictions
- Automatic spending alerts

#### Social Controls
- Who can talk (whitelist, friend-of-friend, open)
- How they can talk (emoji, preset, text, voice)
- When they can talk (time-of-day restrictions)
- Social graph expansion limits

#### Time Topology
- Time-of-day restrictions
- Duration limits
- Break requirements
- Cooldown periods

#### Escalation Paths
- Priority review for issues involving their child
- Direct moderator access
- Expedited support
- Incident notifications

### Incentive System

**Parents who engage with controls earn:**
- Fee rebates (reduced platform fees)
- Platform credits (usable in platform economy)
- Voting weight boosts (within limits, in Parents Council)
- Early access to new safety features

**Engaged parents = safer platform.**

### What Parents Don't Get

**Parents cannot:**
- See chat content (unless flagged for safety)
- View social graphs (privacy-preserving)
- Access identity information
- Monitor private interactions
- Override age-tier restrictions

**This is capability governance, not identity surveillance.**

---

## Enforcement Mechanisms

### API-Level Enforcement

```yaml
# Example: Age-tier API restrictions
enforcement:
  api_checks:
    - age_tier_verification
    - capability_permissions
    - trust_signal_validation
    - context_aware_restrictions
  
  database_constraints:
    - foreign_key_restrictions
    - check_constraints
    - trigger_based_validation
  
  application_logic:
    - permission_checks
    - rate_limiting
    - cooldown_enforcement
```

### Permission Checks

Every API call checks:
1. User's age tier
2. User's trust signals
3. Capability permissions
4. Context (game, social space, etc.)
5. Parent control settings (within age-tier limits)

### Rate Limiting

- Social interactions: Per-hour, per-conversation limits
- Economic transactions: Cooldowns, caps
- Content creation: Graduated access
- Discovery: Trust-based throttling

---

## Integration with Governance Plane

### Governance → Control Flow

1. **Governance sets rule:** "Minors cannot use voice chat"
2. **Control Plane enforces:**
   - API blocks voice chat endpoints for minors
   - UI hides voice chat options
   - Database prevents voice chat records
3. **Execution Plane adapts:**
   - Creators see voice chat is unavailable for minors
   - Alternative communication tools provided

### Control → Execution Flow

1. **Control Plane defines capabilities:** "This game is high-engagement, must include cooldown nudges"
2. **Execution Plane provides tools:**
   - Cooldown nudge API
   - Playtime awareness widgets
   - Break reminder system
3. **Creators use tools:**
   - Required integration for high-engagement games
   - Optional for other games
   - Discovery algorithm favors games with safety features

---

## Why This Prevents Roblox-Style Failure

### Roblox's Approach
- "Parental controls" were buried in settings
- Easy to bypass
- Not incentivized
- Not connected to platform safety
- Settings-based, not architectural

### Kiwi's Control Plane
- Controls are visible and accessible
- Architecturally enforced (not just settings)
- Economically incentivized
- Directly connected to platform health
- Capability-based, not identity-based

---

## Red Lines and Automatic Freezes

### Constitutional Triggers

If Cultural Ledger metrics drop below thresholds:
- **Harassment per capita rises above X** → Monetization expansion freezes
- **Moderator burnout rises** → Growth initiatives pause
- **Forced-outing risk signals appear** → Immediate audit
- **Compulsive play patterns spike** → Dopamine design review triggered

**This prevents "we'll fix it later" drift.**

---

## Related Documentation

- [Three-Plane Architecture](../governance/three_plane_architecture.md) - How Control Plane fits into overall architecture
- [Safety Architecture](./safety_architecture.md) - Technical safety mechanisms
- [Governance Plane](../governance/governance_plane.md) - Rules that Control Plane enforces
- [Execution Plane](./execution_plane.md) - Tools that Control Plane enables

---

**Next:** [Execution Plane](./execution_plane.md)
