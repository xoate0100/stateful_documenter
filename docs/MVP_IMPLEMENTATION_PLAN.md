# MVP Implementation Plan - Documentation Project Support

**Date:** January 2025  
**Goal:** Adapt meta-framework to support documentation/task management projects alongside programming projects

---

## Overview

This plan outlines the specific code changes needed to support documentation projects while maintaining backward compatibility with programming projects.

---

## Phase 1: Core Infrastructure Changes

### 1.1 Extend MVP_SPECIFICATION.yaml Schema

**File:** `7_schemas/mvp_specification.schema.json`

**Changes:**
- Add `project_type` field (required, enum: `["programming", "documentation"]`)
- Add `documentation_structure` section (optional, only for documentation projects)
- Keep existing `MONOREPO_LAYOUT` for programming projects
- Add validation logic to ensure appropriate sections based on project_type

**New Schema Structure:**
```json
{
  "project_type": {
    "type": "string",
    "enum": ["programming", "documentation"],
    "description": "Type of project: programming (code-based) or documentation (task/documentation-based)"
  },
  "documentation_structure": {
    "type": "object",
    "properties": {
      "docs_directory": {"type": "string", "default": "docs/"},
      "data_directory": {"type": "string", "default": "data/"},
      "plans_directory": {"type": "string", "default": "plans/"},
      "evidence_directory": {"type": "string", "default": "evidence/"},
      "callables_directory": {"type": "string", "default": "callables/"}
    }
  }
}
```

### 1.2 Update Plan Schema for Hierarchical Goals

**File:** `7_schemas/plan.schema.json`

**Changes:**
- Extend to support hierarchical goal structure
- Add dependency tracking
- Add time tracking fields
- Add completion evidence

**New Structure:**
```json
{
  "type": "object",
  "required": ["plan_id", "project_type", "goal", "status"],
  "properties": {
    "plan_id": {"type": "string"},
    "project_type": {"type": "string", "enum": ["programming", "documentation"]},
    "component": {
      "type": "string",
      "enum": ["frontend", "backend", "shared"],
      "description": "Only for programming projects"
    },
    "goal": {"type": "string"},
    "goal_hierarchy": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "level", "name", "status"],
        "properties": {
          "id": {"type": "string"},
          "level": {"type": "integer", "minimum": 1, "maximum": 3},
          "name": {"type": "string"},
          "status": {"type": "string", "enum": ["not_started", "in_progress", "paused", "done"]},
          "sub_goals": {"type": "array"},
          "tasks": {
            "type": "array",
            "items": {
              "type": "object",
              "required": ["id", "name", "status"],
              "properties": {
                "id": {"type": "number"},
                "name": {"type": "string"},
                "status": {"type": "string", "enum": ["not_started", "in_progress", "paused", "done"]},
                "dependencies": {
                  "type": "array",
                  "items": {"type": "string"},
                  "description": "Array of task IDs this task depends on"
                },
                "time_tracking": {
                  "type": "object",
                  "properties": {
                    "started": {"type": "string", "format": "date-time"},
                    "completed": {"type": "string", "format": "date-time"},
                    "duration_minutes": {"type": "number"}
                  }
                },
                "completion_evidence": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "type": {"type": "string", "enum": ["github_file", "google_drive", "external_url", "note"]},
                      "url": {"type": "string"},
                      "description": {"type": "string"}
                    }
                  }
                },
                "outputs": {"type": "array", "items": {"type": "string"}}
              }
            }
          }
        }
      }
    },
    "tasks": {
      "type": "array",
      "description": "Legacy flat task list for programming projects"
    },
    "status": {"type": "string", "enum": ["active", "paused", "done"]},
    "auto_commit": {"type": "boolean"}
  }
}
```

### 1.3 Create Task Schema (Extended)

**File:** `7_schemas/tasks.schema.json` (update existing)

**Changes:**
- Add hierarchical support
- Add dependency tracking
- Add time tracking
- Add completion evidence

---

## Phase 2: Project Initialization Updates

### 2.1 Modify init_project.py

**File:** `3_bootstrap_scripts/init_project.py`

**Changes:**
- Add project type detection from MVP_SPECIFICATION.yaml
- Branch logic: `scaffold_programming_project()` vs `scaffold_documentation_project()`
- Documentation project structure:
  ```
  docs/           # Markdown documentation
  data/           # YAML/JSON/CSV structured data
  plans/          # Project plans (hierarchical)
  evidence/       # Completion evidence (links, files)
  callables/      # Reusable plan templates
  ```

