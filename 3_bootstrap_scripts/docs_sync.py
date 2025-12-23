#!/usr/bin/env python3
"""
Documentation Sync Script
Maintains master documentation index that includes:
- Meta-framework documentation (rules, standards, schemas)
- All programming projects
- All documentation projects
- Project-specific master indexes
"""
import sys
import json
import pathlib
import time
from typing import List, Dict, Optional

try:
    import yaml
except ImportError:
    print("[docs] Error: PyYAML not installed. Install with: pip install PyYAML")
    sys.exit(1)


def detect_project_type(project_path: pathlib.Path) -> Optional[str]:
    """Detect project type from MVP_SPECIFICATION.yaml"""
    mvp_path = project_path / "MVP_SPECIFICATION.yaml"
    if not mvp_path.exists():
        return None
    
    try:
        mvp = yaml.safe_load(open(mvp_path))
        project_type = mvp.get("Project_Type") or mvp.get("project_type")
        if project_type:
            return project_type.lower()
    except:
        pass
    
    return None


def find_projects(root: pathlib.Path) -> List[Dict]:
    """Find all projects (folders with MVP_SPECIFICATION.yaml)"""
    projects = []
    
    # Check root-level projects (e.g., mudp_project/)
    for item in root.iterdir():
        if not item.is_dir():
            continue
        
        # Skip meta-framework directories
        if item.name.startswith(("0_", "1_", "2_", "3_", "4_", "5_", "6_", "7_", "8_", ".", "docs", "frontend", "backend", "shared", "scripts")):
            continue
        
        mvp_path = item / "MVP_SPECIFICATION.yaml"
        if mvp_path.exists():
            project_type = detect_project_type(item)
            projects.append({
                "name": item.name,
                "path": str(item),
                "type": project_type or "unknown",
                "mvp_spec": mvp_path
            })
    
    return projects


def get_project_info(project: Dict, root: pathlib.Path) -> Dict:
    """Extract project information from MVP_SPECIFICATION"""
    info = {
        "name": project["name"],
        "type": project["type"],
        "path": project["path"],
        "readme": None,
        "master_index": None,
        "description": None
    }
    
    project_path = pathlib.Path(project["path"])
    
    # Check for README
    readme_path = project_path / "README.md"
    if readme_path.exists():
        try:
            rel_path = readme_path.relative_to(root)
            info["readme"] = str(rel_path).replace("\\", "/")
        except ValueError:
            # Fallback: use relative path from project
            info["readme"] = f"{project['path']}/README.md"
    
    # Check for project-specific master index
    if project["type"] == "documentation":
        master_index_path = project_path / "docs" / "MASTER_INDEX.md"
        if master_index_path.exists():
            try:
                rel_path = master_index_path.relative_to(root)
                info["master_index"] = str(rel_path).replace("\\", "/")
            except ValueError:
                # Fallback: use relative path from project
                info["master_index"] = f"{project['path']}/docs/MASTER_INDEX.md"
    
    # Try to get description from MVP_SPECIFICATION
    try:
        mvp = yaml.safe_load(open(project["mvp_spec"]))
        goals = mvp.get("GOALS_AND_PRINCIPLES", {}).get("goals", [])
        if goals:
            info["description"] = goals[0]  # Use first goal as description
    except:
        pass
    
    return info


