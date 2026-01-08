#!/usr/bin/env python3
"""
Organize Book Content
Reorganizes book content into clear structure with chapter ordering and draft management
"""

import sys
import shutil
from pathlib import Path
from datetime import datetime
import yaml
from typing import Dict, List, Any

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

def analyze_current_content():
    """Analyze current content structure and identify issues"""
    base_dir = Path(__file__).parent.parent
    book_dir = base_dir / "content" / "published" / "book"
    
    issues = {
        'final_chapters': [],
        'draft_files': [],
        'missing_chapters': [],
        'duplicate_chapters': []
    }
    
    # Find all chapter_XX files (final versions)
    for funnel_dir in ['top_of_funnel', 'mid_funnel', 'lower_funnel']:
        funnel_path = book_dir / funnel_dir
        if funnel_path.exists():
            for file in funnel_path.glob('chapter_*.md'):
                chapter_num = extract_chapter_number(file.name)
                if chapter_num:
                    issues['final_chapters'].append({
                        'number': chapter_num,
                        'file': file,
                        'funnel': funnel_dir,
                        'name': file.name
                    })
    
    # Find all draft files (book_*.md)
    for funnel_dir in ['top_of_funnel', 'mid_funnel', 'lower_funnel']:
        funnel_path = book_dir / funnel_dir
        if funnel_path.exists():
            for file in funnel_path.glob('book_*.md'):
                issues['draft_files'].append({
                    'file': file,
                    'funnel': funnel_dir,
                    'name': file.name
                })
    
    # Check for missing chapters
    found_numbers = {ch['number'] for ch in issues['final_chapters']}
    expected_numbers = set(range(1, 7))  # Chapters 1-6
    issues['missing_chapters'] = sorted(expected_numbers - found_numbers)
    
    # Check for duplicates
    chapter_counts = {}
    for ch in issues['final_chapters']:
        num = ch['number']
        chapter_counts[num] = chapter_counts.get(num, 0) + 1
    
    issues['duplicate_chapters'] = [num for num, count in chapter_counts.items() if count > 1]
    
    return issues

