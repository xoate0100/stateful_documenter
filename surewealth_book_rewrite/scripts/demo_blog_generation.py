#!/usr/bin/env python3
"""
Demonstration: Generate Blog Post Using New Microservices System
Shows the full workflow with iterative improvement
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from services.cursor_wrapper import CursorContentWrapper
from services.quality_service import QualityService
from ai_prompts.prompt_builder import PromptBuilder
from meta_framework.content_quality.content_metadata import ContentMetadata


def simulate_cursor_chat(prompt: str) -> str:
    """
    Simulate Cursor chat function
    In real usage, this would be Cursor IDE's chat agent
    """
    # For demo, we'll use the PromptBuilder to generate content
    # In real Cursor IDE, this would call the actual chat agent
    
    # Use existing prompt builder to generate content
    pb = PromptBuilder()
    
    # Parse prompt to extract requirements
    if "blog post" in prompt.lower() or "blog" in prompt.lower():
        format_type = "blog_post"
    elif "chapter" in prompt.lower():
        format_type = "chapter"
    else:
        format_type = "blog_post"
    
    # Extract topic from prompt
    topic = "SECURE Act 2.0 Retirement Changes"
    if "SECURE Act" in prompt or "Secure Act" in prompt:
        topic = "SECURE Act 2.0 Retirement Changes"
    elif "inflation" in prompt.lower():
        topic = "Inflation Impact on Retirement"
    elif "healthcare" in prompt.lower():
        topic = "Healthcare Costs in Retirement"
    
    # Build prompt using PromptBuilder
    full_prompt = pb.build_prompt(
        format_type=format_type,
        topic=topic,
        persona="engineer_retiree",
        length="1500-2000 words",
        emotional_goal="curiosity",
        funnel_stage="top_of_funnel"
    )
    
    # In real usage, this would call Cursor's AI chat
    # For demo, return the prompt (in real usage, AI would generate content)
    return f"[AI Generated Content Based on Prompt]\n\n{full_prompt[:500]}...\n\n[Content would be generated here by Cursor AI]"


def main():
    """Demonstrate blog post generation with new system"""
    
    print("=" * 80)
    print("DEMONSTRATION: Blog Post Generation with Microservices System")
    print("=" * 80)
    print()
    
    # Initialize system
    print("1. Initializing Cursor Content Agent...")
    agent = CursorContentWrapper(simulate_cursor_chat)
    print("   ✓ Agent initialized")
    print()
    
    # Research trending topic
    print("2. Researching Trending Topic...")
    trending_topic = "SECURE Act 2.0 Changes and Their Impact on Retirement Planning in 2026"
    print(f"   ✓ Topic: {trending_topic}")
    print("   ✓ Research findings:")
    print("     - RMD age increased to 73 (2023) and will rise to 75 (2033)")
    print("     - Catch-up contributions for ages 60-63 increased")
    print("     - New Roth catch-up requirement for high earners")
    print("     - Legislators expressed concerns about retirement readiness")
    print()
    
    # Generate blog post
    print("3. Generating Blog Post...")
    print("   Request: Generate blog post about SECURE Act 2.0 changes for engineers")
    print()
    
    request = f"""
    Generate a blog post about {trending_topic} for engineers approaching retirement.
    Length: 1500-2000 words
    Funnel stage: Top of funnel
    Persona: Engineer retiree
    Focus on: How these changes affect retirement planning, what engineers need to know,
    and actionable insights for 2026.
    """
    
    # For demo, we'll use the existing generation system
    from scripts.generate_content_with_quality import generate_content
    
    print("   Generating initial content...")
    result = generate_content(
        topic=trending_topic,
        format_type="blog_post",
        platform="blog",
        funnel_stage="top_of_funnel",
        persona="engineer_retiree",
        emotional_goal="curiosity",
        length="1500-2000 words"
    )
    
    if result and result.get('content'):
        content = result['content']
        print(f"   ✓ Initial content generated ({len(content)} characters)")
        print()
        
        # Quality check
        print("4. Quality Check...")
        quality_service = QualityService()
        quality_report = quality_service.quantify_quality(
            content,
            {
                'format_type': 'blog_post',
                'funnel_stage': 'top_of_funnel',
                'persona': 'engineer_retiree'
            }
        )
        
        print("   Quality Scores:")
        for dimension, score in quality_report['metrics'].items():
            status = "✓" if score >= 0.80 else "⚠" if score >= 0.70 else "✗"
            print(f"     {status} {dimension}: {score:.2f}")
        print()
        
        overall_score = sum(quality_report['metrics'].values()) / len(quality_report['metrics'])
        print(f"   Overall Score: {overall_score:.2f}")
        print()
        
        # Identify improvements needed
        print("5. Identifying Improvements...")
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
            current = quality_report['metrics'].get(dimension, 0.0)
            if current < target - 0.05:
                gap = target - current
                improvements_needed.append({
                    'dimension': dimension,
                    'current': current,
                    'target': target,
                    'gap': gap
                })
        
        if improvements_needed:
            print("   Improvements needed:")
            for imp in improvements_needed[:3]:  # Top 3
                print(f"     - {imp['dimension']}: {imp['current']:.2f} → {imp['target']:.2f} (gap: {imp['gap']:.2f})")
        else:
            print("   ✓ All quality targets met!")
        print()
        
        # Show how to improve (simulated)
        print("6. Improvement Process (Simulated)...")
        if improvements_needed:
            top_improvement = improvements_needed[0]
            print(f"   Improving: {top_improvement['dimension']}")
            print(f"   Current score: {top_improvement['current']:.2f}")
            print(f"   Target score: {top_improvement['target']:.2f}")
            print()
            print("   Agentic Chat Analysis:")
            print(f"     Issue: {top_improvement['dimension']} quality below target")
            print(f"     Root cause: [Analyzed via agentic chat]")
            print(f"     Recommendation: [Generated via agentic chat]")
            print(f"     Expected improvement: +{top_improvement['gap']:.2f}")
            print()
            print("   Prompt Refinement:")
            print("     [Prompt refined with specific instructions]")
            print("     [Content regenerated with improvements]")
            print()
            print("   Re-validation:")
            print(f"     New score: {top_improvement['current'] + top_improvement['gap'] * 0.7:.2f} (improved)")
            print()
        
        # Save content
        print("7. Saving Content...")
        output_dir = Path("content/published/blog")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        from datetime import datetime
        filename = f"blog_{datetime.now().strftime('%Y%m%d')}_secure-act-2-0-changes.md"
        output_file = output_dir / filename
        
        # Create metadata
        metadata_manager = ContentMetadata()
        content_id = f"blog_{datetime.now().strftime('%Y%m%d')}_secure-act-2-0"
        metadata = metadata_manager.create_metadata(
            content_id=content_id,
            title=trending_topic,
            format_type="blog_post",
            platform="blog",
            funnel_stage="top_of_funnel",
            user_intent="researching",
            persona="engineer_retiree",
            topic="secure_act_2_0",
            tags=["secure act 2.0", "retirement", "rmd", "tax planning", "2026"],
            emotional_goal="curiosity",
            word_count=len(content.split())
        )
        
        # Save content
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Save metadata
        metadata_manager.save_metadata(metadata)
        
        print(f"   ✓ Content saved: {output_file}")
        print(f"   ✓ Metadata saved: {metadata_manager.metadata_dir / f'{content_id}.yaml'}")
        print()
        
        # Summary
        print("=" * 80)
        print("GENERATION COMPLETE")
        print("=" * 80)
        print(f"Topic: {trending_topic}")
        print(f"Length: {len(content.split())} words")
        print(f"Quality Score: {overall_score:.2f}")
        print(f"Output: {output_file}")
        print()
        print("Next Steps:")
        print("  - Review content quality")
        print("  - Use agent.improve() to enhance specific dimensions")
        print("  - Use agent.edit() for targeted improvements")
        print("  - Use agent.quality_check() for detailed analysis")
        
    else:
        print("   ✗ Content generation failed")
        print("   (This is a demo - in real usage, Cursor AI would generate content)")


if __name__ == "__main__":
    main()

