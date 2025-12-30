#!/usr/bin/env python3
"""
Test Enhanced Validators on Chapters 1-4
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from meta_framework.content_quality.content_validator import ContentValidator
from pathlib import Path

def test_chapter(chapter_path: Path, chapter_num: int, funnel_stage: str, persona: str):
    """Test a single chapter with enhanced validators"""
    print(f"\n{'='*80}")
    print(f"TESTING CHAPTER {chapter_num}: {chapter_path.name}")
    print(f"{'='*80}")
    
    # Read chapter content
    with open(chapter_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Create metadata
    metadata = {
        'funnel_stage': funnel_stage,
        'persona': persona,
        'chapter_num': chapter_num,
        'format': 'chapter'
    }
    
    # Run validator
    validator = ContentValidator()
    is_valid, issues, warnings = validator.validate_content(content, metadata)
    
    # Report results
    print(f"\nVALIDATION RESULTS:")
    print(f"  Valid: {'YES' if is_valid else 'NO'}")
    print(f"  Issues: {len(issues)}")
    print(f"  Warnings: {len(warnings)}")
    
    if issues:
        print(f"\n  ISSUES FOUND:")
        for issue in issues:
            print(f"    - {issue}")
    
    if warnings:
        print(f"\n  WARNINGS:")
        for warning in warnings:
            print(f"    - {warning}")
    
    if not issues and not warnings:
        print(f"\n  ✓ No issues or warnings found!")
    
    # Run quality checklist
    checklist = validator.get_quality_checklist(content, metadata)
    print(f"\n  QUALITY CHECKLIST:")
    for key, value in checklist.items():
        status = "[OK]" if value else "[FAIL]"
        print(f"    {status} {key}")
    
    return {
        'chapter': chapter_num,
        'valid': is_valid,
        'issues': issues,
        'warnings': warnings,
        'checklist': checklist
    }

def main():
    """Test all chapters"""
    base_dir = Path(__file__).parent.parent
    
    chapters = [
        {
            'path': base_dir / 'content' / 'published' / 'book' / 'top_of_funnel' / 'chapter_01_retirement_reality_check.md',
            'num': 1,
            'funnel': 'top_of_funnel',
            'persona': 'engineer_retiree'
        },
        {
            'path': base_dir / 'content' / 'published' / 'book' / 'top_of_funnel' / 'chapter_02_tax_leak_draining_wealth.md',
            'num': 2,
            'funnel': 'top_of_funnel',
            'persona': 'engineer_retiree'
        },
        {
            'path': base_dir / 'content' / 'published' / 'book' / 'mid_funnel' / 'chapter_03_social_security_claiming_strategy.md',
            'num': 3,
            'funnel': 'mid_funnel',
            'persona': 'faith_family_builder'
        },
        {
            'path': base_dir / 'content' / 'published' / 'book' / 'mid_funnel' / 'chapter_04_estate_planning_legacy_protection.md',
            'num': 4,
            'funnel': 'mid_funnel',
            'persona': 'widow_caregiver'
        }
    ]
    
    print("="*80)
    print("ENHANCED VALIDATOR TEST - Chapters 1-4")
    print("="*80)
    
    results = []
    for chapter in chapters:
        if chapter['path'].exists():
            result = test_chapter(
                chapter['path'],
                chapter['num'],
                chapter['funnel'],
                chapter['persona']
            )
            results.append(result)
        else:
            print(f"\n[ERROR] Chapter {chapter['num']} not found: {chapter['path']}")
    
    # Summary
    print(f"\n{'='*80}")
    print("SUMMARY")
    print(f"{'='*80}")
    
    total_issues = sum(len(r['issues']) for r in results)
    total_warnings = sum(len(r['warnings']) for r in results)
    valid_chapters = sum(1 for r in results if r['valid'])
    
    print(f"\nTotal Chapters Tested: {len(results)}")
    print(f"Valid Chapters: {valid_chapters}/{len(results)}")
    print(f"Total Issues Found: {total_issues}")
    print(f"Total Warnings: {total_warnings}")
    
    # Breakdown by issue type
    issue_types = {}
    for result in results:
        for issue in result['issues']:
            issue_type = issue.split(':')[0] if ':' in issue else issue.split('-')[0]
            issue_types[issue_type] = issue_types.get(issue_type, 0) + 1
    
    if issue_types:
        print(f"\nIssue Breakdown:")
        for issue_type, count in sorted(issue_types.items(), key=lambda x: x[1], reverse=True):
            print(f"  - {issue_type}: {count}")
    
    # Warning types
    warning_types = {}
    for result in results:
        for warning in result['warnings']:
            warning_type = warning.split(':')[0] if ':' in warning else warning.split('-')[0]
            warning_types[warning_type] = warning_types.get(warning_type, 0) + 1
    
    if warning_types:
        print(f"\nWarning Breakdown:")
        for warning_type, count in sorted(warning_types.items(), key=lambda x: x[1], reverse=True):
            print(f"  - {warning_type}: {count}")
    
    print(f"\n{'='*80}")
    print("ENHANCED VALIDATOR TEST COMPLETE")
    print(f"{'='*80}\n")

if __name__ == '__main__':
    main()

