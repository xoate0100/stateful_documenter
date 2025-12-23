# Second Brain System - Overview for AI LLM Parsing

**Last Updated:** January 2025  
**Purpose:** Quick reference for AI assistants to understand system purpose, tech stack, and core problems solved

---

## System Purpose

The Second Brain is an **ADHD-focused knowledge and action management system** designed to overcome initiation inertia, reduce decision fatigue, and provide friction-free capture and execution workflows. It transforms raw captures (conversations, notes, ideas) into an organized Zettelkasten knowledge base with intelligent task management, momentum tracking, and anti-overwhelm features.

---

## Core Problems Solved

### 1. Initiation Inertia (ADHD Primary Problem)
**Problem:** Users with ADHD struggle to start tasks due to:
- Decision paralysis when facing too many options
- Lack of clear "first action" cues
- Overwhelm from seeing all tasks at once
- Context switching difficulty when resuming paused work

**Solution:**
- **Launchpads** with anti-overwhelm limits (max 20 items all-venture, max 8 per venture)
- **First Action Generation:** AI generates concrete, unambiguous first physical steps (e.g., "Open folder X and review file Y")
- **Resume Hints:** Context-specific cues for resuming paused/in-progress work
- **Status-based filtering:** Only show "ready" items by default, reducing cognitive load

### 2. Decision Fatigue
**Problem:** Too many choices cause paralysis; users can't prioritize effectively.

**Solution:**
- **Energy Mode Matching:** Filter tasks by current capacity (calm, creative, grunt, people)
- **Effort Estimate Filtering:** Find quick wins (5-15 min tasks) when energy is low
- **Context Need Indicators:** Prioritize low-context tasks that can start immediately
- **Momentum Scoring:** Visual feedback reinforces engagement and completion

### 3. Information Overload & Fragmentation
**Problem:** Ideas, notes, and tasks scattered across multiple channels and formats; no unified system.

**Solution:**
- **Multi-Channel Capture:** Voice (Alexa), iOS Shortcuts, Email, Desktop quick entry
- **Unified Processing:** All captures normalized into structured Markdown + YAML format
- **Zettelkasten Organization:** Atomic notes with bidirectional linking for knowledge networking
- **AI-Powered Tagging:** Automatic categorization and relationship detection

### 4. Context Loss & Re-entry Difficulty
**Problem:** When returning to paused work, users forget where they left off and what they were doing.

**Solution:**
- **Resume Hints:** AI-generated context cues for paused/in-progress items
- **Status Transitions:** Clear workflow states (inbox → ready → in-progress → paused → done)
- **Momentum Tracking:** Visual progress indicators show completion patterns
- **Daily Primers:** Contextual summaries of what to focus on today

### 5. Lack of Momentum Feedback
**Problem:** No dopamine feedback loop; users don't see progress or feel accomplishment.

**Solution:**
- **Momentum Scores:** Incremental scoring on status transitions (ready → in-progress = +1, in-progress → done = +3)
- **Visual Indicators:** Progress bars, badges, color-coded momentum levels
- **Weekly Momentum Reports:** Summary of completion patterns and engagement trends
- **Celebration Cues:** Visual feedback on task completion

### 6. Executive Dysfunction Scaffolding
**Problem:** ADHD users need external structure to compensate for executive function challenges.

**Solution:**
- **Forced Progress Tracking:** System enforces state transitions and momentum scoring
- **Template Constraints:** Pre-defined schemas reduce decision-making burden
- **Workflow Automation:** n8n integration for custom automation workflows
- **Review Compliance:** Automated reminders and compliance tracking

---

## Tech Stack (Brief)

### Backend
- **Python 3.11+** with **FastAPI** (REST API, health monitoring)
- **SQLite** (state persistence, idempotency tracking)
- **PostgreSQL** (n8n workflow data, optional)
- **Docker Compose** (containerized services)

### AI/ML Services
- **Ollama** (local LLM server, LLAMA3 model)
  - Content analysis and tagging
  - First action generation
  - Resume hint generation
  - AI summarization
