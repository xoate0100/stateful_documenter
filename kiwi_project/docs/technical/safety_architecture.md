# Safety Architecture (Without Surveillance)

**Source:** `kiwi_ingestion.txt` lines 95-136  
**Status:** Core Technical Architecture  
**Last Updated:** 2025-01-14

---

## Overview

Kiwi's safety architecture explicitly rejects biometric child scanning and surveillance-based approaches. Instead, we use Progressive Trust & Capability Unlocking to create safety through friction where it matters, not surveillance.

**Core Principle:** No identity ≠ no safety.

---

## Age-Tiered Accounts

### Tier Structure

- **Child (0–9):** Maximum restrictions, whitelist-only social
- **Tween (10–12):** Moderate restrictions, supervised social
- **Teen (13–15):** Graduated permissions, monitored social
- **Youth (16–17):** Near-adult permissions, self-regulation tools
- **Adult (18+):** Full permissions, separate infrastructure

### Why Age Tiers Matter

Age tiers determine:
- Which APIs exist (not just settings)
- What capabilities are available
- Which social features are accessible
- What economic participation is allowed

This is architectural enforcement, not optional settings.

---

## Capability-Based Permissions

### Chat Modes (Progressive Unlocking)

- **Emoji-only:** Initial stage for youngest users
- **Preset messages:** Pre-approved communication options
- **Limited text:** Filtered, monitored text communication
- **Full text:** Graduated access with trust signals

### Social Graph Expansion

- **Whitelist-only:** For youngest users
- **Friend-of-friend:** Graduated expansion
- **Community-based:** Trusted community access
- **Open (with tools):** Adult-level with self-regulation

### Game Creation Features

- **Template-based:** Start with templates
- **Guided creation:** Step-by-step tools
- **Advanced tools:** Full creator access (with constraints)
- **Economy tools:** Monetization capabilities (age-restricted)

### Economy Access

- **No access:** Youngest users
- **Parent-controlled:** Middle tiers
- **Capped access:** Youth tier
- **Full access:** Adult tier

---

## Trust Signals (Non-Biometric)

### Time on Platform Without Incidents
- Clean record over time
- Graduated trust increases
- Incident-free periods unlock capabilities

### Parental Confirmations
- Parent verification of milestones
- Parent approval for capability unlocks
- Parent engagement with controls

### Moderator-Reviewed Milestones
- Professional review of behavior
- Positive moderation interactions
- Community contribution recognition

### Community Endorsements
- Peer trust ratings (private, non-public)
- Creator recognition
- Helper/mentor status

---

## Escalation Barriers

### No Off-Platform Contact Sharing
- Cannot share external contact information
- Cannot link to external social media
- Cannot exchange personal identifiers

### No Private Voice for Minors
- Voice chat requires public spaces or parent approval
- No private voice channels for minors
- Voice moderation is mandatory

### No "Dating" Affordances at All
- No dating features for minors
- No romantic interaction tools
- No relationship status features

### Age Verification Barriers
- Cannot access adult content
- Cannot join adult social spaces
- Cannot use adult economic features

---

## Progressive Trust Model

### How It Works

1. **Start with Maximum Safety:** All users begin with maximum restrictions
2. **Earn Trust Signals:** Time, behavior, confirmations build trust
3. **Unlock Capabilities:** Trust signals unlock new features
4. **Maintain Trust:** Incidents reduce trust, require rebuilding
5. **Graduated Access:** Age tiers provide natural progression

### Trust Signal Examples

**For a 10-year-old:**
- 30 days incident-free → Unlock preset messages
- Parent confirmation → Unlock limited text chat
- 90 days clean → Unlock friend-of-friend social
- Moderator review → Unlock basic creation tools

**For a 14-year-old:**
- 60 days incident-free → Unlock full text chat
- Community contributions → Unlock advanced creation
- Parent approval → Unlock capped economy access
- Trust signals → Unlock self-regulation tools

---

## Why This Works

### Traditional Surveillance Approach
- Biometric scanning (privacy violation)
- Constant monitoring (creepy, invasive)
- Identity-based tracking (discriminatory)
- Parental dashboards (outing risk)

### Kiwi's Progressive Trust
- No biometrics (privacy-preserving)
- Capability-based (not identity-based)
- Trust signals (not surveillance)
- Parent controls (capability governance, not identity exposure)

### Safety Through Friction

- **High friction for risky behaviors:** Off-platform contact, private voice, dating features
- **Low friction for safe behaviors:** Emoji chat, preset messages, template games
- **Graduated friction:** Trust signals reduce friction over time
- **Contextual friction:** Age tiers provide appropriate barriers

---

## Implementation Details

### API-Level Enforcement

```yaml
# Example: Age-tier API restrictions
age_tier: child (0-9)
  available_apis:
    - emoji_chat
    - preset_messages
    - template_games
    - whitelist_social
  blocked_apis:
    - direct_messaging
    - voice_chat
    - economy_transactions
    - advanced_creation
```

### Permission Checks

Every API call checks:
1. User's age tier
2. User's trust signals
3. Capability permissions
4. Context (game, social space, etc.)

### Trust Signal Calculation

```yaml
trust_signals:
  time_on_platform: days_incident_free
  parental_confirmations: count_of_approvals
  moderator_reviews: positive_interactions
  community_endorsements: peer_trust_ratings
  capability_unlocks: graduated_access_level
```

---

## Parent Controls Integration

Parents can:
- Set capability boundaries (within age tier limits)
- Approve trust signal unlocks
- Monitor capability usage (not content)
- Set time and economic limits
- Receive escalation notifications

Parents cannot:
- See chat content (unless flagged)
- View social graphs (privacy-preserving)
- Access identity information
- Monitor private interactions

**See:** [Control Plane](./control_plane.md) for detailed parent control mechanisms

---

## Comparison to Roblox

### Roblox's Approach
- Age verification via COPPA compliance
- Settings-based restrictions (easily bypassed)
- Reactive moderation
- Surveillance-style monitoring
- Identity-based controls

### Kiwi's Approach
- Age-tiered accounts (architectural)
- Capability-based permissions (enforced)
- Progressive trust (incentivized)
- Non-biometric signals (privacy-preserving)
- Capability governance (not identity surveillance)

---

## Related Documentation

- [Control Plane](./control_plane.md) - How safety is enforced
- [Age Tiers](../../data/age_tiers.yaml) - Structured age tier definitions
- [Social Harm Counter-Architecture](../social/harm_counter_architecture.md) - Protection without exposure
- [First Principles](../strategic/first_principles.md) - Axioms that inform safety design

---

**Next:** [Moderation System](../operational/moderation_system.md)
