#!/usr/bin/env python3
"""
Content Metadata System
Creates and manages metadata for all generated content
"""

import yaml
import json
from pathlib import Path
from typing import Dict, Any, Optional, List
from datetime import datetime
import uuid


class ContentMetadata:
    """Manages content metadata"""
    
    def __init__(self, content_dir: Path = Path("content")):
        self.content_dir = Path(content_dir)
        self.metadata_dir = self.content_dir / "metadata"
        self.metadata_dir.mkdir(parents=True, exist_ok=True)
    
    def create_metadata(self, 
                       content_id: str,
                       title: str,
                       format_type: str,
                       platform: str,
                       funnel_stage: str,
                       user_intent: str,
                       persona: str,
                       topic: str,
                       tags: List[str],
                       emotional_goal: str,
                       narrative_used: Optional[str] = None,
                       signature_phrases: Optional[List[str]] = None,
                       cta_type: str = "soft_cta",
                       cta_count: int = 1,
                       permission_frames_used: int = 0,
                       word_count: int = 0,
                       **kwargs) -> Dict[str, Any]:
        """Create metadata dictionary"""
        
        metadata = {
            'content_id': content_id,
            'title': title,
            'format': format_type,
            'platform': platform,
            'funnel_stage': funnel_stage,
            'user_intent': user_intent,
            'persona': persona,
            'topic': topic,
            'tags': tags,
            'emotional_goal': emotional_goal,
            'narrative_used': narrative_used,
            'signature_phrases': signature_phrases or [],
            'cta_type': cta_type,
            'cta_count': cta_count,
            'permission_frames_used': permission_frames_used,
            'word_count': word_count,
            'created_date': datetime.now().isoformat(),
            'status': 'draft',
            'performance': {
                'views': None,
                'engagement': None,
                'conversions': None
            },
            'related_content': [],
            **kwargs
        }
        
        return metadata
    
    def save_metadata(self, metadata: Dict[str, Any]) -> Path:
        """Save metadata to YAML file"""
        content_id = metadata['content_id']
        metadata_file = self.metadata_dir / f"{content_id}.yaml"
        
        with open(metadata_file, 'w', encoding='utf-8') as f:
            yaml.dump(metadata, f, default_flow_style=False, sort_keys=False)
        
        return metadata_file
    
    def load_metadata(self, content_id: str) -> Optional[Dict[str, Any]]:
        """Load metadata from file"""
        metadata_file = self.metadata_dir / f"{content_id}.yaml"
        
        if not metadata_file.exists():
            return None
        
        with open(metadata_file, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    
    def generate_content_id(self, 
                           platform: str,
                           topic: str,
                           funnel_stage: str,
                           persona: str) -> str:
        """Generate unique content ID"""
        date_str = datetime.now().strftime("%Y-%m-%d")
        topic_slug = topic.lower().replace(' ', '-').replace("'", "").replace(",", "")[:30]
        funnel_slug = funnel_stage.replace('_', '-')
        persona_slug = persona.replace('_', '-')
        
        # Generate short unique ID
        unique_id = str(uuid.uuid4())[:8]
        
        return f"{platform}_{date_str}_{topic_slug}_{funnel_slug}_{persona_slug}_{unique_id}"
    
    def update_content_index(self, metadata: Dict[str, Any]):
        """Update master content index using ContentIndex"""
        try:
            from meta_framework.content_quality.content_index import ContentIndex
            index_manager = ContentIndex(self.content_dir)
            index_manager.add_content(metadata)
        except ImportError:
            # Fallback to simple index update
            index_file = self.content_dir / "index" / "content_index.yaml"
            index_file.parent.mkdir(parents=True, exist_ok=True)
            
            if index_file.exists():
                with open(index_file, 'r', encoding='utf-8') as f:
                    index = yaml.safe_load(f) or {}
            else:
                index = {
                    'content_index': {
                        'total_pieces': 0,
                        'by_funnel': {},
                        'by_persona': {},
                        'by_topic': {},
                        'recent_content': []
                    }
                }
            
            content_index = index['content_index']
            content_index['total_pieces'] = content_index.get('total_pieces', 0) + 1
            
            funnel = metadata.get('funnel_stage', 'unknown')
            persona = metadata.get('persona', 'unknown')
            topic = metadata.get('topic', 'unknown')
            
            content_index['by_funnel'][funnel] = content_index['by_funnel'].get(funnel, 0) + 1
            content_index['by_persona'][persona] = content_index['by_persona'].get(persona, 0) + 1
            content_index['by_topic'][topic] = content_index['by_topic'].get(topic, 0) + 1
            
            recent = content_index.get('recent_content', [])
            recent.insert(0, {
                'content_id': metadata['content_id'],
                'title': metadata['title'],
                'funnel': funnel,
                'persona': persona,
                'created': metadata['created_date']
            })
            content_index['recent_content'] = recent[:50]
            
            with open(index_file, 'w', encoding='utf-8') as f:
                yaml.dump(index, f, default_flow_style=False)