- **OpenAI API** (optional, for enhanced processing)

### Workflow Automation
- **n8n** (visual workflow orchestration, webhook processing)
- **Zapier** (external integrations, email capture)

### Frontend (In Development)
- **TypeScript** with custom component framework
- **Markdown rendering** (marked/markdown-it)
- **CodeMirror 6** (markdown editor)
- **Review GUI** for note management and status transitions

### Data Storage
- **Obsidian Vaults** (Markdown + YAML files, local-first)
- **Structured YAML Schema** (14+ required fields per note)
- **Zettelkasten principles** (atomic notes, bidirectional linking)

### Monitoring & Quality
- **Prometheus/Grafana** (system health monitoring)
- **Loki** (log aggregation)
- **Comprehensive audit framework** (ADHD-specific, behavioral, cognitive metrics)

---

## Key Features

### Current Implementation
- ✅ OpenAI conversation import and processing
- ✅ AI-powered tag generation (Ollama)
- ✅ Obsidian vault structure creation
- ✅ Basic file organization and categorization
- ✅ Idempotency guards (prevents reprocessing)
- ✅ REST API with health monitoring
- ✅ Docker-based deployment

### Planned/In Progress (MVP Gap)
- 🔄 Multi-channel capture (Alexa, iOS, Email, Desktop)
- 🔄 Complete YAML schema with all 14+ fields
- 🔄 Task management with status transitions
- 🔄 Launchpads with anti-overwhelm limits
- 🔄 First action and resume hint generation
- 🔄 Momentum scoring and visualization
- 🔄 Daily primers and weekly momentum reports
- 🔄 Energy mode and effort estimate filtering
- 🔄 Review workflow GUI

---

## Data Model (Core Schema)

Every processed note (`_zettel`) includes:

**Required Fields:**
- `id`, `title`, `created`, `venture`, `domain`, `tags`, `status`
- `ai_summary`, `first_action` (when status=ready)
- `resume_hint` (when status=paused/in-progress)
- `momentum_score`, `effort_estimate_min`, `context_need`, `source`

**Optional Fields:**
- `location`, `energy_mode`, `resources`, `toolbox`, `ai_tags`

**Status Workflow:**
```
inbox → ready → in-progress → paused → done
                ↓              ↑
                └──────────────┘
```

---

## Architecture Principles

1. **Local-First:** All data stored as Markdown + YAML files (portable, agent-ready)
2. **Container-First:** All services run in Docker containers
3. **State-Driven:** SQLite-based state management for reliability
4. **Schema-Enforced:** YAML validation for all data types
5. **Idempotent Operations:** Duplicate prevention and safe retry mechanisms
6. **ADHD-Optimized:** Anti-overwhelm limits, momentum feedback, friction reduction

---

## Target User Persona

**Andy (Primary User):**
- Single user with ADHD-inertia pattern
- Can hyperfocus once started
- Needs unambiguous start cues
- Struggles with initiation and context re-entry
- Benefits from external structure and momentum feedback

**Future Agent (Guardian AI):**
- Will query structured notes later
- Requires consistent schema and exportable format
- Needs agent-ready data structure

---

## Success Metrics

- **Initiation Success:** % of "ready" items that transition to "in-progress" within 24h
- **Momentum Growth:** Average momentum score increase per week
- **Review Compliance:** % of items reviewed within 7 days
- **Overwhelm Prevention:** Launchpad items stay within limits (20/8)
- **Context Re-entry:** % of paused items resumed within 48h

---

## Related Documentation

- `original_MVP.md` - Complete MVP requirements
- `docs/MVP_GAP_ANALYSIS.md` - Current state vs. original vision
- `docs/development/working/FRONTEND_ENHANCEMENT_PLAN.md` - Frontend roadmap
- `README.md` - Technical setup and usage

---

**Note for AI Assistants:** This system is designed to be "agent-ready" with structured schemas, consistent naming conventions, and exportable formats. All processing maintains idempotency and state tracking for reliable automation.

