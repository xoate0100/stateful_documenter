#!/usr/bin/env python3
"""
Generate Blog Post from Prompt and Analyze Content
Uses the generated prompt to create content and run full analysis
"""

import sys
from pathlib import Path
from datetime import datetime

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from scripts.generate_content_with_quality import save_and_validate_content
from services.quality_service import QualityService
from meta_framework.content_quality.content_metadata import ContentMetadata
from meta_framework.content_quality.content_index import ContentIndex


def generate_content_from_prompt(prompt_file: Path) -> str:
    """
    Generate content from prompt file
    In real usage, this would call Cursor AI chat
    For demo, we'll create a placeholder that shows the structure
    """
    # Read prompt
    with open(prompt_file, 'r', encoding='utf-8') as f:
        prompt = f.read()
    
    # In real usage, this would be:
    # content = cursor_chat(prompt)
    # For now, we'll note that content needs to be generated
    
    # Return a note that content generation is needed
    return None


def main():
    """Generate and analyze blog post"""
    
    print("=" * 80)
    print("BLOG POST GENERATION AND ANALYSIS")
    print("=" * 80)
    print()
    
    # Find the prompt file
    prompt_dir = Path("content/prompts/blog")
    prompt_files = list(prompt_dir.glob("*secure-act-2.0*_prompt.txt"))
    
    if not prompt_files:
        print("ERROR: Prompt file not found")
        print(f"Looking in: {prompt_dir}")
        return
    
    prompt_file = prompt_files[0]
    print(f"Found prompt: {prompt_file.name}")
    print()
    
    # Extract content ID from prompt filename
    content_id = prompt_file.stem.replace("_prompt", "")
    
    # Load metadata
    metadata_manager = ContentMetadata()
    metadata = metadata_manager.load_metadata(content_id)
    
    if not metadata:
        print(f"ERROR: Metadata not found for {content_id}")
        return
    
    print(f"Content ID: {content_id}")
    print(f"Topic: {metadata.get('title', 'N/A')}")
    print()
    
    # Read prompt
    print("Reading prompt...")
    with open(prompt_file, 'r', encoding='utf-8') as f:
        prompt = f.read()
    
    print(f"Prompt length: {len(prompt):,} characters")
    print()
    
    # Note: In real usage, content would be generated here via Cursor AI
    print("=" * 80)
    print("CONTENT GENERATION REQUIRED")
    print("=" * 80)
    print()
    print("To generate content:")
    print("1. Open the prompt file in Cursor IDE")
    print(f"2. File: {prompt_file}")
    print("3. Use Cursor chat to generate content from the prompt")
    print("4. Save the generated content")
    print()
    print("Then run this script again with the content file, or:")
    print("  python scripts/analyze_content.py <content_file>")
    print()
    
    # Check if content file already exists
    content_base = Path("content")
    platform = metadata.get('platform', 'blog')
    funnel_stage = metadata.get('funnel_stage', 'top_of_funnel')
    content_dir = content_base / "published" / platform / funnel_stage
    content_file = content_dir / f"{content_id}.md"
    
    if content_file.exists():
        print(f"Found existing content: {content_file}")
        print()
        print("Analyzing existing content...")
        print()
        
        # Read content
        with open(content_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        word_count = len(content.split())
        print(f"Content length: {word_count:,} words")
        print()
        
        # Run quality analysis
        print("=" * 80)
        print("QUALITY ANALYSIS")
        print("=" * 80)
        print()
        
        quality_service = QualityService()
        quality_report = quality_service.quantify_quality(
            content,
            metadata
        )
        
        print("Quality Scores:")
        print("-" * 80)
        metrics = quality_report['metrics']
        for dimension, score in sorted(metrics.items()):
            bar_length = int(score * 20)
            bar = "█" * bar_length + "░" * (20 - bar_length)
            status = "[OK]" if score >= 0.80 else "[WARN]" if score >= 0.70 else "[FAIL]"
            print(f"{status} {dimension:15s} {bar} {score:.2f}")
        
        overall = quality_report.get('overall_score', sum(metrics.values()) / len(metrics))
        print("-" * 80)
        print(f"Overall Score: {overall:.2f}")
        print()
        
        # Show issues and warnings
        if quality_report.get('issues'):
            print("Issues Found:")
            for issue in quality_report['issues'][:5]:
                print(f"  - {issue}")
            print()
        
        if quality_report.get('warnings'):
            print("Warnings:")
            for warning in quality_report['warnings'][:5]:
                print(f"  - {warning}")
            print()
        
        # Validate and save
        print("Running full validation...")
        print()
        
        validation_result = save_and_validate_content(
            content_id=content_id,
            content=content,
            chapter_num=None
        )
        
        if validation_result:
            print("Validation Results:")
            print(f"  Content valid: {validation_result.get('is_valid', False)}")
            print(f"  Issues: {len(validation_result.get('issues', []))}")
            print(f"  Warnings: {len(validation_result.get('warnings', []))}")
            print()
            
            if validation_result.get('file_paths'):
                print("Files Updated:")
                for key, path in validation_result['file_paths'].items():
                    if path:
                        print(f"  - {key}: {path}")
            print()
        
        # Show improvement suggestions
        print("=" * 80)
        print("IMPROVEMENT SUGGESTIONS")
        print("=" * 80)
        print()
        
        target_metrics = {
            "structural": 0.95,
            "sales_copy": 0.90,
            "emotional": 0.85,
            "conversion": 0.90,
            "authority": 0.85,
            "trust": 0.90
        }
        
        improvements_needed = []
        for dimension, target in target_metrics.items():
            current = metrics.get(dimension, 0.0)
            if current < target - 0.05:
                gap = target - current
                improvements_needed.append({
                    'dimension': dimension,
                    'current': current,
                    'target': target,
                    'gap': gap
                })
        
        if improvements_needed:
            print("Improvements needed:")
            for imp in improvements_needed:
                print(f"  - {imp['dimension']}: {imp['current']:.2f} → {imp['target']:.2f} (gap: {imp['gap']:.2f})")
                print(f"    Use: agent.improve(content, 'improve {imp['dimension']} quality')")
            print()
        else:
            print("All quality targets met!")
            print()
        
        print("=" * 80)
        print("ANALYSIS COMPLETE")
        print("=" * 80)
        print()
        print(f"Content file: {content_file}")
        print(f"Metadata: {metadata_manager.metadata_dir / f'{content_id}.yaml'}")
        print(f"Quality score: {overall:.2f}")
        print()
        print("Next steps:")
        print("  - Review content quality scores")
        print("  - Use agent.improve() for any needed improvements")
        print("  - Use agent.edit() for targeted fixes")
        
    else:
        print("Content file not found. Content needs to be generated first.")
        print()
        print("To generate content:")
        print("1. Open prompt in Cursor IDE:")
        print(f"   {prompt_file}")
        print("2. Use Cursor chat to generate content from the prompt")
        print("3. Save content to:")
        print(f"   {content_file}")
        print("4. Run this script again to analyze")


if __name__ == "__main__":
    main()

