#!/usr/bin/env python3
"""
Character State Manager
Manages character state tracking, updates, and controlled evolution
"""

import yaml
import re
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime


class CharacterStateManager:
    """Manages character state tracking and updates"""
    
    def __init__(self, framework_dir: Path = Path("meta_framework")):
        self.framework_dir = Path(framework_dir)
        self.state_file = self.framework_dir / "characters" / "character_state.yaml"
        
        # Load character states
        self._load_states()
    
    def _load_states(self):
        """Load character states from file"""
        if self.state_file.exists():
            with open(self.state_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f) or {}
                self.character_states = data.get('character_states', {})
        else:
            self.character_states = {}
            self._save_states()
    
    def _save_states(self):
        """Save character states to file"""
        self.state_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.state_file, 'w', encoding='utf-8') as f:
            yaml.dump({'character_states': self.character_states}, f, default_flow_style=False, sort_keys=False)
    
    def get_character_state(self, character_id: str) -> Optional[Dict[str, Any]]:
        """Get character state by ID"""
        return self.character_states.get(character_id)
    
    def initialize_character(self, character_id: str, base_profile: Dict[str, Any]) -> bool:
        """
        Initialize a new character in the state tracker
        
        Args:
            character_id: Unique character identifier
            base_profile: Character profile (name, income, situation, age, etc.)
        
        Returns:
            Success status
        """
        if character_id in self.character_states:
            return False  # Character already exists
        
        # All attributes are locked by default
        locked_attributes = list(base_profile.keys())
        
        self.character_states[character_id] = {
            'base_profile': base_profile.copy(),
            'locked_attributes': locked_attributes,
            'usage_tracking': {
                'chapters': [],
                'last_reference': None,
                'total_references': 0
            },
            'evolution_tracking': {
                'allowed': True,
                'changes': []
            },
            'additional_attributes': {}
        }
        
        self._save_states()
        return True
    
    def record_character_usage(self, character_id: str, chapter_num: int, content: str):
        """
        Record character usage in a chapter
        
        Args:
            character_id: Character identifier
            chapter_num: Chapter number where character is used
            content: Content text (for validation)
        """
        if character_id not in self.character_states:
            print(f"⚠️  WARNING: Character '{character_id}' not in state tracker")
            return
        
        char_state = self.character_states[character_id]
        usage = char_state['usage_tracking']
        
        # Update usage tracking
        if chapter_num not in usage['chapters']:
            usage['chapters'].append(chapter_num)
        usage['last_reference'] = f"Chapter {chapter_num}"
        usage['total_references'] = len(usage['chapters'])
        
        # Validate character reference in content
        self._validate_character_reference(character_id, content, chapter_num)
        
        self._save_states()
    
    def _validate_character_reference(self, character_id: str, content: str, chapter_num: int):
        """
        Validate character reference matches state (flag inconsistencies)
        
        This flags issues for editor review but doesn't block
        """
        char_state = self.character_states[character_id]
        base_profile = char_state['base_profile']
        locked_attrs = char_state.get('locked_attributes', [])
        
        name = base_profile.get('name', '')
        if not name:
            return
        
        # Check if character name appears in content
        name_pattern = re.compile(rf'\b{re.escape(name)}\b', re.IGNORECASE)
        if not name_pattern.search(content):
            return  # Character not mentioned, skip validation
        
        # Extract character details from content (simplified - could be enhanced with NLP)
        inconsistencies = []
        
        # Check income mentions
        if 'income' in locked_attrs:
            income = base_profile.get('income')
            if income:
                # Look for income patterns like "$100,000" or "100k"
                income_patterns = [
                    rf'\${re.escape(str(income))}',
                    rf'\${re.escape(str(income // 1000))}k',
                    rf'{re.escape(str(income // 1000))},\d{{3}}',
                ]
                # This is simplified - in production would use NLP to extract actual income mentions
                # For now, just flag if we detect potential inconsistencies
        
        # Check age mentions
        if 'age' in locked_attrs:
            age = base_profile.get('age')
            if age:
                # Look for age patterns
                age_pattern = rf'\b{re.escape(str(age))}\s*(?:years?\s*old|years? of age)'
                # Simplified check
        
        # Check situation mentions
        if 'situation' in locked_attrs:
            situation = base_profile.get('situation')
            # Would check for situation consistency
        
        # If inconsistencies found, flag for editor review
        if inconsistencies:
            # Would add to editor tracker
            print(f"  ⚠️  Flagged inconsistencies for {character_id} in Chapter {chapter_num}")
    
    def add_character_attribute(self, character_id: str, attribute_name: str, 
                               attribute_value: Any, chapter_num: int) -> bool:
        """
        Add a new attribute to character (for story evolution)
        
        Args:
            character_id: Character identifier
            attribute_name: Name of new attribute
            attribute_value: Value of attribute
            chapter_num: Chapter where attribute is introduced
        
        Returns:
            Success status
        """
        if character_id not in self.character_states:
            return False
        
        char_state = self.character_states[character_id]
        
        # Add to additional_attributes
        if 'additional_attributes' not in char_state:
            char_state['additional_attributes'] = {}
        
        char_state['additional_attributes'][attribute_name] = attribute_value
        
        # Track in evolution_tracking
        evolution = char_state['evolution_tracking']
        evolution['changes'].append({
            'type': 'attribute_added',
            'attribute': attribute_name,
            'value': attribute_value,
            'chapter': chapter_num,
            'timestamp': datetime.now().isoformat()
        })
        
        self._save_states()
        return True
    
    def update_character_attribute(self, character_id: str, attribute_name: str,
                                  new_value: Any, chapter_num: int, 
                                  justification: Optional[str] = None) -> bool:
        """
        Update a character attribute (controlled evolution)
        
        Args:
            character_id: Character identifier
            attribute_name: Attribute to update
            new_value: New value
            chapter_num: Chapter where change occurs
            justification: Reason for change (required for controlled evolution)
        
        Returns:
            Success status
        """
        if character_id not in self.character_states:
            return False
        
        char_state = self.character_states[character_id]
        
        # Check if attribute is locked
        locked_attrs = char_state.get('locked_attributes', [])
        if attribute_name in locked_attrs:
            print(f"⚠️  WARNING: Cannot update locked attribute '{attribute_name}' for {character_id}")
            return False
        
        # Check if evolution is allowed
        evolution = char_state['evolution_tracking']
        if not evolution.get('allowed', True):
            print(f"⚠️  WARNING: Evolution not allowed for {character_id}")
            return False
        
        # Update attribute
        if attribute_name in char_state['base_profile']:
            old_value = char_state['base_profile'][attribute_name]
            char_state['base_profile'][attribute_name] = new_value
        elif attribute_name in char_state.get('additional_attributes', {}):
            old_value = char_state['additional_attributes'][attribute_name]
            char_state['additional_attributes'][attribute_name] = new_value
        else:
            # New attribute
            if 'additional_attributes' not in char_state:
                char_state['additional_attributes'] = {}
            old_value = None
            char_state['additional_attributes'][attribute_name] = new_value
        
        # Track change
        evolution['changes'].append({
            'type': 'attribute_updated',
            'attribute': attribute_name,
            'old_value': old_value,
            'new_value': new_value,
            'chapter': chapter_num,
            'justification': justification,
            'timestamp': datetime.now().isoformat()
        })
        
        self._save_states()
        return True
    
    def get_character_summary(self, character_id: str) -> Dict[str, Any]:
        """Get character summary for prompt inclusion"""
        if character_id not in self.character_states:
            return {}
        
        char_state = self.character_states[character_id]
        base_profile = char_state['base_profile']
        usage = char_state['usage_tracking']
        
        # Build contextual summary (as per decision: contextual, not full profile)
        summary = {
            'name': base_profile.get('name'),
            'key_attributes': {}
        }
        
        # Include only relevant attributes (contextual)
        # In production, this would be determined by context
        for key in ['income', 'situation', 'age']:
            if key in base_profile:
                summary['key_attributes'][key] = base_profile[key]
        
        # Add additional attributes if any
        if char_state.get('additional_attributes'):
            summary['key_attributes'].update(char_state['additional_attributes'])
        
        summary['usage'] = {
            'total_references': usage['total_references'],
            'last_reference': usage['last_reference']
        }
        
        return summary
    
    def get_all_characters(self) -> List[str]:
        """Get list of all character IDs"""
        return list(self.character_states.keys())
    
    def get_characters_by_chapter(self, chapter_num: int) -> List[str]:
        """Get characters used in a specific chapter"""
        characters = []
        for char_id, char_state in self.character_states.items():
            usage = char_state.get('usage_tracking', {})
            if chapter_num in usage.get('chapters', []):
                characters.append(char_id)
        return characters

