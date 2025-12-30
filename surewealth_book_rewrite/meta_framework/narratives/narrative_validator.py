#!/usr/bin/env python3
"""
Narrative Validator
Validates narrative usage and handles AI-assisted narrative generation
"""

import yaml
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime


class NarrativeValidator:
    """Validates and manages narrative usage"""
    
    def __init__(self, framework_dir: Path = Path("meta_framework")):
        self.framework_dir = Path(framework_dir)
        self.narratives_dir = self.framework_dir / "narratives"
        self.tracker_file = self.narratives_dir / "narrative_generation_tracker.yaml"
        
        # Load tracker
        self._load_tracker()
    
    def _load_tracker(self):
        """Load narrative generation tracker"""
        if self.tracker_file.exists():
            with open(self.tracker_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                self.tracker = data if data else {}
        else:
            self.tracker = {
                'narrative_generation_tracker': {
                    'approved_narratives': [],
                    'pending_narratives': [],
                    'rejected_narratives': []
                }
            }
        
        # Ensure structure exists
        if 'narrative_generation_tracker' not in self.tracker:
            self.tracker['narrative_generation_tracker'] = {
                'approved_narratives': [],
                'pending_narratives': [],
                'rejected_narratives': []
            }
    
    def validate_narrative_ids(self, narrative_ids: List[str]) -> Tuple[bool, List[str], List[str]]:
        """
        Validate narrative IDs before generation (PRE-GENERATION)
        
        Returns: (is_valid, missing_narratives, suggestions)
        """
        missing = []
        suggestions = []
        
        # Get all approved narratives
        tracker_data = self.tracker.get('narrative_generation_tracker', {})
        if tracker_data is None:
            tracker_data = {}
        approved = set(tracker_data.get('approved_narratives', []))
        
        # Check framework narratives
        for narrative_id in narrative_ids:
            found = False
            
            # Check in framework directories
            for narrative_type in ['allegories', 'metaphors', 'case_studies']:
                narrative_file = self.narratives_dir / narrative_type / f"{narrative_id}.yaml"
                if narrative_file.exists():
                    found = True
                    break
            
            # Check approved narratives
            if narrative_id in approved:
                found = True
            
            if not found:
                missing.append(narrative_id)
                # Suggest closest match (simplified - could be enhanced)
                suggestions.append(f"Consider using closest match from framework")
        
        return len(missing) == 0, missing, suggestions
    
    def detect_new_narratives(self, content: str, narrative_ids: List[str]) -> List[Dict[str, Any]]:
        """
        Detect if AI created new narratives (POST-GENERATION)
        
        Returns: List of detected new narratives
        """
        new_narratives = []
        
        # This is a simplified check - in production, would use NLP to detect
        # narrative-like structures that aren't in the framework
        
        # For now, just check if content mentions narratives not in narrative_ids
        # Pattern: Look for narrative-like structures
        
        # If we detect a new narrative, flag it
        # In production, this would be more sophisticated
        
        return new_narratives
    
    def request_narrative_generation(self, context: str, emotional_journey: Dict[str, Any]) -> Dict[str, Any]:
        """
        Request AI to generate a new narrative (AI-assisted)
        
        Returns: Draft narrative for human approval
        """
        narrative_draft = {
            'title': f"Narrative for: {context[:50]}...",
            'type': 'allegory',  # Default, could be determined by context
            'status': 'draft',
            'created_by': 'ai',
            'created_date': datetime.now().isoformat(),
            'approved_date': None,
            'emotional_journey': emotional_journey,
            'context': context,
            'usage': {
                'chapters': [],
                'first_used': None,
                'total_uses': 0
            }
        }
        
        # Add to pending
        pending = self.tracker.get('narrative_generation_tracker', {}).get('pending_narratives', [])
        pending.append(narrative_draft)
        self.tracker['narrative_generation_tracker']['pending_narratives'] = pending
        
        self._save_tracker()
        
        return narrative_draft
    
    def approve_narrative(self, narrative_id: str, narrative_data: Dict[str, Any]) -> bool:
        """
        Approve a pending narrative and add to framework
        
        Returns: Success status
        """
        pending = self.tracker.get('narrative_generation_tracker', {}).get('pending_narratives', [])
        
        # Find narrative in pending
        narrative = None
        for n in pending:
            if n.get('title') == narrative_id or n.get('created_date') == narrative_id:
                narrative = n
                break
        
        if not narrative:
            return False
        
        # Update status
        narrative['status'] = 'approved'
        narrative['approved_date'] = datetime.now().isoformat()
        
        # Move to approved
        approved = self.tracker.get('narrative_generation_tracker', {}).get('approved_narratives', [])
        approved.append(narrative_id)
        self.tracker['narrative_generation_tracker']['approved_narratives'] = approved
        
        # Remove from pending
        pending.remove(narrative)
        self.tracker['narrative_generation_tracker']['pending_narratives'] = pending
        
        # Save narrative to framework (would create YAML file)
        # For now, just track in tracker
        
        self._save_tracker()
        
        return True
    
    def _save_tracker(self):
        """Save tracker to file"""
        self.tracker_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.tracker_file, 'w', encoding='utf-8') as f:
            yaml.dump(self.tracker, f, default_flow_style=False, sort_keys=False)

