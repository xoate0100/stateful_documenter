#!/usr/bin/env python3
"""
Migrate Content to New Directory Structure
Moves existing content to organized structure with metadata
"""

import shutil
import yaml
from pathlib import Path
from datetime import datetime
import re


def count_words(text: str) -> int:
    """Count words in text"""
    return len(re.findall(r'\b\w+\b', text))


def extract_metadata_from_filename(filename: str) -> dict:
    """Extract metadata from existing filename"""
    # Try to parse existing filenames
    # facebook_post_1_tax_leak.md -> topic: tax_leak, platform: facebook
    
    metadata = {
        'platform': 'facebook',
        'funnel_stage': 'mid_funnel',  # Default
        'persona': 'engineer_retiree',  # Default
        'topic': 'unknown'
    }
    
    if 'facebook' in filename.lower():
        metadata['platform'] = 'facebook'
    elif 'linkedin' in filename.lower():
        metadata['platform'] = 'linkedin'
    
    if 'tax' in filename.lower() or 'leak' in filename.lower():
        metadata['topic'] = 'tax_planning'
    elif '401k' in filename.lower() or 'gap' in filename.lower():
        metadata['topic'] = 'retirement_income'
    elif 'income' in filename.lower() or 'social_security' in filename.lower():
        metadata['topic'] = 'retirement_income'
    
    return metadata


def migrate_content():
    """Migrate existing content to new structure"""
    
    old_content_dir = Path("content/social")
    new_base = Path("content")
    
    # Create new structure
    new_dirs = [
        new_base / "published" / "facebook" / "top_of_funnel",
        new_base / "published" / "facebook" / "mid_funnel",
        new_base / "published" / "facebook" / "lower_funnel",
        new_base / "prompts" / "facebook",
        new_base / "metadata",
        new_base / "index",
    ]
    
    for dir_path in new_dirs:
        dir_path.mkdir(parents=True, exist_ok=True)
    
    # Find all content files
    content_files = list(old_content_dir.glob("*.md"))
    prompt_files = list(old_content_dir.glob("*_prompt.txt"))
    
    print(f"Found {len(content_files)} content files")
    print(f"Found {len(prompt_files)} prompt files")
    
    migrated = []
    
    for content_file in content_files:
        if content_file.name == "FACEBOOK_POSTS_SUMMARY.md":
            continue  # Skip summary file
        
        print(f"\nProcessing: {content_file.name}")
        
        # Read content
        with open(content_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract metadata
        metadata_from_file = extract_metadata_from_filename(content_file.name)
        
        # Generate content ID
        date_str = datetime.now().strftime("%Y-%m-%d")
        topic_slug = metadata_from_file['topic']
        platform = metadata_from_file['platform']
        funnel = metadata_from_file['funnel_stage']
        persona = metadata_from_file['persona']
        unique_id = content_file.stem.replace('facebook_post_', '').replace('_', '-')
        
        content_id = f"{platform}_{date_str}_{topic_slug}_{funnel}_{persona}_{unique_id}"
        
        # Determine funnel stage from content analysis
        word_count = count_words(content)
        if 'tax' in content.lower() and 'leak' in content.lower():
            funnel_stage = 'mid_funnel'
        elif '401k' in content.lower() or 'gap' in content.lower():
            funnel_stage = 'top_of_funnel'
        else:
            funnel_stage = 'top_of_funnel'
        
        # Move content file
        new_content_dir = new_base / "published" / platform / funnel_stage
        new_content_file = new_content_dir / f"{content_id}.md"
        
        shutil.copy2(content_file, new_content_file)
        print(f"  [OK] Content moved to: {new_content_file}")
        
        # Create metadata
        metadata = {
            'content_id': content_id,
            'title': content_file.stem.replace('_', ' ').title(),
            'format': 'social_post',
            'platform': platform,
            'funnel_stage': funnel_stage,
            'user_intent': 'researching',
            'persona': persona,
            'topic': metadata_from_file['topic'],
            'tags': [metadata_from_file['topic'], funnel_stage, persona],
            'emotional_goal': 'curiosity',
            'word_count': word_count,
            'created_date': datetime.now().isoformat(),
            'status': 'published',
            'performance': {
                'views': None,
                'engagement': None,
                'conversions': None
            },
            'related_content': []
        }
        
        # Save metadata
        metadata_file = new_base / "metadata" / f"{content_id}.yaml"
        with open(metadata_file, 'w', encoding='utf-8') as f:
            yaml.dump(metadata, f, default_flow_style=False, sort_keys=False)
        
        print(f"  [OK] Metadata saved: {metadata_file}")
        
        migrated.append({
            'old_file': str(content_file),
            'new_file': str(new_content_file),
            'metadata': str(metadata_file),
            'content_id': content_id
        })
    
    # Move prompt files
    for prompt_file in prompt_files:
        print(f"\nProcessing prompt: {prompt_file.name}")
        
        new_prompt_dir = new_base / "prompts" / "facebook"
        new_prompt_file = new_prompt_dir / prompt_file.name
        
        shutil.copy2(prompt_file, new_prompt_file)
        print(f"  [OK] Prompt moved to: {new_prompt_file}")
    
    # Create content index
    index = {
        'content_index': {
            'total_pieces': len(migrated),
            'by_funnel': {},
            'by_persona': {},
            'by_topic': {},
            'recent_content': []
        }
    }
    
    for item in migrated:
        metadata = yaml.safe_load(open(new_base / "metadata" / f"{item['content_id']}.yaml"))
        
        funnel = metadata['funnel_stage']
        persona = metadata['persona']
        topic = metadata['topic']
        
        index['content_index']['by_funnel'][funnel] = index['content_index']['by_funnel'].get(funnel, 0) + 1
        index['content_index']['by_persona'][persona] = index['content_index']['by_persona'].get(persona, 0) + 1
        index['content_index']['by_topic'][topic] = index['content_index']['by_topic'].get(topic, 0) + 1
        
        index['content_index']['recent_content'].append({
            'content_id': item['content_id'],
            'title': metadata['title'],
            'funnel': funnel,
            'persona': persona,
            'created': metadata['created_date']
        })
    
    # Save index
    index_file = new_base / "index" / "content_index.yaml"
    with open(index_file, 'w', encoding='utf-8') as f:
        yaml.dump(index, f, default_flow_style=False, sort_keys=False)
    
    print(f"\n  [OK] Content index saved: {index_file}")
    
    print("\n" + "=" * 70)
    print("Migration Complete")
    print("=" * 70)
    print(f"Migrated {len(migrated)} content files")
    print(f"Moved {len(prompt_files)} prompt files")
    print(f"Created {len(migrated)} metadata files")
    print(f"Created content index")
    print("\nNew structure:")
    print(f"  Content: content/published/{platform}/")
    print(f"  Prompts: content/prompts/{platform}/")
    print(f"  Metadata: content/metadata/")
    print(f"  Index: content/index/")


if __name__ == "__main__":
    migrate_content()

