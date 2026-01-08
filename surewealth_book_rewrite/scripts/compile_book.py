#!/usr/bin/env python3
"""
Compile Book
Compiles all approved chapters into a single book document with table of contents
"""

import sys
from pathlib import Path
from datetime import datetime
import yaml
from typing import Dict, List, Any

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

def load_book_registry() -> Dict[str, Any]:
    """Load book registry"""
    base_dir = Path(__file__).parent.parent
    registry_file = base_dir / "content" / "index" / "book_registry.yaml"
    
    if not registry_file.exists():
        print(f"❌ Book registry not found: {registry_file}")
        print("Run: python scripts/organize_book_content.py first")
        sys.exit(1)
    
    with open(registry_file, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def generate_table_of_contents(registry: Dict[str, Any]) -> str:
    """Generate table of contents from registry"""
    toc = "# Table of Contents\n\n"
    
    chapters = sorted(
        registry['chapters'].values(),
        key=lambda x: x['number']
    )
    
    for ch in chapters:
        if ch['status'] in ['approved', 'published']:
            toc += f"{ch['number']}. {ch['title']}\n"
    
    return toc

def compile_chapters(registry: Dict[str, Any], base_dir: Path) -> str:
    """Compile all approved chapters into single document"""
    book_content = []
    
    # Add title page
    book_content.append(f"# {registry['title']}\n\n")
    book_content.append(f"*Generated: {datetime.now().strftime('%B %d, %Y')}*\n\n")
    book_content.append("---\n\n")
    
    # Add table of contents
    book_content.append(generate_table_of_contents(registry))
    book_content.append("\n---\n\n")
    
    # Add chapters in order
    chapters = sorted(
        registry['chapters'].values(),
        key=lambda x: x['number']
    )
    
    for ch in chapters:
        if ch['status'] in ['approved', 'published']:
            # Try to find chapter file
            chapter_file = base_dir / ch.get('target_path', ch.get('current_path', ''))
            
            if not chapter_file.exists():
                # Try alternative paths
                chapters_dir = base_dir / "content" / "published" / "book" / "chapters"
                chapter_file = chapters_dir / ch['filename']
            
            if chapter_file.exists():
                with open(chapter_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Add chapter header if not present
                    if not content.startswith('#'):
                        book_content.append(f"# Chapter {ch['number']}: {ch['title']}\n\n")
                    book_content.append(content)
                    book_content.append("\n\n---\n\n")
            else:
                print(f"⚠️  Warning: Chapter {ch['number']} file not found: {chapter_file}")
                book_content.append(f"# Chapter {ch['number']}: {ch['title']}\n\n")
                book_content.append("*[Chapter content not found]*\n\n")
    
    return ''.join(book_content)

def export_book(content: str, output_file: Path, format_type: str = 'markdown'):
    """Export book to specified format"""
    if format_type == 'markdown':
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] Book exported to: {output_file}")
    elif format_type == 'pdf':
        # Would require pandoc or similar
        print("⚠️  PDF export requires pandoc. Exporting as markdown instead.")
        export_book(content, output_file.with_suffix('.md'), 'markdown')
    else:
        print(f"⚠️  Format '{format_type}' not yet supported. Exporting as markdown.")
        export_book(content, output_file.with_suffix('.md'), 'markdown')

def main():
    """Main function"""
    import argparse
    parser = argparse.ArgumentParser(description='Compile book from chapters')
    parser.add_argument('--format', default='markdown', choices=['markdown', 'pdf', 'docx'],
                       help='Output format (default: markdown)')
    parser.add_argument('--output', help='Output filename (default: auto-generated)')
    args = parser.parse_args()
    
    base_dir = Path(__file__).parent.parent
    
    # Load registry
    print("Loading book registry...")
    registry = load_book_registry()
    
    # Compile chapters
    print("Compiling chapters...")
    book_content = compile_chapters(registry, base_dir)
    
    # Generate output filename
    if args.output:
        output_file = Path(args.output)
    else:
        book_slug = registry['title'].lower().replace(' ', '_').replace(':', '').replace(',', '')
        output_file = base_dir / "content" / "published" / "book" / f"{book_slug}_compiled.md"
    
    # Export
    print(f"Exporting to {args.format}...")
    export_book(book_content, output_file, args.format)
    
    print(f"\n[OK] Book compilation complete!")
    print(f"   Output: {output_file}")
    print(f"   Chapters: {len([ch for ch in registry['chapters'].values() if ch['status'] in ['approved', 'published']])}")
    print(f"   Total words: ~{sum(ch.get('word_count', 0) for ch in registry['chapters'].values())}")

if __name__ == '__main__':
    main()

