# Documentation Project System - Analysis & Requirements

**Date:** January 2025  
**Purpose:** Comprehensive analysis of adapting the meta-framework for stateful documentation/task management projects (non-programming)

---

## Executive Summary

You're building a **stateful task-tracked documentation system** that adapts your existing programming-focused meta-framework to handle complex, multi-step documentation and organizational projects. The system addresses ADHD-related executive function challenges (task switching friction, scope creep, difficulty staying on track) while maintaining the robust constraints, sandbox rules, and execution guidelines from your current framework.

**Core Problem:** ChatGPT/Claude/Gemini conversations lose state, get long, and hallucinate. You need persistent, stateful memory across AI interactions for complex projects requiring lots of back-and-forth.

---

## What You're Building

### Primary Use Cases

1. **Marketing Configuration Projects**
   - Google Ads setup (audience lists, naming conventions across Analytics/Ads/Tag Manager)
   - Email sequence management (30 emails in "book download" sequence, need to segment "opened download" contacts)
   - Cross-platform campaign coordination

2. **Operations Documentation**
   - Snow Operations Documentation system updates
   - Traverse folders, find employee communications, update with additional instructions
   - Maintain consistency across distributed documentation

3. **Complex Life Projects**
   - Private school creation (mix of documentation tasks + real-world actions)
   - Tasks completed outside system need reporting mechanism
   - Long-term goal tracking with hierarchical breakdown

4. **Business Growth Projects**
   - "Grow business $500,000 this year" → broken into manageable, atomic goal sets
   - MVP definition: "Setup Google Ads and get one ad running for 1 month"
   - Zoom in/out capability: focus on details without losing big picture

### Execution Environment

**Critical Architecture Decision:** This system operates entirely within the **Cursor IDE workspace** where you have access to Cursor IDE AI chat agents. This means:

- **File-based execution:** All plans, tasks, and state stored as YAML/Markdown files in the workspace
- **Cursor AI agent execution:** Cursor AI agents read `ACTIVE_PLAN.yaml` and execute tasks directly
- **No separate application:** Everything works through Cursor's existing AI sandbox and file system
- **Same workflow:** Documentation projects follow the same AI execution model as programming projects
- **Stateful memory:** Persistent state in `6_ai_runtime_context/` allows AI agents to maintain context across sessions

This is a **meta-framework adaptation**, not a new application. The system leverages Cursor IDE's existing AI capabilities to execute documentation/task management workflows.

### Key Differentiators from Programming Projects

| Programming Projects | Documentation Projects |
|---------------------|----------------------|
| Code files (TS/Python) | Markdown docs, YAML/JSON, CSV |
| Frontend/Backend/Shared components | Hierarchical goals → sub-goals → tasks |
| Test-driven development | Completion criteria (guidelines, not hard rules) |
| Code quality gates | Documentation quality + task state tracking |
| Component-based structure | Goal-based structure with focus mode |
| **Execution:** Cursor AI writes code | **Execution:** Cursor AI writes docs, updates plans, tracks state |

---

## Core Requirements

### 1. Hierarchical Goal System

**Structure:**
```
High-Level Goal (e.g., "Grow business $500k")
  └─ Sub-Goal (e.g., "Setup Google Ads")
      └─ Sub-Goal (e.g., "Get one ad running")
          └─ Task (e.g., "Create audience list")
          └─ Task (e.g., "Define naming conventions")
```

**Features:**
- **Automatic parent completion:** When all child tasks complete, parent goal can auto-complete (with review loop)
- **Focus mode:** When "zoomed in" on a sub-goal, hide full hierarchy to prevent overwhelm
- **State preservation:** System "comes with you" into zoom, maintains context of parent goals
- **Review loops:** Built-in closure/feedback mechanisms for completed parent goals ("warm fuzzy goods")

### 2. Stateful Task Tracking

**Automatic Tracking:**
- **Time tracking:** Automatic date/time tracking (no manual entry to avoid executive function overload)
- **Dependency surfacing:** System identifies and surfaces blocking dependencies
- **Task breakdown:** AI suggests breaking down tasks that are "taking too long"
- **Status transitions:** Track task states (not started → in-progress → paused → done)

**Completion Reporting:**
- External task completion (real-world actions) can be reported with evidence
- Evidence storage: GitHub (version controlled) + Google Drive (via Google Workspace)
- Completion criteria as guidelines (flexible, can evolve as project clarifies)

### 3. Focus & Scope Management

**ADHD-Optimized Features:**
- **No hard blocks:** Don't stifle creativity/flow, but match new tasks to existing callables/projects
- **No limits:** No artificial limits on active tasks or time-based restrictions
- **Ideation capture:** Quick "park this idea" action with:
  - Prompted review (pushed to user)
  - Brief exploration window
  - Stateful filing for later access

**Scope Creep Prevention:**
- Surface dependencies and blocking tasks
- Suggest task breakdown when tasks take too long
- Maintain focus mode context (zoom in without losing big picture)

