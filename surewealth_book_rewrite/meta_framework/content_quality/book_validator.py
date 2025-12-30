#!/usr/bin/env python3
"""
Book-Level Content Validator
Validates content against all book generation constraints
"""

import yaml
import json
import re
from pathlib import Path
from typing import Dict, List, Any, Tuple, Optional
from datetime import datetime


class EditorTracker:
    """Tracks issues for editor review with file, line, scenario, issue details"""
    
    def __init__(self, tracker_file: Path = None):
        if tracker_file is None:
            tracker_file = Path("content") / "editor_tracker" / "issues.yaml"
        self.tracker_file = tracker_file
        self.tracker_file.parent.mkdir(parents=True, exist_ok=True)
        self.issues = []
    
    def add_issue(self, file_path: str, line_number: Optional[int], 
                  scenario: str, issue_type: str, details: List[str]):
        """Add issue to tracker"""
        issue = {
            'file_path': file_path,
            'line_number': line_number,
            'scenario': scenario,
            'issue_type': issue_type,
            'details': details,
            'timestamp': datetime.now().isoformat(),
            'status': 'pending_review'
        }
        self.issues.append(issue)
        self._save()
    
    def _save(self):
        """Save tracker to file"""
        with open(self.tracker_file, 'w', encoding='utf-8') as f:
            yaml.dump({'issues': self.issues}, f, default_flow_style=False)
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get statistics on tracked issues"""
        if not self.issues:
            return {'total': 0}
        
        by_type = {}
        for issue in self.issues:
            issue_type = issue.get('issue_type', 'unknown')
            by_type[issue_type] = by_type.get(issue_type, 0) + 1
        
        return {
            'total': len(self.issues),
            'by_type': by_type,
            'pending': len([i for i in self.issues if i.get('status') == 'pending_review'])
        }


class BookValidator:
    """Validates content for book generation with all constraints"""
    
    def __init__(self, framework_dir: Path = Path("meta_framework")):
        self.framework_dir = Path(framework_dir)
        self.editor_tracker = EditorTracker()
        
        # Load configuration files
        self._load_configs()
    
    def _load_configs(self):
        """Load all configuration files"""
        # CTA funnel rules
        cta_rules_file = self.framework_dir / "tools_ctas" / "cta_funnel_rules.yaml"
        if cta_rules_file.exists():
            with open(cta_rules_file, 'r', encoding='utf-8') as f:
                self.cta_rules = yaml.safe_load(f).get('cta_funnel_rules', {})
        else:
            self.cta_rules = {}
        
        # Character state
        char_state_file = self.framework_dir / "characters" / "character_state.yaml"
        if char_state_file.exists():
            with open(char_state_file, 'r', encoding='utf-8') as f:
                self.character_states = yaml.safe_load(f).get('character_states', {})
        else:
            self.character_states = {}
        
        # Emotional arc tracker
        arc_file = self.framework_dir / "chapters" / "emotional_arc_tracker.yaml"
        if arc_file.exists():
            with open(arc_file, 'r', encoding='utf-8') as f:
                self.arc_tracker = yaml.safe_load(f)
        else:
            self.arc_tracker = {}
        
        # Chapter references
        refs_file = self.framework_dir / "chapters" / "chapter_references.yaml"
        if refs_file.exists():
            with open(refs_file, 'r', encoding='utf-8') as f:
                self.chapter_refs = yaml.safe_load(f)
        else:
            self.chapter_refs = {}
        
        # Signature phrases
        sig_file = self.framework_dir / "language" / "signature_phrases_repository.yaml"
        if sig_file.exists():
            with open(sig_file, 'r', encoding='utf-8') as f:
                self.sig_phrases = yaml.safe_load(f).get('signature_phrases', {})
        else:
            self.sig_phrases = {}
        
        # Permission frames
        perm_file = self.framework_dir / "language" / "permission_frames_repository.yaml"
        if perm_file.exists():
            with open(perm_file, 'r', encoding='utf-8') as f:
                self.permission_frames = yaml.safe_load(f)
        else:
            self.permission_frames = {}
    
    def validate_narrative_usage(self, content: str, narrative_ids: List[str], 
                                 chapter_num: Optional[int] = None) -> Tuple[bool, List[str]]:
        """
        Validate narrative usage - check if only framework narratives are used
        
        Returns: (is_valid, violations)
        """
        violations = []
        
        # Load all approved narratives from framework
        narratives_dir = self.framework_dir / "narratives"
        approved_narratives = set()
        
        # Load from narrative tracker
        tracker_file = self.framework_dir / "narratives" / "narrative_generation_tracker.yaml"
        if tracker_file.exists():
            with open(tracker_file, 'r', encoding='utf-8') as f:
                tracker = yaml.safe_load(f)
                if tracker:
                    tracker_data = tracker.get('narrative_generation_tracker', {})
                    if tracker_data:
                        approved = tracker_data.get('approved_narratives', [])
                        approved_narratives.update(approved)
        
        # Check if content uses unauthorized narratives
        # Pattern: Look for narrative-like structures not in framework
        # This is a simplified check - could be enhanced with NLP
        
        # For now, validate that specified narratives are in framework
        for narrative_id in narrative_ids:
            # Check if narrative exists in framework
            narrative_found = False
            for narrative_type in ['allegories', 'metaphors', 'case_studies']:
                narrative_file = narratives_dir / narrative_type / f"{narrative_id}.yaml"
                if narrative_file.exists():
                    narrative_found = True
                    break
            
            if not narrative_found and narrative_id not in approved_narratives:
                violations.append(f"Narrative '{narrative_id}' not found in framework")
        
        return len(violations) == 0, violations
    
    def validate_character_reference(self, content: str, character_id: str, 
                                    chapter_num: Optional[int] = None) -> Tuple[bool, Dict[str, Any]]:
        """
        Validate character reference matches character state
        
        Returns: (is_valid, issues_dict)
        """
        issues = {
            'inconsistencies': [],
            'warnings': []
        }
        
        if character_id not in self.character_states:
            issues['warnings'].append(f"Character '{character_id}' not in state tracker")
            return True, issues  # New character, allow but warn
        
        char_state = self.character_states[character_id]
        base_profile = char_state.get('base_profile', {})
        locked_attrs = char_state.get('locked_attributes', [])
        
        # Extract character details from content
        # Pattern: Look for character name and attributes
        name = base_profile.get('name', '')
        if name:
            # Find character references
            name_pattern = re.compile(rf'\b{re.escape(name)}\b', re.IGNORECASE)
            if name_pattern.search(content):
                # Check for attribute mentions
                for attr in locked_attrs:
                    attr_value = base_profile.get(attr)
                    if attr_value:
                        # Check if content mentions different value
                        # This is simplified - could be enhanced
                        pass
        
        # Flag for editor review (as requested)
        if issues['inconsistencies']:
            self.editor_tracker.add_issue(
                file_path=f"chapter_{chapter_num}.md" if chapter_num else "unknown",
                line_number=None,  # Would need content parsing to get exact line
                scenario=f"Character reference: {character_id}",
                issue_type="character_inconsistency",
                details=issues['inconsistencies']
            )
        
        return len(issues['inconsistencies']) == 0, issues
    
    def validate_cta_funnel_match(self, content: str, funnel_stage: str, 
                                  chapter_num: Optional[int] = None) -> Tuple[bool, List[str], str]:
        """
        Validate CTA matches funnel stage
        
        Returns: (is_valid, issues, corrected_content)
        """
        issues = []
        corrected_content = content
        
        if funnel_stage not in self.cta_rules:
            return True, [], content  # Unknown stage, skip validation
        
        rules = self.cta_rules[funnel_stage]
        max_count = rules.get('max_count', 1)
        allowed_types = rules.get('allowed_cta_types', [])
        
        # Extract CTAs from content (simplified pattern matching)
        # Use more specific patterns to avoid double-counting
        cta_patterns = [
            r"(Schedule|Book|Call|Contact).*?(consultation|meeting|call now)",
            r"Let's (run|test|check|verify) your",
            r"Would you like to (know|see|learn|explore)",
            r"If there were a way to.*?\?",
            r"If I could show you.*?\?",
        ]
        
        cta_matches = []
        for pattern in cta_patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                # Check if this match overlaps with a previous match (avoid double-counting)
                overlap = False
                for existing in cta_matches:
                    if not (match.end() <= existing['start'] or match.start() >= existing['end']):
                        overlap = True
                        break
                
                if not overlap:
                    cta_matches.append({
                        'text': match.group(0),
                        'start': match.start(),
                        'end': match.end()
                    })
        
        # Check count
        if len(cta_matches) > max_count:
            issues.append(f"Too many CTAs ({len(cta_matches)}), max is {max_count} for {funnel_stage}")
        
        # Auto-correct: Replace inappropriate CTAs
        auto_correct = self.cta_rules.get('auto_correction', {}).get('enabled', False)
        if auto_correct and issues:
            # Replace with appropriate CTA or pre-sell
            replacement = self._get_appropriate_cta(funnel_stage, chapter_num)
            if replacement:
                # Replace first inappropriate CTA
                if cta_matches:
                    first_match = cta_matches[0]
                    corrected_content = (
                        corrected_content[:first_match['start']] +
                        replacement +
                        corrected_content[first_match['end']:]
                    )
        
        # Strict validation: Reject if doesn't match
        if issues and not auto_correct:
            return False, issues, content
        
        return True, issues, corrected_content
    
    def _get_appropriate_cta(self, funnel_stage: str, chapter_num: Optional[int] = None) -> Optional[str]:
        """Get appropriate CTA for funnel stage"""
        if funnel_stage == 'top_of_funnel':
            return "Want to see if this applies to you?"
        elif funnel_stage == 'mid_funnel':
            return "If there were a way to [benefit], would you like to know how?"
        elif funnel_stage == 'lower_funnel':
            return "Let's run your numbers, privately."
        elif chapter_num:
            return f"Read more about this in Chapter {chapter_num + 1}"
        return None
    
    def validate_emotional_progression(self, chapter_num: int, emotional_state: str, 
                                      sub_state: Optional[str] = None) -> Tuple[bool, List[str]]:
        """
        Validate emotional state matches progression
        
        Returns: (is_valid, warnings)
        """
        warnings = []
        
        if 'book_emotional_arc' not in self.arc_tracker:
            return True, []  # No arc defined yet
        
        arc = self.arc_tracker['book_emotional_arc']
        actual_progression = arc.get('actual_progression', [])
        
        # Initialize last_state
        last_state = None
        
        # Check for regression
        if len(actual_progression) > 0:
            last_state = actual_progression[-1].get('state')
            if last_state and self._is_regression(last_state, emotional_state):
                # Allow with reason (as per decision)
                warnings.append(f"Emotional regression detected: {last_state} → {emotional_state}. Ensure this is justified.")
        
        # Check for smooth transitions
        validation_rules = arc.get('validation_rules', {})
        if 'Smooth transitions preferred' in str(validation_rules):
            if last_state and not self._is_smooth_transition(last_state, emotional_state):
                warnings.append(f"Transition may not be smooth: {last_state} → {emotional_state}")
        
        return True, warnings  # Warn but don't block
    
    def _is_regression(self, from_state: str, to_state: str) -> bool:
        """Check if transition is a regression"""
        progression = ['fear', 'concern', 'hope', 'confidence', 'action']
        try:
            from_idx = progression.index(from_state.lower())
            to_idx = progression.index(to_state.lower())
            return to_idx < from_idx
        except ValueError:
            return False
    
    def _is_smooth_transition(self, from_state: str, to_state: str) -> bool:
        """Check if transition is smooth (adjacent states)"""
        progression = ['fear', 'concern', 'hope', 'confidence', 'action']
        try:
            from_idx = progression.index(from_state.lower())
            to_idx = progression.index(to_state.lower())
            return abs(to_idx - from_idx) <= 1
        except ValueError:
            return True  # Unknown states, allow
    
    def validate_chapter_references(self, content: str, chapter_num: int) -> Tuple[bool, List[str]]:
        """
        Validate all chapter references in content
        
        Returns: (is_valid, issues)
        """
        issues = []
        
        # Extract chapter references
        chapter_ref_pattern = r'[Cc]hapter\s+(\d+)'
        matches = re.finditer(chapter_ref_pattern, content)
        
        for match in matches:
            ref_chapter = int(match.group(1))
            
            # Check if forward reference (to unwritten chapter)
            if ref_chapter > chapter_num:
                # Check if chapter is planned
                planned = self.chapter_refs.get('chapter_references', {}).get('planned_chapters', [])
                if ref_chapter not in planned:
                    issues.append(f"Forward reference to Chapter {ref_chapter} (not yet written or planned)")
            
            # Check if backward reference (to written chapter)
            elif ref_chapter < chapter_num:
                # Validate content matches (related topic)
                # This would require chapter content analysis
                # For now, just check that reference exists
                pass
        
        # Strict validation: Reject if invalid
        return len(issues) == 0, issues
    
    def validate_signature_phrase_rotation(self, content: str, chapter_num: int) -> Tuple[bool, List[str]]:
        """
        Validate signature phrase rotation (min 3 chapters between uses)
        
        Returns: (is_valid, issues)
        """
        issues = []
        
        # Load signature phrases
        if not self.sig_phrases:
            return True, []  # No signature phrases loaded, skip validation
        
        for phrase_id, phrase_data in self.sig_phrases.items():
            phrase = phrase_data.get('phrase', '')
            if not phrase:
                continue
            
            # Check if phrase is in content
            if phrase.lower() in content.lower():
                usage = phrase_data.get('usage_tracking', {})
                last_used = usage.get('last_used_chapter')
                
                if last_used is not None:
                    distance = chapter_num - last_used
                    min_distance = phrase_data.get('rotation_rule', {}).get('min_chapters_between', 3)
                    
                    if distance < min_distance:
                        issues.append(
                            f"Signature phrase '{phrase}' used too recently "
                            f"(last used in Chapter {last_used}, current: Chapter {chapter_num}, "
                            f"min distance: {min_distance})"
                        )
        
        # Strict enforcement: Reject if too recent
        return len(issues) == 0, issues
    
    def validate_permission_frames(self, content: str) -> Tuple[bool, List[str]]:
        """
        Validate permission frame usage (max 2, require variety)
        
        Returns: (is_valid, issues)
        """
        issues = []
        
        if not self.permission_frames:
            return True, []  # No permission frames loaded, skip validation
        
        permission_frames = self.permission_frames.get('permission_frames', {})
        all_frames = []
        for category in permission_frames.values():
            if isinstance(category, list):
                all_frames.extend(category)
        
        # Count permission frames
        frame_count = 0
        used_frames = []
        
        for frame in all_frames:
            count = len(re.findall(re.escape(frame), content, re.IGNORECASE))
            if count > 0:
                frame_count += count
                used_frames.append(frame)
        
        # Check max count (2)
        max_count = self.permission_frames.get('usage_rules', {}).get('max_per_chapter', 2)
        if frame_count > max_count:
            issues.append(f"Too many permission frames ({frame_count}), max is {max_count}")
        
        # Check variety (if using multiple)
        require_variety = self.permission_frames.get('usage_rules', {}).get('require_variety', True)
        if require_variety and len(set(used_frames)) < len(used_frames):
            issues.append("Permission frames must use different phrases (variety required)")
        
        # Strict enforcement: Reject if limit exceeded
        return len(issues) == 0, issues
    
    def validate_all(self, content: str, metadata: Dict[str, Any], 
                    chapter_num: Optional[int] = None) -> Dict[str, Any]:
        """
        Run all validations
        
        Returns validation results dictionary
        """
        results = {
            'is_valid': True,
            'issues': [],
            'warnings': [],
            'auto_fixes': [],
            'corrected_content': content
        }
        
        funnel_stage = metadata.get('funnel_stage', 'mid_funnel')
        narrative_ids = metadata.get('narrative_ids', [])
        character_ids = metadata.get('character_ids', [])
        emotional_state = metadata.get('emotional_state')
        
        # Validate narratives
        nar_valid, nar_issues = self.validate_narrative_usage(content, narrative_ids, chapter_num)
        if not nar_valid:
            results['issues'].extend(nar_issues)
            results['is_valid'] = False
        
        # Validate characters
        for char_id in character_ids:
            char_valid, char_issues = self.validate_character_reference(content, char_id, chapter_num)
            if char_issues.get('inconsistencies'):
                results['warnings'].extend(char_issues['inconsistencies'])
                # Flag for editor review (don't block)
        
        # Validate CTAs
        cta_valid, cta_issues, corrected = self.validate_cta_funnel_match(content, funnel_stage, chapter_num)
        if not cta_valid:
            results['issues'].extend(cta_issues)
            results['is_valid'] = False
        elif corrected != content:
            results['auto_fixes'].append("CTA auto-corrected")
            results['corrected_content'] = corrected
        
        # Validate emotional arc
        if emotional_state:
            arc_valid, arc_warnings = self.validate_emotional_progression(
                chapter_num or 1, emotional_state
            )
            results['warnings'].extend(arc_warnings)
        
        # Validate chapter references
        if chapter_num:
            ref_valid, ref_issues = self.validate_chapter_references(content, chapter_num)
            if not ref_valid:
                results['issues'].extend(ref_issues)
                results['is_valid'] = False
        
        # Validate signature phrases
        if chapter_num:
            sig_valid, sig_issues = self.validate_signature_phrase_rotation(content, chapter_num)
            if not sig_valid:
                results['issues'].extend(sig_issues)
                results['is_valid'] = False
        
        # Validate permission frames
        perm_valid, perm_issues = self.validate_permission_frames(content)
        if not perm_valid:
            results['issues'].extend(perm_issues)
            results['is_valid'] = False
        
        return results


class EditorTracker:
    """Tracks issues for editor review with file, line, scenario, issue details"""
    
    def __init__(self, tracker_file: Path = None):
        if tracker_file is None:
            tracker_file = Path("content") / "editor_tracker" / "issues.yaml"
        self.tracker_file = tracker_file
        self.tracker_file.parent.mkdir(parents=True, exist_ok=True)
        self.issues = []
    
    def add_issue(self, file_path: str, line_number: Optional[int], 
                  scenario: str, issue_type: str, details: List[str]):
        """Add issue to tracker"""
        issue = {
            'file_path': file_path,
            'line_number': line_number,
            'scenario': scenario,
            'issue_type': issue_type,
            'details': details,
            'timestamp': datetime.now().isoformat(),
            'status': 'pending_review'
        }
        self.issues.append(issue)
        self._save()
    
    def _save(self):
        """Save tracker to file"""
        with open(self.tracker_file, 'w', encoding='utf-8') as f:
            yaml.dump({'issues': self.issues}, f, default_flow_style=False)
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get statistics on tracked issues"""
        if not self.issues:
            return {'total': 0}
        
        by_type = {}
        for issue in self.issues:
            issue_type = issue.get('issue_type', 'unknown')
            by_type[issue_type] = by_type.get(issue_type, 0) + 1
        
        return {
            'total': len(self.issues),
            'by_type': by_type,
            'pending': len([i for i in self.issues if i.get('status') == 'pending_review'])
        }

