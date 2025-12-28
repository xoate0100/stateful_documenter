#!/usr/bin/env python3
"""
Generate Content with Quality Validation
Integrates lessons learned and new content structure
"""

import sys
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from ai_prompts.prompt_builder import PromptBuilder
from meta_framework.content_quality.content_validator import ContentValidator
from meta_framework.content_quality.content_metadata import ContentMetadata
from meta_framework.content_quality.content_index import ContentIndex


def count_words(text: str) -> int:
    """Count words in text"""
    return len(re.findall(r'\b\w+\b', text))


def extract_signature_phrases(content: str, phrases: list) -> list:
    """Extract which signature phrases were used"""
    used = []
    for phrase in phrases:
        if phrase.lower() in content.lower():
            used.append(phrase)
    return used


def count_permission_frames(content: str) -> int:
    """Count permission frames in content"""
    patterns = [
        r"If you don't mind me asking",
        r"Before we go any further",
        r"Let me share something with you",
    ]
    return sum(len(re.findall(pattern, content, re.IGNORECASE)) for pattern in patterns)


def count_ctas(content: str) -> int:
    """Count CTAs in content"""
    patterns = [
        r"## Your Next Step",
        r"\*\*.*?\?\*\*",
        r"Would.*?like to know",
        r"If there were a way",
    ]
    return sum(1 for pattern in patterns if re.search(pattern, content, re.IGNORECASE))


def generate_content(
    topic: str,
    format_type: str,
    platform: str,
    funnel_stage: str,
    persona: str,
    emotional_goal: str,
    narrative_id: Optional[str] = None,
    length: Optional[str] = None,
    output_content: bool = True
) -> Dict[str, Any]:
    """
    Generate content with quality validation and metadata
    
    Returns dict with:
    - prompt: Generated prompt
    - metadata: Content metadata
    - validation: Validation results
    - file_paths: Where files were saved
    """
    
    # Initialize systems
    builder = PromptBuilder()
    validator = ContentValidator()
    metadata_manager = ContentMetadata()
    index_manager = ContentIndex()
    
    # Generate prompt
    print(f"Generating prompt for: {topic}")
    print(f"  Format: {format_type} | Platform: {platform}")
    print(f"  Funnel: {funnel_stage} | Persona: {persona}")
    
    prompt = builder.build_prompt(
        format_type=format_type,
        topic=topic,
        persona=persona,
        length=length,
        emotional_goal=emotional_goal,
        narrative_ids=[narrative_id] if narrative_id else None,
        validate=False
    )
    
    # Generate content ID
    content_id = metadata_manager.generate_content_id(
        platform=platform,
        topic=topic,
        funnel_stage=funnel_stage,
        persona=persona
    )
    
    # Create directory structure
    content_base = Path("content")
    
    # Published vs drafts
    if output_content:
        content_dir = content_base / "published" / platform / funnel_stage
    else:
        content_dir = content_base / "drafts" / platform / funnel_stage
    
    content_dir.mkdir(parents=True, exist_ok=True)
    
    # Prompts directory
    prompts_dir = content_base / "prompts" / platform
    prompts_dir.mkdir(parents=True, exist_ok=True)
    
    # Save prompt
    prompt_file = prompts_dir / f"{content_id}_prompt.txt"
    with open(prompt_file, 'w', encoding='utf-8') as f:
        f.write(prompt)
    
    print(f"  [OK] Prompt saved: {prompt_file}")
    
    # If we have generated content, process it
    file_paths = {
        'prompt': str(prompt_file),
        'content': None,
        'metadata': None
    }
    
    if output_content:
        # For now, just save prompt - content would come from AI
        # In production, this would accept generated content as parameter
        print(f"  [INFO] Content file would be saved to: {content_dir}")
        print(f"  [INFO] Run AI generation with prompt, then call save_content()")
    
    # Create metadata (will be updated when content is saved)
    metadata = metadata_manager.create_metadata(
        content_id=content_id,
        title=topic,
        format_type=format_type,
        platform=platform,
        funnel_stage=funnel_stage,
        user_intent='researching' if funnel_stage == 'top_of_funnel' else 'comparing',
        persona=persona,
        topic=topic.lower().replace(' ', '_'),
        tags=[topic.lower().replace(' ', '_'), funnel_stage, persona],
        emotional_goal=emotional_goal,
        narrative_used=narrative_id,
        cta_type='soft_cta' if funnel_stage in ['top_of_funnel', 'mid_funnel'] else 'primary_cta',
        cta_count=1,  # Will be updated when content is analyzed
        permission_frames_used=0,  # Will be updated when content is analyzed
        word_count=0  # Will be updated when content is analyzed
    )
    
    # Save metadata
    metadata_file = metadata_manager.save_metadata(metadata)
    file_paths['metadata'] = str(metadata_file)
    print(f"  [OK] Metadata saved: {metadata_file}")
    
    # Update content index
    index_manager.add_content(metadata)
    print(f"  [OK] Content index updated")
    
    return {
        'prompt': prompt,
        'metadata': metadata,
        'content_id': content_id,
        'file_paths': file_paths,
        'validation': None  # Will be populated when content is validated
    }