### 4. AI Integration & Execution (Cursor IDE)

**Primary Execution Environment:** Cursor IDE workspace with Cursor AI chat agents

**AI Roles in Cursor IDE:**
1. **Ideation:** Green field support to ideate MVP and essential activities (via Cursor chat)
2. **Plan Creation:** Break down massive goals into manageable, atomic goal sets (AI creates/updates ACTIVE_PLAN.yaml)
3. **Execution:** Cursor AI agents execute tasks by:
   - Reading `6_ai_runtime_context/ACTIVE_PLAN.yaml` to understand current state
   - Creating/updating markdown documentation in `docs/`
   - Managing structured data files (YAML/JSON/CSV) in `data/`
   - Updating task status, time tracking, and completion evidence
   - Following AI_SANDBOX_RULES.md (same constraints as programming projects)

**Stateful Memory:**
- Persistent context in `6_ai_runtime_context/` files (ACTIVE_PLAN.yaml, ACTIVE_TASK_POINTER.yaml, MEMORY_STATE.yaml)
- Cursor AI agents maintain context across chat sessions by reading these files
- No rework due to hallucination/lost context (state is file-based, not conversation-based)
- Project state maintained in GitHub (version controlled)
- **Cross-AI Tool Support:** You can also use ChatGPT/Claude/Gemini for ideation, but execution happens in Cursor IDE where state is maintained

**OpenAI API Integration (Post-MVP):**
- On-demand asset generation:
  - Markdown documentation templates
  - Structured data files (CSV schemas, YAML configs)
  - Content drafts (email copy, ad copy)
  - Analysis/summaries of exported data
- Document enhancement: Expand partial plans into full task breakdowns

### 5. Second Brain Integration

**Architecture:**
- **Second Brain = Storage/Capture Layer** (existing system)
- **This System = Execution/Memory Layer** (new system)
- Build on top of Second Brain, don't redo efforts

**Integration Points:**
- **Read reference data:** When working on a project, show related notes from Second Brain
- **Auto-update tasks:** Task completions automatically create/update Second Brain notes (schema-enforced)
- **Callable library:** Reusable plans/ideas can:
  - Live in GitHub (package-like abilities)
  - Be referenced in Second Brain
  - Be editable when "called in" (organic evolution)

**Callable Library Features:**
- **Organization:** Tags, categories, keyword searchable
- **AI suggestions:** Proactively suggest relevant modules based on current project context
- **Types:** Full plans (with tasks) + partial plans (concepts)
- **Evolution:** Editable when called in (not just templates), so callables improve over time
- **Example:** "Google Ads" scaffold that works for setup/execution/testing every time, scales to Meta/X/TikTok ads

### 6. Project Initialization Adaptation

**Current System:**
- Designed for programming projects (frontend/backend/shared)
- MVP_SPECIFICATION.yaml defines tech stack, components, etc.
- Generates code structure, dependencies, etc.

**New System Needs:**
- Support for documentation projects (no code components)
- Project type detection: "documentation" vs "programming"
- Different scaffolding based on project type
- Same constraints/sandbox/execution guidelines framework

---

## MVP Scope (Phase 1)

### Must-Have Features

1. **Core Task System**
   - Hierarchical goals (3 levels: Goal → Sub-Goal → Task)
   - Task state tracking (not_started, in_progress, paused, done)
   - Automatic time tracking (start/end timestamps)
   - Dependency management (blocking relationships)
   - Focus mode (zoom in/out on goals)

2. **Project Initialization**
   - Modified `init_project.py` to detect project type
   - Support "documentation" project type in MVP_SPECIFICATION.yaml
   - Generate appropriate structure (docs/, data/, plans/)
   - Same validation/schema enforcement

3. **Stateful Plan Execution**
   - ACTIVE_PLAN.yaml with hierarchical structure
   - ACTIVE_TASK_POINTER.yaml to track current focus
   - State persistence in 6_ai_runtime_context/
   - AI can read/execute plans (same sandbox rules)

4. **Second Brain Integration (Basic)**
   - Read reference data from Second Brain (read-only for MVP)
   - Auto-update Second Brain when tasks complete (schema-enforced)
   - Basic callable library structure (GitHub-based)

5. **Documentation Artifacts**
   - Markdown documentation generation
   - YAML/JSON structured data support
   - CSV import/export capability
   - Evidence attachment (links to Google Drive, GitHub files)

### Deferred to Phase 2

- Full ideation capture system (park ideas, exploration windows)
- OpenAI API integration (asset generation, document enhancement)
- Advanced callable library (AI suggestions, cross-project access)
- Google Drive integration (evidence storage)
- Review loops with celebration/feedback
- Task breakdown suggestions (AI-powered)

---

## Technical Architecture

### Execution Model

