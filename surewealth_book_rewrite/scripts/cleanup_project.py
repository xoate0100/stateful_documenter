#!/usr/bin/env python3
"""
Project Cleanup Script
Organizes documentation, archives deprecated files, updates indexes
"""

import shutil
from pathlib import Path
from datetime import datetime


def cleanup_project():
    """Clean up and organize project structure"""
    
    project_root = Path(".")
    
    # Create archive directory if it doesn't exist
    archive_dir = project_root / "docs" / "archive"
    archive_dir.mkdir(parents=True, exist_ok=True)
    
    # Files to archive from root (deprecated/duplicate summaries)
    files_to_archive = [
        "INTEGRATION_COMPLETE_SUMMARY.md",
        "INTEGRATION_SUMMARY.md",
        "PATTERN_INTEGRATION_VERIFIED.md",
        "COMPLIANCE_SYSTEM_SUMMARY.md",
        "META_FRAMEWORK_AUDIT_COMPLETE.md",
        "META_FRAMEWORK_AUDIT.md",
        "SURewEALTH_CONTENT_ANALYSIS.md",  # Duplicate of docs/analysis/SUREWEALTH_CONTENT_ANALYSIS.md
    ]
    
    # Files to move to docs/ (integration docs)
    files_to_move_to_docs = [
        "FINAL_INTEGRATION_STATUS.md",
    ]
    
    print("=" * 70)
    print("Project Cleanup - Archiving Deprecated Files")
    print("=" * 70)
    print()
    
    # Archive files
    archived = []
    for filename in files_to_archive:
        source = project_root / filename
        if source.exists():
            dest = archive_dir / filename
            shutil.move(str(source), str(dest))
            archived.append(filename)
            print(f"  [ARCHIVED] {filename} -> docs/archive/")
    
    # Move files to docs/
    moved = []
    docs_dir = project_root / "docs"
    for filename in files_to_move_to_docs:
        source = project_root / filename
        if source.exists():
            dest = docs_dir / filename
            shutil.move(str(source), str(dest))
            moved.append(filename)
            print(f"  [MOVED] {filename} -> docs/")
    
    print()
    print(f"Archived {len(archived)} files")
    print(f"Moved {len(moved)} files to docs/")
    print()
    
    # Check for old compliance_report.md
    compliance_report = project_root / "compliance_report.md"
    if compliance_report.exists():
        # Check if it's old (you can add date checking logic here)
        dest = archive_dir / f"compliance_report_{datetime.now().strftime('%Y%m%d')}.md"
        shutil.move(str(compliance_report), str(dest))
        print(f"  [ARCHIVED] compliance_report.md -> docs/archive/")
    
    print()
    print("=" * 70)
    print("Cleanup Complete")
    print("=" * 70)
    print("\nNext steps:")
    print("1. Review archived files in docs/archive/")
    print("2. Update README.md")
    print("3. Update docs/MASTER_INDEX.md")
    print("4. Update docs/analysis/ANALYSIS_INDEX.md")


if __name__ == "__main__":
    cleanup_project()