def generate_master_index(projects: List[Dict], root: pathlib.Path) -> str:
    """Generate comprehensive master documentation index"""
    
    # Separate projects by type
    programming_projects = [p for p in projects if p["type"] == "programming"]
    documentation_projects = [p for p in projects if p["type"] == "documentation"]
    unknown_projects = [p for p in projects if p["type"] == "unknown"]
    
    lines = [
        "# Master Documentation Index",
        "",
        "**Last Updated:** " + time.strftime("%Y-%m-%d %H:%M:%S"),
        "",
        "This is the master reference for all documentation in this repository, including:",
        "- Meta-framework rules, standards, and guidelines",
        "- All programming projects",
        "- All documentation projects",
        "",
        "---",
        "",
        "## Meta-Framework Documentation",
        "",
        "### Core Framework",
        "- **[Meta-Framework Overview](0_phase0_bootstrap/META_FRAMEWORK_OVERVIEW.md)** - Framework architecture and principles",
        "- **[AI Sandbox Rules](0_phase0_bootstrap/AI_SANDBOX_RULES.md)** - AI agent execution rules (project-type aware)",
        "- **[AI Execution Constraints](0_phase0_bootstrap/AI_EXECUTION_CONSTRAINTS.md)** - Execution constraints and gates",
        "- **[Feature Flags](0_phase0_bootstrap/feature_flags.yml)** - Guardrails and permissions configuration",
        "",
        "### Standards & Guidelines",
        "- **[Documentation Standards](1_global_standards/DOCS_STANDARDS.md)** - Documentation requirements",
        "- **[Code Style Guide](1_global_standards/CODE_STYLE_GUIDE.md)** - Code formatting and style",
        "- **[SOLID Principles](1_global_standards/SOLID_PRINCIPLES.md)** - Architecture principles (programming projects)",
        "- **[Test Strategy (TDD)](1_global_standards/TEST_STRATEGY_TDD.md)** - Test-driven development (programming projects)",
        "- **[Security Baselines](1_global_standards/SECURITY_BASELINES.md)** - Security requirements",
        "- **[Git Strategy](1_global_standards/GIT_STRATEGY.md)** - Git workflow and commit conventions",
        "- **[CI/CD Guide](1_global_standards/CI_CD_GUIDE.md)** - Continuous integration/deployment",
        "",
        "### Architecture & Schemas",
        "- **[Layer Rules](5_reference_architectures/LAYER_RULES.yaml)** - Component architecture rules",
        "- **[Schemas](7_schemas/)** - JSON schemas for validation",
        "",
        "### Scripts & Tools",
        "- **[Bootstrap Scripts](3_bootstrap_scripts/)** - Project initialization and maintenance scripts",
        "- **[Templates](2_framework_templates/)** - Project templates and configurations",
        "",
        "### Active Context",
        "- **[Active Plan](6_ai_runtime_context/ACTIVE_PLAN.yaml)** - Current execution plan",
        "- **[Active Task Pointer](6_ai_runtime_context/ACTIVE_TASK_POINTER.yaml)** - Current focus",
        "",
        "---",
        "",
        "## Programming Projects",
        ""
    ]
    
    if programming_projects:
        for project in programming_projects:
            lines.append(f"### [{project['name']}]({project['path']}/)")
            if project.get("description"):
                lines.append(f"- **Description:** {project['description']}")
            if project.get("readme"):
                readme_name = pathlib.Path(project['readme']).name
                lines.append(f"- **README:** [{readme_name}]({project['readme']})")
            lines.append("")
    else:
        lines.append("*No programming projects found*")
        lines.append("")
    
    lines.extend([
        "---",
        "",
        "## Documentation Projects",
        ""
    ])
    
    if documentation_projects:
        for project in documentation_projects:
            lines.append(f"### [{project['name']}]({project['path']}/)")
            if project.get("description"):
                lines.append(f"- **Description:** {project['description']}")
            if project.get("readme"):
                readme_name = pathlib.Path(project['readme']).name
                lines.append(f"- **README:** [{readme_name}]({project['readme']})")
            if project.get("master_index"):
                lines.append(f"- **Master Index:** [MASTER_INDEX.md]({project['master_index']}) - Comprehensive project documentation")
            lines.append("")
    else:
        lines.append("*No documentation projects found*")
        lines.append("")
    
    if unknown_projects:
        lines.extend([
            "---",
            "",
            "## Other Projects",
            ""
        ])
        for project in unknown_projects:
            lines.append(f"- [{project['name']}]({project['path']}/)")
        lines.append("")
    
    lines.extend([
        "---",
        "",
        "## Repository Structure",
        "",
        "```",
        "repository/",
        "├── 0_phase0_bootstrap/     # Meta-framework configuration",
        "├── 1_global_standards/      # Standards and guidelines",
        "├── 2_framework_templates/   # Project templates",
        "├── 3_bootstrap_scripts/     # Initialization scripts",
        "├── 4_docs_index/            # This master index",
        "├── 5_reference_architectures/ # Architecture rules",
        "├── 6_ai_runtime_context/     # Active plans and state",
        "├── 7_schemas/               # Validation schemas",
        "├── 8_ci/                     # CI/CD configuration",
        "├── frontend/                 # Frontend code (if root is programming project)",
        "├── backend/                  # Backend code (if root is programming project)",
        "├── shared/                   # Shared code (if root is programming project)",
        "└── <project_name>/          # Individual projects (programming or documentation)",
        "```",
        "",
        "---",
        "",
        "## How to Use This Index",
        "",
        "1. **For Meta-Framework Rules:** See [Meta-Framework Documentation](#meta-framework-documentation) section",
        "2. **For Programming Projects:** See [Programming Projects](#programming-projects) section",
        "3. **For Documentation Projects:** See [Documentation Projects](#documentation-projects) section",
        "4. **For Project-Specific Documentation:** Each documentation project has its own `docs/MASTER_INDEX.md`",
        "",
        "---",
        "",
        "**Note:** This index is automatically generated by `docs_sync.py`. Run it manually or via pre-commit hook.",
        ""
    ])
    
    return "\n".join(lines)


def main():
    """Main documentation sync"""
    root = pathlib.Path.cwd()
    idx_path = root / "4_docs_index" / "DOCUMENTATION_INDEX.md"
    
    # Ensure directory exists
    idx_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Find all projects
    projects = find_projects(root)
    
    # Get project information
    project_info = [get_project_info(p, root) for p in projects]
    
    # Generate master index
    index_content = generate_master_index(project_info, root)
    
    # Write index
    idx_path.write_text(index_content, encoding="utf-8")
    
    print(f"[docs] Master index updated: {idx_path}")
    print(f"[docs] Found {len(projects)} project(s):")
    for p in project_info:
        print(f"  - {p['name']} ({p['type']})")
    
    sys.exit(0)


if __name__ == "__main__":
    main()
