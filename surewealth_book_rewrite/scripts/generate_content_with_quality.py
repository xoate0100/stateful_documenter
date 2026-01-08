#!/usr/bin/env python3
"""
Generate Content with Quality Validation
Integrates all new validation systems: BookValidator, BookQualityTracker, Character State
"""

import sys
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional, List

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from ai_prompts.prompt_builder import PromptBuilder
from meta_framework.content_quality.content_validator import ContentValidator
from meta_framework.content_quality.content_metadata import ContentMetadata
from meta_framework.content_quality.content_index import ContentIndex
from meta_framework.content_quality.book_validator import BookValidator
from scripts.book_quality_tracker import BookQualityTracker
from meta_framework.characters.character_state_manager import CharacterStateManager
from meta_framework.narratives.narrative_validator import NarrativeValidator


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
    character_ids: Optional[List[str]] = None,
    length: Optional[str] = None,
    chapter_num: Optional[int] = None,
    emotional_state: Optional[str] = None,
    output_content: bool = True
) -> Dict[str, Any]:
    """
    Generate content with full quality validation and tracking
    
    Returns dict with:
    - prompt: Generated prompt
    - metadata: Content metadata
    - validation: Validation results
    - file_paths: Where files were saved
    """
    
    # Initialize all systems
    builder = PromptBuilder()
    validator = ContentValidator()
    book_validator = BookValidator()
    metadata_manager = ContentMetadata()
    index_manager = ContentIndex()
    quality_tracker = BookQualityTracker()
    character_manager = CharacterStateManager()
    narrative_validator = NarrativeValidator()
    
    # PRE-GENERATION VALIDATION
    
    # Validate narrative IDs
    if narrative_id:
        nar_valid, nar_missing, nar_suggestions = narrative_validator.validate_narrative_ids([narrative_id])
        if not nar_valid:
            print(f"⚠️  WARNING: Narrative validation issues:")
            for missing in nar_missing:
                print(f"   - Missing narrative: {missing}")
            print(f"   - Suggestions: {nar_suggestions}")
            # Continue with closest match (as per decision)
    
    # Validate character IDs
    if character_ids:
        for char_id in character_ids:
            char_state = character_manager.get_character_state(char_id)
            if not char_state:
                print(f"⚠️  WARNING: Character '{char_id}' not found in state tracker")
            else:
                print(f"✓ Character '{char_id}' loaded: {char_state.get('base_profile', {}).get('name', 'Unknown')}")
    
    # Generate prompt with chapter number for structure recommendation
    print(f"\n{'='*70}")
    print(f"Generating prompt for: {topic}")
    print(f"  Format: {format_type} | Platform: {platform}")
    print(f"  Funnel: {funnel_stage} | Persona: {persona}")
    if chapter_num:
        print(f"  Chapter: {chapter_num}")
    if emotional_state:
        print(f"  Emotional State: {emotional_state}")
    print(f"{'='*70}\n")
    
    prompt = builder.build_prompt(
        format_type=format_type,
        topic=topic,
        persona=persona,
        length=length,
        emotional_goal=emotional_goal,
        narrative_ids=[narrative_id] if narrative_id else None,
        character_ids=character_ids or [],
        chapter_num=chapter_num,
        validate=True  # Enable pre-generation validation
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
        print(f"  [INFO] Run AI generation with prompt, then call save_and_validate_content()")
    
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
        emotional_state=emotional_state,
        narrative_used=narrative_id,
        character_ids=character_ids or [],
        chapter_num=chapter_num,
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
        'validation': None,  # Will be populated when content is validated
        'expected_length': length  # Store for validation
    }