def extract_chapter_number(filename: str) -> int:
    """Extract chapter number from filename"""
    import re
    match = re.search(r'chapter_(\d+)', filename, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return None

def create_book_registry(final_chapters: List[Dict]) -> Dict[str, Any]:
    """Create book registry from final chapters"""
    registry = {
        'book_id': 'surewealth_retirement_income_book',
        'title': 'The SureWealth Way: Building Retirement Income That Lasts',
        'status': 'in_progress',
        'total_chapters': len(final_chapters),
        'chapters': {}
    }
    
    # Chapter title mapping
    chapter_titles = {
        1: 'Retirement Reality Check',
        2: 'The Tax Leak Draining Your Wealth',
        3: 'Social Security: The Claiming Strategy Most People Miss',
        4: 'Protecting Your Legacy: Estate Planning That Works',
        5: 'Healthcare and Longevity: Planning for the Unknown',
        6: 'Real Outcomes: From Crisis to Confidence'
    }
    
    # Funnel stage mapping
    funnel_mapping = {
        1: 'top_of_funnel',
        2: 'top_of_funnel',
        3: 'mid_funnel',
        4: 'mid_funnel',
        5: 'mid_funnel',
        6: 'lower_funnel'
    }
    
    for ch in sorted(final_chapters, key=lambda x: x['number']):
        num = ch['number']
        registry['chapters'][f'chapter_{num:02d}'] = {
            'number': num,
            'title': chapter_titles.get(num, 'Unknown'),
            'filename': ch['name'],
            'status': 'approved',
            'version': 1,
            'funnel_stage': funnel_mapping.get(num, 'unknown'),
            'last_updated': datetime.now().strftime('%Y-%m-%d'),
            'current_path': str(ch['file'].relative_to(Path(__file__).parent.parent)),
            'target_path': f'content/published/book/chapters/chapter_{num:02d}_{chapter_titles.get(num, "unknown").lower().replace(" ", "_").replace(":", "").replace(",", "")}.md'
        }
    
    return registry

def organize_content(dry_run: bool = False):
    """Organize book content into proper structure"""
    base_dir = Path(__file__).parent.parent
    
    # Analyze current content
    print("="*80)
    print("ANALYZING CURRENT CONTENT STRUCTURE")
    print("="*80)
    issues = analyze_current_content()
    
    print(f"\nFinal Chapters Found: {len(issues['final_chapters'])}")
    for ch in sorted(issues['final_chapters'], key=lambda x: x['number']):
        print(f"  Chapter {ch['number']}: {ch['name']} ({ch['funnel']})")
    
    print(f"\nDraft Files Found: {len(issues['draft_files'])}")
    print(f"  Total draft files to archive: {len(issues['draft_files'])}")
    
    if issues['missing_chapters']:
        print(f"\n[WARN] Missing Chapters: {issues['missing_chapters']}")
    
    if issues['duplicate_chapters']:
        print(f"\n[WARN] Duplicate Chapters: {issues['duplicate_chapters']}")
    
    # Create new directory structure
    chapters_dir = base_dir / "content" / "published" / "book" / "chapters"
    drafts_archive = base_dir / "content" / "drafts" / "book" / "archive"
    index_dir = base_dir / "content" / "index"
    
    if not dry_run:
        chapters_dir.mkdir(parents=True, exist_ok=True)
        drafts_archive.mkdir(parents=True, exist_ok=True)
        index_dir.mkdir(parents=True, exist_ok=True)
    
    # Create book registry
    print("\n" + "="*80)
    print("CREATING BOOK REGISTRY")
    print("="*80)
    registry = create_book_registry(issues['final_chapters'])
    
    registry_file = index_dir / "book_registry.yaml"
    if not dry_run:
        with open(registry_file, 'w', encoding='utf-8') as f:
            yaml.dump(registry, f, default_flow_style=False, sort_keys=False)
        print(f"\n[OK] Book registry created: {registry_file}")
    else:
        print(f"\n[DRY RUN] Would create: {registry_file}")
    
    # Move final chapters to organized structure
    print("\n" + "="*80)
    print("ORGANIZING FINAL CHAPTERS")
    print("="*80)
    
    for ch in sorted(issues['final_chapters'], key=lambda x: x['number']):
        num = ch['number']
        source_file = ch['file']
        
        # Get target filename from registry
        target_filename = registry['chapters'][f'chapter_{num:02d}']['target_path'].split('/')[-1]
        target_file = chapters_dir / target_filename
        
        if not dry_run:
            if target_file.exists():
                print(f"[WARN] Target exists, backing up: {target_file}")
                backup = target_file.with_suffix('.md.bak')
                shutil.copy2(target_file, backup)
            
            shutil.copy2(source_file, target_file)
            print(f"[OK] Chapter {num}: {source_file.name} -> {target_file.name}")
        else:
            print(f"[DRY RUN] Would move: {source_file.name} -> {target_file.name}")
    
    # Archive draft files
    print("\n" + "="*80)
    print("ARCHIVING DRAFT FILES")
    print("="*80)
    
    for draft in issues['draft_files']:
        source_file = draft['file']
        # Create archive path preserving structure
        archive_path = drafts_archive / source_file.name
        
        if not dry_run:
            shutil.copy2(source_file, archive_path)
            print(f"[OK] Archived: {source_file.name}")
        else:
            print(f"[DRY RUN] Would archive: {source_file.name}")
    
    # Generate summary
    print("\n" + "="*80)
    print("ORGANIZATION SUMMARY")
    print("="*80)
    print(f"\nFinal Chapters: {len(issues['final_chapters'])}")
    print(f"Draft Files Archived: {len(issues['draft_files'])}")
    print(f"Book Registry: {registry_file}")
    print(f"Chapters Directory: {chapters_dir}")
    print(f"Drafts Archive: {drafts_archive}")
    
    if not dry_run:
        print("\n[OK] Content organization complete!")
        print("\nNext steps:")
        print("1. Review organized chapters in: content/published/book/chapters/")
        print("2. Verify book registry: content/index/book_registry.yaml")
        print("3. Run: python scripts/compile_book.py --format pdf")
    else:
        print("\n[DRY RUN] No files were moved. Run without --dry-run to execute.")

def main():
    """Main function"""
    import argparse
    parser = argparse.ArgumentParser(description='Organize book content into clear structure')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done without making changes')
    args = parser.parse_args()
    
    organize_content(dry_run=args.dry_run)

if __name__ == '__main__':
    main()

