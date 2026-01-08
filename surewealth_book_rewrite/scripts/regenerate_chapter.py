#!/usr/bin/env python3
"""
Regenerate Chapter Script
Helper script to validate and save regenerated chapter content
"""

import sys
from pathlib import Path
from typing import Optional

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.generate_book import BookGenerator
from scripts.generate_content_with_quality import save_and_validate_content, count_words


def regenerate_chapter(chapter_num: int, content: str, content_id: Optional[str] = None):
    """
    Regenerate a specific chapter with validation
    
    Args:
        chapter_num: Chapter number (1-6)
        content: AI-generated content
        content_id: Optional content ID (will be found from metadata if not provided)
    """
    generator = BookGenerator()
    
    # Find chapter spec
    chapter_spec = next(
        (c for c in generator.book_structure if c['chapter_num'] == chapter_num),
        None
    )
    
    if not chapter_spec:
        print(f"Error: Chapter {chapter_num} not found")
        return None
    
    print(f"\n{'='*80}")
    print(f"REGENERATING CHAPTER {chapter_num}: {chapter_spec['title']}")
    print(f"{'='*80}\n")
    
    # Quick length check
    word_count = count_words(content)
    expected_length = chapter_spec.get('length', '3000-4000 words')
    
    if '-' in expected_length:
        min_words, max_words = map(int, expected_length.replace(' words', '').split('-'))
    else:
        min_words = int(expected_length.replace(' words', '').replace('word', '').strip())
        max_words = min_words
    
    print(f"Length Check:")
    print(f"  Word Count: {word_count:,}")
    print(f"  Expected: {min_words:,}-{max_words:,} words")
    
    if word_count < min_words:
        gap = min_words - word_count
        gap_pct = (gap / min_words * 100) if min_words > 0 else 0
        print(f"  [FAIL] Content too short - {gap:,} words short ({gap_pct:.1f}%)")
        print(f"  [ACTION] Content will be rejected. Please expand content to at least {min_words:,} words.")
        return {
            'success': False,
            'error': f"Content too short: {word_count:,} words (expected {min_words:,}-{max_words:,})",
            'word_count': word_count,
            'expected_min': min_words,
            'expected_max': max_words,
            'gap': gap
        }
    elif word_count > max_words:
        excess = word_count - max_words
        print(f"  [WARN] Content exceeds maximum by {excess:,} words")
    else:
        print(f"  [OK] Length acceptable")
    
    # Generate prompt and metadata if needed
    if not content_id:
        print(f"\nGenerating prompt and metadata...")
        result = generator.generate_chapter(chapter_spec, generated_content=None)
        content_id = result['generation']['content_id']
        print(f"  Content ID: {content_id}")
    
    # Validate and save
    print(f"\nValidating and saving content...")
    validation = save_and_validate_content(
        content_id=content_id,
        content=content,
        chapter_num=chapter_num
    )
    
    # Check for critical issues
    if validation.get('should_reject') or validation.get('critical_issues'):
        print(f"\n{'='*80}")
        print(f"CONTENT REJECTED - CRITICAL ISSUES FOUND")
        print(f"{'='*80}")
        for issue in validation.get('critical_issues', [])[:5]:
            print(f"  - {issue}")
        if len(validation.get('critical_issues', [])) > 5:
            print(f"  ... and {len(validation['critical_issues']) - 5} more")
        print(f"\n[ACTION] Regenerate content with fixes before proceeding.")
        return {
            'success': False,
            'validation': validation
        }
    
    # Success
    print(f"\n{'='*80}")
    print(f"CHAPTER {chapter_num} REGENERATED SUCCESSFULLY")
    print(f"{'='*80}")
    print(f"  Word Count: {word_count:,}")
    print(f"  Status: Validated and saved")
    print(f"  Issues: {len(validation.get('issues', []))}")
    print(f"  Warnings: {len(validation.get('warnings', []))}")
    print(f"  File: {validation.get('content_file', 'N/A')}")
    
    return {
        'success': True,
        'validation': validation,
        'word_count': word_count
    }


def main():
    """Main function for command-line usage"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Regenerate and validate a chapter')
    parser.add_argument('--chapter', type=int, required=True, help='Chapter number (1-6)')
    parser.add_argument('--content-file', help='Path to file containing generated content')
    parser.add_argument('--content', help='Generated content (if not from file)')
    parser.add_argument('--content-id', help='Content ID (optional, will be found if not provided)')
    
    args = parser.parse_args()
    
    # Get content
    if args.content_file:
        content = Path(args.content_file).read_text(encoding='utf-8')
    elif args.content:
        content = args.content
    else:
        print("Error: Must provide --content-file or --content")
        sys.exit(1)
    
    # Regenerate
    result = regenerate_chapter(
        chapter_num=args.chapter,
        content=content,
        content_id=args.content_id
    )
    
    if result and result.get('success'):
        print("\n[OK] Chapter regeneration complete!")
        sys.exit(0)
    else:
        print("\n[FAIL] Chapter regeneration failed. See errors above.")
        sys.exit(1)


if __name__ == '__main__':
    main()

