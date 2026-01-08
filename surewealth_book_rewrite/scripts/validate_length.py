#!/usr/bin/env python3
"""
Length Validation Script
Validates content length and provides detailed analysis
"""

import sys
import re
from pathlib import Path
from typing import Dict, Any

def count_words(text: str) -> int:
    """Count words in text"""
    return len(re.findall(r'\b\w+\b', text))

def validate_length(content: str, expected_length: str) -> Dict[str, Any]:
    """
    Validate content length against expected length
    
    Args:
        content: Content to validate
        expected_length: Expected length specification (e.g., "3000-4000 words")
    
    Returns:
        Validation results dictionary
    """
    word_count = count_words(content)
    
    # Parse expected length
    if '-' in expected_length:
        min_words, max_words = map(int, expected_length.replace(' words', '').split('-'))
    else:
        min_words = int(expected_length.replace(' words', '').replace('word', '').strip())
        max_words = min_words
    
    target_words = (min_words + max_words) // 2
    
    # Determine status
    if word_count < min_words:
        status = "REJECT"
        gap = min_words - word_count
        gap_pct = (gap / min_words * 100) if min_words > 0 else 0
        message = f"Content too short - {word_count:,} words (expected {min_words:,}-{max_words:,}). Gap: {gap:,} words ({gap_pct:.1f}% short)."
    elif word_count > max_words:
        status = "WARN"
        excess = word_count - max_words
        excess_pct = (excess / max_words * 100) if max_words > 0 else 0
        message = f"Content exceeds maximum - {word_count:,} words (expected {min_words:,}-{max_words:,}). Excess: {excess:,} words ({excess_pct:.1f}% over)."
    elif word_count < target_words:
        status = "WARN"
        gap = target_words - word_count
        message = f"Content below target - {word_count:,} words (target: ~{target_words:,} words). Consider expanding by {gap:,} words."
    else:
        status = "PASS"
        message = f"Content length acceptable - {word_count:,} words (expected {min_words:,}-{max_words:,})."
    
    return {
        'status': status,
        'word_count': word_count,
        'expected_min': min_words,
        'expected_max': max_words,
        'target': target_words,
        'message': message,
        'is_valid': status in ["PASS", "WARN"]  # Only reject if below minimum
    }

def main():
    """Main function for command-line usage"""
    import argparse
    parser = argparse.ArgumentParser(description='Validate content length')
    parser.add_argument('--content-file', required=True, help='Path to content file')
    parser.add_argument('--expected-length', required=True, help='Expected length (e.g., "3000-4000 words")')
    args = parser.parse_args()
    
    content_file = Path(args.content_file)
    if not content_file.exists():
        print(f"Error: File not found: {content_file}")
        sys.exit(1)
    
    content = content_file.read_text(encoding='utf-8')
    result = validate_length(content, args.expected_length)
    
    print(f"Length Validation Results:")
    print(f"  Status: {result['status']}")
    print(f"  Word Count: {result['word_count']:,}")
    print(f"  Expected: {result['expected_min']:,}-{result['expected_max']:,} words")
    print(f"  Target: ~{result['target']:,} words")
    print(f"  Message: {result['message']}")
    print(f"  Valid: {'Yes' if result['is_valid'] else 'No'}")
    
    if result['status'] == "REJECT":
        sys.exit(1)
    elif result['status'] == "WARN":
        sys.exit(0)  # Warning but not fatal
    else:
        sys.exit(0)

if __name__ == '__main__':
    main()

