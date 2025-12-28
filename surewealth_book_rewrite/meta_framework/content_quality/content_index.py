#!/usr/bin/env python3
"""
Content Index System
Manages searchable index of all content by funnel, persona, topic, tags
"""

import yaml
from pathlib import Path
from typing import Dict, Any, List, Optional
from datetime import datetime


class ContentIndex:
    """Manages content index for searchability"""
    
    def __init__(self, content_dir: Path = Path("content")):
        self.content_dir = Path(content_dir)
        self.index_dir = self.content_dir / "index"
        self.index_dir.mkdir(parents=True, exist_ok=True)
        self.index_file = self.index_dir / "content_index.yaml"
        self.metadata_dir = self.content_dir / "metadata"
    
    def load_index(self) -> Dict[str, Any]:
        """Load content index"""
        if not self.index_file.exists():
            return self._create_empty_index()
        
        with open(self.index_file, 'r', encoding='utf-8') as f:
            index = yaml.safe_load(f) or {}
        
        # Ensure structure exists
        if 'content_index' not in index:
            return self._create_empty_index()
        
        return index
    
    def _create_empty_index(self) -> Dict[str, Any]:
        """Create empty index structure"""
        return {
            'content_index': {
                'total_pieces': 0,
                'by_funnel': {},
                'by_persona': {},
                'by_topic': {},
                'by_platform': {},
                'by_format': {},
                'by_tag': {},
                'recent_content': [],
                'last_updated': datetime.now().isoformat()
            }
        }
    
    def add_content(self, metadata: Dict[str, Any]):
        """Add content to index"""
        index = self.load_index()
        content_index = index['content_index']
        
        # Update counts
        content_index['total_pieces'] = content_index.get('total_pieces', 0) + 1
        
        # Update by funnel
        funnel = metadata.get('funnel_stage', 'unknown')
        content_index['by_funnel'][funnel] = content_index['by_funnel'].get(funnel, 0) + 1
        
        # Update by persona
        persona = metadata.get('persona', 'unknown')
        content_index['by_persona'][persona] = content_index['by_persona'].get(persona, 0) + 1
        
        # Update by topic
        topic = metadata.get('topic', 'unknown')
        content_index['by_topic'][topic] = content_index['by_topic'].get(topic, 0) + 1
        
        # Update by platform
        platform = metadata.get('platform', 'unknown')
        content_index['by_platform'][platform] = content_index['by_platform'].get(platform, 0) + 1
        
        # Update by format
        format_type = metadata.get('format', 'unknown')
        content_index['by_format'][format_type] = content_index['by_format'].get(format_type, 0) + 1
        
        # Update by tags
        tags = metadata.get('tags', [])
        for tag in tags:
            content_index['by_tag'][tag] = content_index['by_tag'].get(tag, 0) + 1
        
        # Add to recent content (keep last 100)
        recent = content_index.get('recent_content', [])
        recent.insert(0, {
            'content_id': metadata.get('content_id'),
            'title': metadata.get('title'),
            'funnel': funnel,
            'persona': persona,
            'platform': platform,
            'format': format_type,
            'created': metadata.get('created_date', datetime.now().isoformat())
        })
        content_index['recent_content'] = recent[:100]
        
        # Update timestamp
        content_index['last_updated'] = datetime.now().isoformat()
        
        # Save index
        self.save_index(index)
    
    def save_index(self, index: Dict[str, Any]):
        """Save index to file"""
        with open(self.index_file, 'w', encoding='utf-8') as f:
            yaml.dump(index, f, default_flow_style=False, sort_keys=False)
    
    def search_by_funnel(self, funnel_stage: str) -> List[Dict[str, Any]]:
        """Search content by funnel stage"""
        return self._search_metadata('funnel_stage', funnel_stage)
    
    def search_by_persona(self, persona: str) -> List[Dict[str, Any]]:
        """Search content by persona"""
        return self._search_metadata('persona', persona)
    
    def search_by_topic(self, topic: str) -> List[Dict[str, Any]]:
        """Search content by topic"""
        return self._search_metadata('topic', topic)
    
    def search_by_tag(self, tag: str) -> List[Dict[str, Any]]:
        """Search content by tag"""
        results = []
        
        if not self.metadata_dir.exists():
            return results
        
        for metadata_file in self.metadata_dir.glob("*.yaml"):
            try:
                with open(metadata_file, 'r', encoding='utf-8') as f:
                    metadata = yaml.safe_load(f)
                    if metadata and tag in metadata.get('tags', []):
                        results.append(metadata)
            except Exception:
                continue
        
        return results
    
    def search_by_platform(self, platform: str) -> List[Dict[str, Any]]:
        """Search content by platform"""
        return self._search_metadata('platform', platform)
    
    def _search_metadata(self, field: str, value: str) -> List[Dict[str, Any]]:
        """Search metadata files by field"""
        results = []
        
        if not self.metadata_dir.exists():
            return results
        
        for metadata_file in self.metadata_dir.glob("*.yaml"):
            try:
                with open(metadata_file, 'r', encoding='utf-8') as f:
                    metadata = yaml.safe_load(f)
                    if metadata and metadata.get(field) == value:
                        results.append(metadata)
            except Exception:
                continue
        
        return results
    
    def get_recent_content(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get recent content"""
        index = self.load_index()
        recent = index['content_index'].get('recent_content', [])
        return recent[:limit]
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get index statistics"""
        index = self.load_index()
        content_index = index['content_index']
        
        return {
            'total_pieces': content_index.get('total_pieces', 0),
            'by_funnel': content_index.get('by_funnel', {}),
            'by_persona': content_index.get('by_persona', {}),
            'by_topic': content_index.get('by_topic', {}),
            'by_platform': content_index.get('by_platform', {}),
            'by_format': content_index.get('by_format', {}),
            'last_updated': content_index.get('last_updated')
        }
    
    def rebuild_index(self):
        """Rebuild index from all metadata files"""
        index = self._create_empty_index()
        content_index = index['content_index']
        
        if not self.metadata_dir.exists():
            self.save_index(index)
            return
        
        for metadata_file in self.metadata_dir.glob("*.yaml"):
            try:
                with open(metadata_file, 'r', encoding='utf-8') as f:
                    metadata = yaml.safe_load(f)
                    if not metadata:
                        continue
                    
                    # Update counts
                    content_index['total_pieces'] += 1
                    
                    funnel = metadata.get('funnel_stage', 'unknown')
                    persona = metadata.get('persona', 'unknown')
                    topic = metadata.get('topic', 'unknown')
                    platform = metadata.get('platform', 'unknown')
                    format_type = metadata.get('format', 'unknown')
                    tags = metadata.get('tags', [])
                    
                    content_index['by_funnel'][funnel] = content_index['by_funnel'].get(funnel, 0) + 1
                    content_index['by_persona'][persona] = content_index['by_persona'].get(persona, 0) + 1
                    content_index['by_topic'][topic] = content_index['by_topic'].get(topic, 0) + 1
                    content_index['by_platform'][platform] = content_index['by_platform'].get(platform, 0) + 1
                    content_index['by_format'][format_type] = content_index['by_format'].get(format_type, 0) + 1
                    
                    for tag in tags:
                        content_index['by_tag'][tag] = content_index['by_tag'].get(tag, 0) + 1
                    
                    # Add to recent
                    recent = content_index.get('recent_content', [])
                    recent.append({
                        'content_id': metadata.get('content_id'),
                        'title': metadata.get('title'),
                        'funnel': funnel,
                        'persona': persona,
                        'platform': platform,
                        'format': format_type,
                        'created': metadata.get('created_date', datetime.now().isoformat())
                    })
                    content_index['recent_content'] = recent
            except Exception as e:
                print(f"Error processing {metadata_file}: {e}")
                continue
        
        # Sort recent by date
        content_index['recent_content'].sort(key=lambda x: x.get('created', ''), reverse=True)
        content_index['recent_content'] = content_index['recent_content'][:100]
        content_index['last_updated'] = datetime.now().isoformat()
        
        self.save_index(index)

