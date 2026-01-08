#!/usr/bin/env python3
"""
Generate Blog Post Using New Microservices System
Demonstrates full workflow with trending topic
"""

import sys
from pathlib import Path
from datetime import datetime

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from ai_prompts.prompt_builder import PromptBuilder
from scripts.generate_content_with_quality import generate_content
from services.quality_service import QualityService
from meta_framework.content_quality.content_metadata import ContentMetadata


def main():
    """Generate blog post about trending topic"""
    
    print("=" * 80)
    print("BLOG POST GENERATION DEMONSTRATION")
    print("=" * 80)
    print()
    
    # Trending topic from web research
    trending_topic = (
        "SECURE Act 2.0: What Engineers Need to Know About "
        "Retirement Changes in 2026"
    )
    
    print(f"Topic: {trending_topic}")
    print()
    print("Research Findings:")
    print("  - RMD age increased to 73 (2023) and will rise to 75 (2033)")
    print("  - Catch-up contributions for ages 60-63 increased to $11,250 (2025)")
    print("  - New Roth catch-up requirement for high earners (2026)")
    print("  - Legislators expressed serious concerns about retirement readiness")
    print("  - Full Retirement Age (FRA) now 67 for those born in 1960 or later")
    print()
    
    # Generate content
    print("Generating blog post...")
    print()
    
    result = generate_content(
        topic=trending_topic,
        format_type="blog_post",
        platform="blog",
        funnel_stage="top_of_funnel",
        persona="engineer_retiree",
        emotional_goal="curiosity",
        length="1500-2000 words",
        narrative_id=None,
        character_ids=None
    )
    
    if result and result.get('content'):
        content = result['content']
        word_count = len(content.split())
        
        print(f"✓ Content generated: {word_count} words")
        print()
        
        # Quality check
        print("Running quality check...")
        quality_service = QualityService()
        quality_report = quality_service.quantify_quality(
            content,
            {
                'format_type': 'blog_post',
                'funnel_stage': 'top_of_funnel',
                'persona': 'engineer_retiree'
            }
        )
        
        print()
        print("Quality Scores:")
        print("-" * 80)
        metrics = quality_report['metrics']
        for dimension, score in sorted(metrics.items()):
            bar_length = int(score * 20)
            bar = "█" * bar_length + "░" * (20 - bar_length)
            status = "[OK]" if score >= 0.80 else "[WARN]" if score >= 0.70 else "[FAIL]"
            print(f"{status} {dimension:15s} {bar} {score:.2f}")
        
        overall = quality_report['overall_score']
        print("-" * 80)
        print(f"Overall Score: {overall:.2f}")
        print()
        
        # Save content
        output_dir = Path("content/published/blog")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        timestamp = datetime.now().strftime('%Y%m%d')
        filename = f"blog_{timestamp}_secure-act-2-0-changes.md"
        output_file = output_dir / filename
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Save metadata
        metadata_manager = ContentMetadata()
        content_id = f"blog_{timestamp}_secure-act-2-0"
        metadata = metadata_manager.create_metadata(
            content_id=content_id,
            title=trending_topic,
            format_type="blog_post",
            platform="blog",
            funnel_stage="top_of_funnel",
            user_intent="researching",
            persona="engineer_retiree",
            topic="secure_act_2_0",
            tags=[
                "secure act 2.0",
                "retirement",
                "rmd",
                "tax planning",
                "2026",
                "retirement legislation"
            ],
            emotional_goal="curiosity",
            word_count=word_count
        )
        metadata_manager.save_metadata(metadata)
        
        print(f"✓ Content saved: {output_file}")
        print(f"✓ Metadata saved")
        print()
        
        # Show how to improve
        if overall < 0.85:
            print("Improvement Suggestions:")
            print("-" * 80)
            target_metrics = {
                "structural": 0.95,
                "sales_copy": 0.90,
                "emotional": 0.85,
                "conversion": 0.90,
                "authority": 0.85,
                "trust": 0.90
            }
            
            for dimension, target in target_metrics.items():
                current = metrics.get(dimension, 0.0)
                if current < target - 0.05:
                    print(f"  - {dimension}: {current:.2f} → {target:.2f}")
                    print(f"    Use: agent.improve(content, 'improve {dimension} quality')")
            print()
        
        print("=" * 80)
        print("GENERATION COMPLETE")
        print("=" * 80)
        print(f"File: {output_file}")
        print(f"Quality: {overall:.2f}")
        print()
        print("Next: Use Cursor IDE to improve content:")
        print("  agent.improve(content, 'add curiosity gaps')")
        print("  agent.edit(content, 'improve CTA at end')")
        print("  agent.quality_check(content)")
        
    else:
        print("✗ Content generation failed")
        if result:
            print(f"Error: {result.get('error', 'Unknown error')}")


if __name__ == "__main__":
    main()