def save_and_validate_content(
    content_id: str,
    content: str,
    signature_phrases: Optional[list] = None
) -> Dict[str, Any]:
    """
    Save generated content and validate it
    
    Returns validation results
    """
    
    validator = ContentValidator()
    metadata_manager = ContentMetadata()
    
    # Load metadata
    metadata = metadata_manager.load_metadata(content_id)
    if not metadata:
        raise ValueError(f"Metadata not found for content_id: {content_id}")
    
    # Analyze content
    word_count = count_words(content)
    permission_frames = count_permission_frames(content)
    cta_count = count_ctas(content)
    
    # Extract signature phrases
    if signature_phrases is None:
        # Load from metadata or framework
        sig_phrases = metadata.get('signature_phrases', [])
    else:
        sig_phrases = extract_signature_phrases(content, signature_phrases)
    
    # Update metadata
    metadata['word_count'] = word_count
    metadata['permission_frames_used'] = permission_frames
    metadata['cta_count'] = cta_count
    metadata['signature_phrases'] = sig_phrases
    metadata['status'] = 'published'
    
    # Save content file
    content_base = Path("content")
    platform = metadata['platform']
    funnel_stage = metadata['funnel_stage']
    content_dir = content_base / "published" / platform / funnel_stage
    content_file = content_dir / f"{content_id}.md"
    
    with open(content_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Validate content
    is_valid, issues, warnings = validator.validate_content(content, metadata)
    
    # Get quality checklist
    checklist = validator.get_quality_checklist(content, metadata)
    
    # Update metadata with validation results
    metadata['validation'] = {
        'is_valid': is_valid,
        'issues': issues,
        'warnings': warnings,
        'checklist': checklist
    }
    
    # Save updated metadata
    metadata_manager.save_metadata(metadata)
    
    # Update index with updated metadata
    index_manager.add_content(metadata)
    
    return {
        'is_valid': is_valid,
        'issues': issues,
        'warnings': warnings,
        'checklist': checklist,
        'content_file': str(content_file),
        'metadata_file': str(metadata_manager.metadata_dir / f"{content_id}.yaml")
    }


def main():
    """Example usage"""
    
    # Example: Generate Facebook post
    result = generate_content(
        topic="The Hidden Tax Leak Draining Your Retirement",
        format_type="social_post",
        platform="facebook",
        funnel_stage="mid_funnel",
        persona="engineer_retiree",
        emotional_goal="curiosity",
        narrative_id="ALLEGORY_LEAKY_BUCKET",
        length="2000-3000 words",
        output_content=False  # Just generate prompt for now
    )
    
    print("\n" + "=" * 70)
    print("Content Generation Complete")
    print("=" * 70)
    print(f"Content ID: {result['content_id']}")
    print(f"Prompt: {result['file_paths']['prompt']}")
    print(f"Metadata: {result['file_paths']['metadata']}")
    print("\nNext Steps:")
    print("1. Use prompt with AI to generate content")
    print("2. Call save_and_validate_content() with generated content")
    print("3. Review validation results and fix any issues")


if __name__ == "__main__":
    main()