**New Functions:**
```python
def detect_project_type(mvp_spec):
    """Detect if project is programming or documentation type"""
    return mvp_spec.get("project_type", "programming")

def scaffold_documentation_project(mvp_spec):
    """Scaffold directory structure for documentation projects"""
    doc_structure = mvp_spec.get("documentation_structure", {})
    # Create directories based on doc_structure
    # Generate initial ACTIVE_PLAN.yaml with hierarchical structure
    # Set up Second Brain integration config
```

### 2.2 Update MVP_SPECIFICATION.yaml Template

**File:** `0_phase0_bootstrap/MVP_SPECIFICATION.yaml`

**Changes:**
- Add `project_type` field at top level
- Add `documentation_structure` section (commented example)
- Update `ACTIVE_PLAN_TEMPLATE` to support both project types

---

## Phase 3: State Management & Focus Mode

### 3.1 Create Focus Mode Manager

**File:** `3_bootstrap_scripts/focus_mode.py` (new)

**Purpose:** Manage zoom in/out on hierarchical goals

**Functions:**
```python
def get_focused_context(active_plan_path, task_pointer_path):
    """Get filtered plan context based on current focus level"""
    # Read ACTIVE_PLAN.yaml
    # Read ACTIVE_TASK_POINTER.yaml
    # Return only relevant goal/task context + parent context (hidden from view)
    
def set_focus_level(goal_id, level):
    """Set current focus to specific goal level"""
    # Update ACTIVE_TASK_POINTER.yaml
    # Maintain parent context references
```

### 3.2 Update ACTIVE_TASK_POINTER.yaml

**File:** `6_ai_runtime_context/ACTIVE_TASK_POINTER.yaml` (update existing)

**New Structure:**
```yaml
current_focus:
  goal_id: "subgoal-1-1"
  level: 2
  name: "Create audience lists"
parent_context:
  - goal_id: "goal-1"
    level: 1
    name: "Setup Google Ads for Business"
    status: "in_progress"
```

### 3.3 Create Time Tracking Utility

**File:** `3_bootstrap_scripts/time_tracker.py` (new)

**Purpose:** Automatic time tracking for tasks

**Functions:**
```python
def track_task_start(task_id, plan_path):
    """Record task start timestamp"""
    
def track_task_complete(task_id, plan_path):
    """Record task completion timestamp and calculate duration"""
    
def get_task_duration(task_id, plan_path):
    """Get duration for a task"""
    
def detect_long_running_tasks(plan_path, threshold_hours=4):
    """Identify tasks that have been running too long"""
```

---

## Phase 4: Dependency Management

### 4.1 Create Dependency Analyzer

**File:** `3_bootstrap_scripts/dependency_analyzer.py` (new)

**Purpose:** Surface blocking dependencies and validate dependency graph

**Functions:**
```python
def get_blocking_tasks(task_id, plan_path):
    """Get list of tasks blocking this task"""
    
def get_blocked_tasks(task_id, plan_path):
    """Get list of tasks blocked by this task"""
    
def validate_dependency_cycles(plan_path):
    """Check for circular dependencies"""
    
def get_ready_tasks(plan_path):
    """Get tasks that have no blocking dependencies"""
```

---

## Phase 5: Second Brain Integration

### 5.1 Create Second Brain Configuration

**File:** `second_brain_config.yaml` (new, in project root)

**Structure:**
```yaml
second_brain:
  vault_path: "/path/to/second/brain/vault"
  enabled: true
  sync_on_completion: true
  read_references: true
```

### 5.2 Create Second Brain Reader Utility

**File:** `3_bootstrap_scripts/second_brain_reader.py` (new)

**Purpose:** Read related notes from Second Brain based on project context

**Functions:**
```python
def get_related_notes(project_keywords, vault_path):
    """Query Second Brain for notes related to current project"""
    # Search by tags, keywords, venture, domain
    # Return list of relevant notes with metadata
    
def load_note_content(note_path):
    """Load full content of a Second Brain note"""
```

### 5.3 Create Second Brain Updater Utility

**File:** `3_bootstrap_scripts/second_brain_updater.py` (new)

**Purpose:** Create/update Second Brain notes when tasks complete

**Functions:**
```python
def create_task_completion_note(task, plan, vault_path):
    """Create Second Brain note for completed task"""
    # Follow Second Brain schema (14+ required fields)
    # Set status, venture, domain, tags based on task/plan
    # Include completion evidence links
    
def update_task_note_status(note_path, new_status):
    """Update status of existing Second Brain note"""
```