def save_and_validate_content(
    content_id: str,
    content: str,
    signature_phrases: Optional[list] = None,
    chapter_num: Optional[int] = None
) -> Dict[str, Any]:
    """
    Save generated content and validate it with all new validation systems
    
    Returns validation results
    """
    
    validator = ContentValidator()
    book_validator = BookValidator()
    metadata_manager = ContentMetadata()
    index_manager = ContentIndex()
    quality_tracker = BookQualityTracker()
    character_manager = CharacterStateManager()
    
    # Load metadata
    metadata = metadata_manager.load_metadata(content_id)
    if not metadata:
        raise ValueError(f"Metadata not found for content_id: {content_id}")
    
    # Get expected length from metadata if available
    expected_length = metadata.get('expected_length') or metadata.get('length')
    
    print(f"\n{'='*70}")
    print(f"Validating Content: {content_id}")
    print(f"{'='*70}\n")
    
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
    
    content_dir.mkdir(parents=True, exist_ok=True)
    with open(content_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  [OK] Content saved: {content_file}")
    
    # POST-GENERATION VALIDATION
    
    # Run BookValidator (all new validations)
    print(f"\n  Running BookValidator...")
    book_validation = book_validator.validate_all(
        content=content,
        metadata=metadata,
        chapter_num=chapter_num or metadata.get('chapter_num')
    )
    
    # Auto-fix if enabled
    if book_validation.get('auto_fixes'):
        print(f"  [AUTO-FIX] Applied {len(book_validation['auto_fixes'])} fixes")
        content = book_validation['corrected_content']
        # Re-save corrected content
        with open(content_file, 'w', encoding='utf-8') as f:
            f.write(content)
    
    # Run ContentValidator (lessons learned + edge cases)
    print(f"  Running ContentValidator with comprehensive validation...")
    # Get expected length from metadata or chapter spec
    expected_length = metadata.get('expected_length') or metadata.get('length')
    is_valid, issues, warnings = validator.validate_content(content, metadata, expected_length=expected_length)
    
    # Combine validation results
    all_issues = book_validation.get('issues', []) + issues
    all_warnings = book_validation.get('warnings', []) + warnings
    
    # Get quality checklist
    checklist = validator.get_quality_checklist(content, metadata)
    
    # Update character states if characters were used
    character_ids = metadata.get('character_ids', [])
    if character_ids and chapter_num:
        print(f"\n  Updating character states...")
        for char_id in character_ids:
            character_manager.record_character_usage(
                character_id=char_id,
                chapter_num=chapter_num,
                content=content
            )
            print(f"    ✓ Updated usage for: {char_id}")
    
    # Run quality checkpoint if this is a chapter
    if chapter_num:
        print(f"\n  Running quality checkpoint for Chapter {chapter_num}...")
        checkpoint = quality_tracker.checkpoint(
            chapter_num=chapter_num,
            content_file=content_file,
            metadata=metadata
        )
    else:
        checkpoint = None
    
    # Update metadata with validation results
    metadata['validation'] = {
        'is_valid': book_validation.get('is_valid', True) and is_valid,
        'book_validation': {
            'is_valid': book_validation.get('is_valid', True),
            'issues': book_validation.get('issues', []),
            'warnings': book_validation.get('warnings', []),
            'auto_fixes': book_validation.get('auto_fixes', [])
        },
        'content_validation': {
            'is_valid': is_valid,
            'issues': issues,
            'warnings': warnings
        },
        'all_issues': all_issues,
        'all_warnings': all_warnings,
        'checklist': checklist,
        'checkpoint': checkpoint
    }
    
    # Save updated metadata
    metadata_manager.save_metadata(metadata)
    
    # Update index with updated metadata
    index_manager.add_content(metadata)
    
    # Check for critical issues (length, compliance, required elements)
    critical_issues = [i for i in all_issues if 'CRITICAL' in i or 'too short' in i.lower() or 'compliance violation' in i.lower()]
    should_reject = len(critical_issues) > 0
    
    # Print summary
    print(f"\n{'='*70}")
    print(f"Validation Complete")
    print(f"{'='*70}")
    print(f"  Valid: {'[OK]' if metadata['validation']['is_valid'] and not should_reject else '[FAIL]'}")
    print(f"  Issues: {len(all_issues)}")
    print(f"  Warnings: {len(all_warnings)}")
    
    if critical_issues:
        print(f"\n  [FAIL] CRITICAL ISSUES FOUND ({len(critical_issues)}):")
        for issue in critical_issues[:5]:  # Show first 5
            print(f"    - {issue}")
        if len(critical_issues) > 5:
            print(f"    ... and {len(critical_issues) - 5} more")
        print(f"\n  [ACTION REQUIRED] Content will be REJECTED. Regenerate with fixes.")
    
    if checkpoint:
        print(f"  Quality Score: {checkpoint.get('metrics', {}).get('overall_consistency', 0):.1%}")
    print(f"{'='*70}\n")
    
    return {
        'is_valid': metadata['validation']['is_valid'] and not should_reject,
        'should_reject': should_reject,
        'critical_issues': critical_issues,
        'issues': all_issues,
        'warnings': all_warnings,
        'checklist': checklist,
        'content_file': str(content_file),
        'metadata_file': str(metadata_manager.metadata_dir / f"{content_id}.yaml"),
        'checkpoint': checkpoint
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