**File-Based AI Agent Execution:**
- All state stored as YAML/Markdown files in Cursor IDE workspace
- Cursor AI agents read `6_ai_runtime_context/ACTIVE_PLAN.yaml` to understand current state
- AI agents execute tasks by:
  1. Reading plan structure and current focus level
  2. Creating/updating documentation files in `docs/`
  3. Managing structured data in `data/`
  4. Updating task status and time tracking in plan files
  5. Syncing completion to Second Brain via utility scripts
- Same AI sandbox rules apply (read-only meta-framework, write permissions for project files)
- No separate UI or application needed - everything works through Cursor's file system and AI chat

### Modified Components

1. **MVP_SPECIFICATION.yaml Schema**
   - Add `project_type: "documentation" | "programming"`
   - Add `documentation_structure` section (replaces MONOREPO_LAYOUT for docs projects)
   - Keep same validation framework

2. **init_project.py**
   - Detect project type from MVP_SPECIFICATION.yaml
   - Branch logic: programming vs documentation scaffolding
   - Documentation projects: Generate `docs/`, `data/`, `plans/`, `evidence/` structure
   - Same validation, hooks, CI setup

3. **Plan Schema (plan.schema.json)**
   - Extend to support hierarchical goals
   - Add `parent_goal_id`, `goal_level` fields
   - Add `dependencies` array to tasks
   - Add `time_tracking` (start_time, end_time, duration)
   - Add `completion_evidence` (links, notes)

4. **ACTIVE_PLAN.yaml Structure**
   ```yaml
   plan_id: "google-ads-setup"
   project_type: "documentation"
   goal_hierarchy:
     - id: "goal-1"
       level: 1
       name: "Setup Google Ads for Business"
       status: "in_progress"
       sub_goals:
         - id: "subgoal-1-1"
           level: 2
           name: "Create audience lists"
           status: "not_started"
           tasks:
             - id: 1
               name: "Export existing customer list"
               status: "in_progress"
               dependencies: []
               time_tracking:
                 started: "2025-01-15T10:00:00Z"
               completion_evidence: []
   ```

5. **Focus Mode Implementation**
   - ACTIVE_TASK_POINTER.yaml tracks current "zoom level"
   - AI reads only relevant context when zoomed in
   - Parent goal context maintained but hidden from view

6. **Second Brain Integration**
   - Configuration file: `second_brain_config.yaml` (path to Second Brain vault)
   - Utility: `read_second_brain_references.py` (query related notes)
   - Utility: `update_second_brain_task.py` (create/update notes on task completion)
   - Follow Second Brain schema (14+ required fields from SECOND_BRAIN_OVERVIEW.md)

### New Components

1. **Time Tracking Utility**
   - Automatic timestamp on task status changes
   - Calculate duration for completed tasks
   - Detect "taking too long" (configurable threshold)

2. **Dependency Analyzer**
   - Parse task dependencies from ACTIVE_PLAN.yaml
   - Surface blocking tasks
   - Validate dependency cycles

3. **Focus Mode Manager**
   - Track current zoom level in ACTIVE_TASK_POINTER.yaml
   - Filter plan context for AI based on zoom level
   - Maintain parent context without overwhelming

4. **Callable Library Structure**
   - Directory: `callables/` (GitHub-based, version controlled)
   - Structure: `callables/{category}/{name}/plan.yaml`
   - Metadata: Tags, categories, description
   - Can be "called in" to projects (copied/edited)

---

## SOLID Principles Application

You mentioned needing your brain to operate more like SOLID systems to avoid "dependency hell" and repetition. The system should enforce:

1. **Single Responsibility:** Each goal/task has one clear purpose
2. **Open/Closed:** Callable library extensible without modifying core
3. **Liskov Substitution:** Documentation projects and programming projects both follow same meta-framework interface
4. **Interface Segregation:** Clear separation between Second Brain (storage) and this system (execution)
5. **Dependency Inversion:** Depend on abstractions (plan schema, task interface), not concrete implementations

---

## Success Metrics

1. **Stateful Memory:** Zero rework due to lost context/hallucination
2. **Focus Maintenance:** Can zoom in on tasks without losing big picture
3. **Task Completion:** % of tasks completed vs abandoned
4. **Dependency Resolution:** Time to identify and resolve blocking dependencies
5. **Second Brain Sync:** % of task completions successfully synced to Second Brain

---

## Next Steps

1. **Modify MVP_SPECIFICATION.yaml schema** to support documentation projects
2. **Update init_project.py** to handle documentation project type
3. **Extend plan.schema.json** for hierarchical goals
4. **Create Second Brain integration utilities** (read/update)
5. **Implement focus mode** (ACTIVE_TASK_POINTER.yaml management)
6. **Build time tracking** (automatic timestamps)
7. **Create callable library structure** (basic GitHub-based)

---

## Questions for Further Clarification

1. Should documentation projects still use the same pre-commit hooks (format, lint, etc.) or different validation?
2. How should "completion criteria" be stored? In task YAML, separate file, or both?
3. For the "park idea" feature (Phase 2), should parked ideas become new projects or just stored callables?
4. Should the system support multiple active projects simultaneously, or one at a time?

---

**End of Analysis**

