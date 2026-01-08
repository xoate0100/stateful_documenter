#!/usr/bin/env python3
"""
Full Workflow Demonstration
Shows complete blog post generation using new microservices system
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


def main():
    """Demonstrate full blog post generation workflow"""
    
    print("=" * 80)
    print("BLOG POST GENERATION - FULL WORKFLOW DEMONSTRATION")
    print("=" * 80)
    print()
    
    # Step 1: Research trending topic
    print("STEP 1: Research Trending Topic")
    print("-" * 80)
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
    
    # Step 2: Generate prompt
    print("STEP 2: Generate Prompt Using PromptBuilder")
    print("-" * 80)
    builder = PromptBuilder()
    
    # Use chapter format for blog post (similar structure)
    prompt = builder.build_prompt(
        format_type="chapter",  # Use chapter format for blog post
        topic=trending_topic,
        persona="engineer_retiree",
        length="1500-2000 words",
        emotional_goal="curiosity",
        validate=True
    )
    
    print("Prompt generated successfully")
    print(f"Prompt length: {len(prompt)} characters")
    print()
    print("Key Prompt Elements:")
    print("  - Format: chapter (used for blog post)")
    print("  - Persona: engineer_retiree")
    print("  - Length: 1500-2000 words")
    print("  - Emotional goal: curiosity")
    print("  - Includes: compliance rules, citations, current scenarios")
    print()
    
    # Step 3: Generate content structure
    print("STEP 3: Generate Content Structure")
    print("-" * 80)
    result = generate_content(
        topic=trending_topic,
        format_type="chapter",  # Use chapter format for blog post
        platform="blog",
        funnel_stage="top_of_funnel",
        persona="engineer_retiree",
        emotional_goal="curiosity",
        length="1500-2000 words",
        narrative_id=None,
        character_ids=None,
        output_content=False  # Just generate prompt and metadata
    )
    
    print("Content structure generated")
    print(f"Content ID: {result['content_id']}")
    print(f"Prompt saved: {result['file_paths']['prompt']}")
    print(f"Metadata saved: {result['file_paths']['metadata']}")
    print()
    
    # Step 4: Show what would happen with AI generation
    print("STEP 4: AI Content Generation (Simulated)")
    print("-" * 80)
    print("In Cursor IDE, you would now:")
    print("  1. Use the generated prompt with Cursor chat")
    print("  2. Cursor AI generates the blog post content")
    print("  3. Content is saved and validated")
    print()
    print("Example Cursor Chat Request:")
    print(f'  "{prompt[:200]}..."')
    print()
    
    # Step 5: Show quality validation workflow
    print("STEP 5: Quality Validation Workflow")
    print("-" * 80)
    print("After content is generated, the system would:")
    print("  1. Run ContentValidator (checks compliance, length, etc.)")
    print("  2. Run BookValidator (checks narratives, characters, CTAs)")
    print("  3. Run QualityService (quantifies quality scores)")
    print("  4. Identify improvements needed")
    print("  5. Use agentic chat to suggest improvements")
    print("  6. Refine prompt and regenerate if needed")
    print()
    
    # Step 6: Show improvement workflow
    print("STEP 6: Improvement Workflow (Using Cursor Agent)")
    print("-" * 80)
    print("In Cursor IDE, you can improve content:")
    print()
    print("Example 1: Improve specific dimension")
    print('  agent.improve(content, "add curiosity gaps and enhance emotional tone")')
    print()
    print("Example 2: Targeted edit")
    print('  agent.edit(content, "fix phrase repetition on line 45", scope="targeted")')
    print()
    print("Example 3: Comprehensive improvement")
    print('  agent.edit(content, "improve all CTAs to be more engaging", scope="comprehensive")')
    print()
    print("Example 4: Quality check")
    print('  report = agent.quality_check(content)')
    print('  print(f"Scores: {report[\'metrics\']}")')
    print('  print(f"Suggestions: {report[\'intelligent_suggestions\']}")')
    print()
    
    # Summary
    print("=" * 80)
    print("WORKFLOW SUMMARY")
    print("=" * 80)
    print()
    print("1. Research trending topic")
    print("2. Generate prompt using PromptBuilder")
    print("3. Generate content structure and metadata")
    print("4. Use Cursor IDE chat to generate content from prompt")
    print("5. Validate content quality")
    print("6. Use Cursor agent to improve/edit content")
    print("7. Save final content with metadata")
    print()
    print("Key Files Generated:")
    print(f"  - Prompt: {result['file_paths']['prompt']}")
    print(f"  - Metadata: {result['file_paths']['metadata']}")
    print()
    print("Next Steps:")
    print("  1. Open the prompt file in Cursor IDE")
    print("  2. Use Cursor chat to generate content from the prompt")
    print("  3. Use agent.improve() and agent.edit() to refine content")
    print("  4. Use agent.quality_check() to validate final quality")
    print()


if __name__ == "__main__":
    main()

