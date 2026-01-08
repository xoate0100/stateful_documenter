#!/usr/bin/env python3
"""
Run Prompt and Analyze Generated Content
Generates content from prompt, saves it properly, and runs full analysis
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from scripts.generate_content_with_quality import save_and_validate_content
from services.quality_service import QualityService
from meta_framework.content_quality.content_metadata import ContentMetadata


def main():
    """Generate content from prompt and analyze"""
    
    print("=" * 80)
    print("GENERATE CONTENT FROM PROMPT AND ANALYZE")
    print("=" * 80)
    print()
    
    # Find prompt file
    prompt_file = Path("content/prompts/blog/blog_2026-01-08_secure-act-2.0:-what-engineers_top-of-funnel_engineer-retiree_dfb39ec6_prompt.txt")
    
    if not prompt_file.exists():
        print(f"ERROR: Prompt file not found: {prompt_file}")
        return
    
    print(f"Found prompt: {prompt_file.name}")
    
    # Extract content ID
    content_id = "blog_2026-01-08_secure-act-2.0:-what-engineers_top-of-funnel_engineer-retiree_dfb39ec6"
    
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
    with open(prompt_file, 'r', encoding='utf-8') as f:
        prompt = f.read()
    
    print(f"Prompt length: {len(prompt):,} characters")
    print()
    
    # Check if content already exists
    content_base = Path("content")
    platform = metadata.get('platform', 'blog')
    funnel_stage = metadata.get('funnel_stage', 'top_of_funnel')
    content_dir = content_base / "published" / platform / funnel_stage
    content_file = content_dir / f"{content_id}.md"
    
    if content_file.exists():
        print(f"Content file already exists: {content_file}")
        print("Reading existing content...")
        print()
        
        with open(content_file, 'r', encoding='utf-8') as f:
            content = f.read()
    else:
        print("=" * 80)
        print("CONTENT GENERATION REQUIRED")
        print("=" * 80)
        print()
        print("To generate content:")
        print("1. Open the prompt file in Cursor IDE")
        print(f"   {prompt_file}")
        print("2. Copy the entire prompt")
        print("3. Use Cursor chat to generate content from the prompt")
        print("4. Save the generated content to:")
        print(f"   {content_file}")
        print()
        print("Then run this script again to analyze.")
        print()
        print("Alternatively, paste the generated content here and I'll save it.")
        return
    
    # Analyze content
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
    metrics = quality_report.get('metrics', {})
    for dimension, score in sorted(metrics.items()):
        bar_length = int(score * 20)
        bar = "#" * bar_length + "-" * (20 - bar_length)
        status = "[OK]" if score >= 0.80 else "[WARN]" if score >= 0.70 else "[FAIL]"
        print(f"{status} {dimension:15s} {bar} {score:.2f}")
    
    overall = quality_report.get('overall_score', sum(metrics.values()) / len(metrics) if metrics else 0.0)
    print("-" * 80)
    print(f"Overall Score: {overall:.2f}")
    print()
    
    # Show issues and warnings
    if quality_report.get('issues'):
        print("Issues Found:")
        for issue in quality_report['issues'][:10]:
            print(f"  - {issue}")
        print()
    
    if quality_report.get('warnings'):
        print("Warnings:")
        for warning in quality_report['warnings'][:10]:
            print(f"  - {warning}")
        print()
    
    # Run full validation
    print("=" * 80)
    print("FULL VALIDATION")
    print("=" * 80)
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
            print(f"  - {imp['dimension']}: {imp['current']:.2f} -> {imp['target']:.2f} (gap: {imp['gap']:.2f})")
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
    print("Content is properly organized in:")
    print(f"  - Published: {content_dir}")
    print(f"  - Metadata: {metadata_manager.metadata_dir}")
    print(f"  - Prompt: {prompt_file.parent}")


if __name__ == "__main__":
    main()