**Second Brain Schema Compliance:**
- Required fields: `id`, `title`, `created`, `venture`, `domain`, `tags`, `status`
- Task completion notes: `status=done`, include `ai_summary`, `momentum_score`
- Link back to project: Include project path in `resources` or `toolbox`

---

## Phase 6: Callable Library Structure

### 6.1 Create Callable Library Manager

**File:** `3_bootstrap_scripts/callable_manager.py` (new)

**Purpose:** Manage reusable plan templates

**Functions:**
```python
def list_callables(category=None, tags=None):
    """List available callable plans"""
    
def load_callable(callable_id):
    """Load a callable plan template"""
    
def call_in_callable(callable_id, project_path):
    """Copy callable into project and make editable"""
    # Copy plan.yaml to project
    # Update references
    # Mark as "called in" (not template)
    
def create_callable(plan_path, metadata):
    """Create new callable from existing plan"""
    # Extract reusable parts
    # Add metadata (tags, categories, description)
    # Save to callables/ directory
```

### 6.2 Callable Library Structure

**Directory:** `callables/` (in project root or shared location)

**Structure:**
```
callables/
  marketing/
    google-ads-setup/
      plan.yaml
      metadata.yaml
      README.md
  operations/
    snow-ops-docs/
      plan.yaml
      metadata.yaml
```

**metadata.yaml:**
```yaml
callable_id: "google-ads-setup"
name: "Google Ads Setup"
category: "marketing"
tags: ["google-ads", "marketing", "audience-lists"]
description: "Complete setup workflow for Google Ads campaigns"
version: "1.0.0"
```

---

## Phase 7: Documentation Artifact Support

### 7.1 Create Documentation Generator

**File:** `3_bootstrap_scripts/doc_generator.py` (new)

**Purpose:** Generate markdown documentation from plans/tasks

**Functions:**
```python
def generate_task_documentation(task, plan):
    """Generate markdown doc for a task"""
    
def generate_goal_summary(goal, plan):
    """Generate summary documentation for a goal"""
    
def generate_project_overview(plan_path):
    """Generate project overview documentation"""
```

### 7.2 CSV Import/Export Support

**File:** `3_bootstrap_scripts/csv_handler.py` (new)

**Purpose:** Handle CSV imports from external systems (Google Ads, payroll, etc.)

**Functions:**
```python
def import_csv_to_data(csv_path, data_directory):
    """Import CSV and convert to structured YAML/JSON"""
    
def export_data_to_csv(data_path, csv_path):
    """Export structured data to CSV format"""
```

---

## Phase 8: AI Sandbox Rules Updates

### 8.1 Update AI_SANDBOX_RULES.md

**File:** `0_phase0_bootstrap/AI_SANDBOX_RULES.md`

**Changes:**
- Add documentation project permissions (docs/, data/, plans/, evidence/)
- Update task execution rules for hierarchical goals
- Add focus mode context rules (only show relevant context when zoomed)

### 8.2 Update Feature Flags

**File:** `0_phase0_bootstrap/feature_flags.yml`

**Changes:**
- Add `documentation_projects: true` flag
- Add `second_brain_integration: true` flag
- Add `hierarchical_goals: true` flag
- Update `write_to` permissions to include documentation directories

---

## Implementation Order

1. **Week 1: Schema & Structure**
   - Update MVP_SPECIFICATION.yaml schema
   - Update plan.schema.json for hierarchical goals
   - Create documentation_structure support

2. **Week 2: Initialization**
   - Modify init_project.py for project type detection
   - Implement scaffold_documentation_project()
   - Test initialization for both project types

3. **Week 3: State Management**
   - Implement focus mode manager
   - Create time tracking utility
   - Update ACTIVE_TASK_POINTER.yaml structure

4. **Week 4: Dependencies & Integration**
   - Implement dependency analyzer
   - Create Second Brain reader/updater
   - Basic callable library structure

5. **Week 5: Documentation & Testing**
   - Documentation artifact generators
   - CSV import/export
   - Update sandbox rules
   - Test with real Google Ads project

---

## Testing Strategy

1. **Unit Tests:** Each new utility function
2. **Integration Tests:** Full project initialization for documentation type
3. **End-to-End Test:** Complete Google Ads setup project using new system
4. **Backward Compatibility:** Ensure programming projects still work

---

## Migration Path

For existing projects:
- Programming projects: No changes needed (backward compatible)
- New documentation projects: Use new project_type="documentation"
- Can convert existing plans to hierarchical structure (optional migration script)

---

**End of Implementation Plan**

