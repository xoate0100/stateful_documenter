#!/usr/bin/env python3
"""
Analyze Book Length
Counts words in each chapter and compares to expected length
"""

import re
from pathlib import Path
import yaml

def count_words(text: str) -> int:
    """Count words in text"""
    return len(re.findall(r'\b\w+\b', text))

def analyze_book_length():
    """Analyze actual vs expected book length"""
    base_dir = Path(__file__).parent.parent
    
    # Load book registry
    registry_file = base_dir / "content" / "index" / "book_registry.yaml"
    with open(registry_file, 'r', encoding='utf-8') as f:
        registry = yaml.safe_load(f)
    
    # Load book structure to get expected lengths
    book_structure_file = base_dir / "scripts" / "generate_book.py"
    with open(book_structure_file, 'r', encoding='utf-8') as f:
        content = f.read()
        # Extract length specifications
        import re
        length_specs = re.findall(r"'length':\s*'([^']+)'", content)
    
    chapters_dir = base_dir / "content" / "published" / "book" / "chapters"
    
    print("="*80)
    print("BOOK LENGTH ANALYSIS")
    print("="*80)
    print()
    
    total_actual = 0
    total_expected_min = 0
    total_expected_max = 0
    
    chapters = sorted(registry['chapters'].items(), key=lambda x: x[1]['number'])
    
    for i, (ch_key, ch_data) in enumerate(chapters):
        ch_num = ch_data['number']
        ch_title = ch_data['title']
        
        # Find chapter file
        chapter_file = chapters_dir / ch_data['filename']
        if not chapter_file.exists():
            # Try alternative filename
            chapter_file = chapters_dir / f"chapter_{ch_num:02d}_{ch_title.lower().replace(' ', '_').replace(':', '').replace(',', '')}.md"
        
        if chapter_file.exists():
            content = chapter_file.read_text(encoding='utf-8')
            word_count = count_words(content)
            total_actual += word_count
            
            # Get expected length
            if i < len(length_specs):
                length_spec = length_specs[i]
                if '-' in length_spec:
                    min_words, max_words = map(int, length_spec.replace(' words', '').split('-'))
                    total_expected_min += min_words
                    total_expected_max += max_words
                    expected_str = f"{min_words:,}-{max_words:,}"
                else:
                    min_words = int(length_spec.replace(' words', ''))
                    max_words = min_words
                    total_expected_min += min_words
                    total_expected_max += max_words
                    expected_str = f"{min_words:,}"
            else:
                expected_str = "Unknown"
                min_words = 3000
                max_words = 4000
                total_expected_min += min_words
                total_expected_max += max_words
            
            # Calculate gap
            gap_min = min_words - word_count
            gap_max = max_words - word_count
            gap_pct = ((min_words - word_count) / min_words * 100) if min_words > 0 else 0
            
            status = "OK" if word_count >= min_words else "SHORT"
            
            print(f"Chapter {ch_num}: {ch_title}")
            print(f"  Expected: {expected_str} words")
            print(f"  Actual:   {word_count:,} words")
            print(f"  Gap:      {gap_min:,} to {gap_max:,} words ({gap_pct:.1f}% short)")
            print(f"  Status:   {status}")
            print()
        else:
            print(f"Chapter {ch_num}: FILE NOT FOUND - {chapter_file}")
            print()
    
    # Summary
    print("="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Total Expected: {total_expected_min:,} - {total_expected_max:,} words")
    print(f"Total Actual:   {total_actual:,} words")
    print(f"Total Gap:      {total_expected_min - total_actual:,} to {total_expected_max - total_actual:,} words")
    print(f"Gap Percentage: {((total_expected_min - total_actual) / total_expected_min * 100):.1f}% short")
    print()
    
    # Page estimates (250 words/page)
    expected_pages_min = total_expected_min / 250
    expected_pages_max = total_expected_max / 250
    actual_pages = total_actual / 250
    
    print(f"Expected Pages: {expected_pages_min:.1f} - {expected_pages_max:.1f} pages")
    print(f"Actual Pages:   {actual_pages:.1f} pages")
    print(f"Page Gap:       {expected_pages_min - actual_pages:.1f} to {expected_pages_max - actual_pages:.1f} pages")
    print()
    
    # With introduction (5 pages = 1,250 words)
    intro_words = 1250
    total_with_intro = total_actual + intro_words
    pages_with_intro = total_with_intro / 250
    
    print(f"With Introduction (+{intro_words:,} words):")
    print(f"  Total Words: {total_with_intro:,}")
    print(f"  Total Pages: {pages_with_intro:.1f}")
    print(f"  Still Short: {expected_pages_min - pages_with_intro:.1f} to {expected_pages_max - pages_with_intro:.1f} pages")
    print()

if __name__ == '__main__':
    analyze_book_length()

