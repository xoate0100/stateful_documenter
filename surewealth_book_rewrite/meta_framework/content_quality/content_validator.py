#!/usr/bin/env python3
"""
Content Quality Validator
Validates generated content against lessons_learned.json
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any, Tuple
from datetime import datetime


class ContentValidator:
    """Validates content against lessons learned"""
    
    def __init__(self, lessons_file: Path = None):
        if lessons_file is None:
            lessons_file = Path(__file__).parent / "lessons_learned.json"
        
        with open(lessons_file, 'r', encoding='utf-8') as f:
            self.lessons = json.load(f)
        
        self.issues = []
        self.warnings = []
    
    def validate_content(self, content: str, metadata: Dict[str, Any]) -> Tuple[bool, List[str], List[str]]:
        """
        Validate content against lessons learned
        
        Returns: (is_valid, issues, warnings)
        """
        self.issues = []
        self.warnings = []
        
        # Check structure variation
        self._check_structure_variation(content, metadata)
        
        # Check permission frames
        self._check_permission_frames(content)
        
        # Check signature phrases
        self._check_signature_phrases(content, metadata)
        
        # Check CTAs
        self._check_ctas(content, metadata)
        
        # Check story resolution
        self._check_story_resolution(content)
        
        # Check dialogue
        self._check_dialogue(content)
        
        # Check numbers
        self._check_numbers(content)
        
        return len(self.issues) == 0, self.issues, self.warnings
    
    def _check_structure_variation(self, content: str, metadata: Dict[str, Any]):
        """Check if structure varies from previous pieces"""
        # This would require content index - for now, just warn
        structure_patterns = [
            r"If you don't mind me asking.*?---",
            r"## The Story of",
            r"## The.*?Gap",
        ]
        
        matches = sum(1 for pattern in structure_patterns if re.search(pattern, content, re.DOTALL))
        if matches >= 2:
            self.warnings.append("Structure may be too formulaic - consider variation")
    
    def _check_permission_frames(self, content: str):
        """Check permission frame usage"""
        permission_frames = [
            r"If you don't mind me asking",
            r"Before we go any further",
            r"Let me share something with you",
        ]
        
        count = sum(len(re.findall(pattern, content, re.IGNORECASE)) for pattern in permission_frames)
        
        if count > 2:
            self.issues.append(f"Too many permission frames ({count}). Max 2 per piece.")
        elif count == 0:
            self.warnings.append("No permission frames used - consider adding one for engagement")
    
    def _check_signature_phrases(self, content: str, metadata: Dict[str, Any]):
        """Check signature phrase usage"""
        # Load signature phrases
        sig_phrases = self.lessons.get('critical_issues', {}).get('signature_phrase_repetition', {})
        
        # Check for overuse
        common_phrases = [
            "Hope is not a strategy",
            "The cost of waiting",
            "You've worked too hard to risk it now",
        ]
        
        phrase_counts = {}
        for phrase in common_phrases:
            count = len(re.findall(re.escape(phrase), content, re.IGNORECASE))
            if count > 0:
                phrase_counts[phrase] = count
        
        if len(phrase_counts) > 2:
            self.issues.append(f"Too many signature phrases ({len(phrase_counts)}). Max 1-2 per piece.")
        
        # Note: Full rotation check requires content index
        if len(phrase_counts) > 0:
            self.warnings.append("Consider rotating signature phrases to avoid repetition")
    
    def _check_ctas(self, content: str, metadata: Dict[str, Any]):
        """Check CTA count and appropriateness"""
        # Find CTA sections
        cta_patterns = [
            r"## Your Next Step",
            r"\*\*.*?\?\*\*",  # Bold question CTAs
            r"Would.*?like to know",
            r"If there were a way",
        ]
        
        cta_count = sum(1 for pattern in cta_patterns if re.search(pattern, content, re.IGNORECASE))
        
        funnel_stage = metadata.get('funnel_stage', 'unknown')
        
        if cta_count > 1:
            if funnel_stage in ['top_of_funnel', 'mid_funnel']:
                self.issues.append(f"Too many CTAs ({cta_count}) for {funnel_stage}. Should be 1 soft CTA.")
            else:
                self.warnings.append(f"Multiple CTAs ({cta_count}) - ensure appropriate for funnel stage")
        
        if cta_count == 0:
            self.warnings.append("No CTA found - content should end with appropriate CTA")
    
    def _check_story_resolution(self, content: str):
        """Check story resolution strength with concrete outcome validation"""
        issues = []
        
        # Check for vague phrases
        vague_resolutions = [
            r"everything changed",
            r"it worked",
            r"problem solved",
            r"retired\. For real this time",
        ]
        
        has_vague = any(re.search(pattern, content, re.IGNORECASE) for pattern in vague_resolutions)
        
        if has_vague:
            issues.append("Story resolution is vague - provide concrete details and outcomes")
        
        # Check for concrete resolution elements
        # Look for specific numbers, outcomes, timelines
        has_specific_numbers = bool(re.search(r'\$[\d,]+|[\d,]+%|[\d,]+ years?', content))
        has_timeline = bool(re.search(r'(after|within|over|in) [\d,]+ (months?|years?|weeks?)', content, re.IGNORECASE))
        has_before_after = bool(re.search(r'(from|to|reduced|increased|saved|cost) [\d$%]+ (to|from|by) [\d$%]+', content, re.IGNORECASE))
        
        # If story exists but lacks concrete elements, warn
        story_sections = re.findall(r'## .*Story|## .*Case Study|## .*Example', content, re.IGNORECASE)
        if story_sections and not (has_specific_numbers or has_timeline or has_before_after):
            # Check if there's a story section with resolution
            story_content = re.search(r'(## .*Story|## .*Case Study|## .*Example).*?(?=##|$)', content, re.IGNORECASE | re.DOTALL)
            if story_content:
                story_text = story_content.group(0)
                # Check if story has resolution section
                if re.search(r'(eventually|finally|in the end|result|outcome|resolution)', story_text, re.IGNORECASE):
                    issues.append("Story resolution lacks concrete outcomes - add specific numbers, timelines, or before/after comparisons")
        
        if issues:
            self.issues.extend(issues)
    
    def _check_dialogue(self, content: str):
        """Check dialogue authenticity with naturalness validation"""
        issues = []
        
        # Find all direct quotes (shorter threshold to catch more)
        direct_quotes = re.findall(r'"[^"]{20,}"', content)
        
        # Check for scripted patterns
        scripted_patterns = [
            r'"Wait[^"]*telling me',
            r'"You\'re telling me',
            r'"I\'ve been thinking',
        ]
        
        has_scripted = any(re.search(pattern, content, re.IGNORECASE) for pattern in scripted_patterns)
        
        if has_scripted:
            issues.append("Dialogue feels scripted - use indirect quotes or narrative style")
        
        # Check for natural dialogue patterns
        if direct_quotes:
            # Check for contractions (natural speech)
            has_contractions = any(re.search(r'\b(don\'t|won\'t|can\'t|it\'s|that\'s|you\'re|I\'m)', quote, re.IGNORECASE) for quote in direct_quotes)
            
            # Check for information dumps (long quotes with multiple facts)
            long_quotes = [q for q in direct_quotes if len(q) > 100]
            if len(long_quotes) > 2:
                issues.append("Too many long dialogue quotes - use indirect quotes or narrative style for information")
            
            # Check for excessive dialogue
            if len(direct_quotes) > 3:
                issues.append("Too much direct dialogue - use indirect quotes or narrative style for most character thoughts")
        
        if issues:
            self.issues.extend(issues)
    
    def _check_numbers(self, content: str):
        """Check number believability with context and range validation"""
        warnings = []
        
        # Find all dollar amounts and percentages
        dollar_amounts = re.findall(r'\$[\d,]+', content)
        percentages = re.findall(r'[\d,]+%', content)
        all_numbers = dollar_amounts + percentages
        
        # Check for too-perfect numbers
        perfect_numbers = [amt for amt in dollar_amounts if amt.endswith(',000') or amt.endswith('00')]
        perfect_percentages = [pct for pct in percentages if pct in ['25%', '50%', '75%', '100%', '10%', '20%', '30%', '40%', '60%', '70%', '80%', '90%']]
        
        if len(dollar_amounts) > 0 and len(perfect_numbers) > len(dollar_amounts) * 0.7:
            warnings.append("Many numbers are too round - consider using ranges or more realistic specifics")
        
        if len(percentages) > 0 and len(perfect_percentages) > len(percentages) * 0.6:
            warnings.append("Many percentages are too round - consider using ranges or more realistic specifics")
        
        # Check for context with numbers
        # Look for phrases like "about", "roughly", "approximately", "based on", "according to"
        context_phrases = [
            r'about \$[\d,]+',
            r'roughly \$[\d,]+',
            r'approximately \$[\d,]+',
            r'based on .*\$[\d,]+',
            r'according to .*\$[\d,]+',
        ]
        has_context = any(re.search(pattern, content, re.IGNORECASE) for pattern in context_phrases)
        
        # If many numbers but little context, warn
        if len(all_numbers) > 5 and not has_context:
            warnings.append("Numbers lack context - consider adding 'about', 'roughly', or 'based on' for believability")
        
        if warnings:
            self.warnings.extend(warnings)
    
    def get_quality_checklist(self, content: str, metadata: Dict[str, Any]) -> Dict[str, bool]:
        """Run quality checklist"""
        checklist = self.lessons.get('quality_checklist', {})
        results = {}
        
        is_valid, issues, warnings = self.validate_content(content, metadata)
        
        # Map validation results to checklist
        results['structure'] = len([i for i in issues + warnings if 'structure' in i.lower()]) == 0
        results['permission_frames'] = len([i for i in issues if 'permission frame' in i.lower()]) == 0
        results['signature_phrases'] = len([i for i in issues if 'signature phrase' in i.lower()]) == 0
        results['ctas'] = len([i for i in issues if 'cta' in i.lower()]) == 0
        results['story_resolution'] = len([i for i in issues if 'resolution' in i.lower()]) == 0
        results['dialogue'] = len([i for i in issues if 'dialogue' in i.lower()]) == 0
        results['numbers'] = len([i for i in warnings if 'number' in i.lower()]) == 0
        results['metadata'] = 'funnel_stage' in metadata and 'persona' in metadata
        
        return results
    
    def get_lessons_guidance(self, funnel_stage: str = None) -> str:
        """Get lessons learned guidance for prompt"""
        guidance = []
        
        critical_issues = self.lessons.get('critical_issues', {})
        
        # Add structure guidance
        if 'repetitive_structure' in critical_issues:
            issue = critical_issues['repetitive_structure']
            guidance.append(f"STRUCTURE: {issue['what_to_do_instead'][0]}")
        
        # Add permission frame guidance
        if 'permission_frame_overuse' in critical_issues:
            issue = critical_issues['permission_frame_overuse']
            guidance.append(f"PERMISSION FRAMES: Max 2 per piece, vary language")
        
        # Add CTA guidance based on funnel
        if funnel_stage:
            cta_guidance = self.lessons.get('funnel_mismatches', {}).get('cta_aggressiveness', {})
            if 'funnel_guidelines' in cta_guidance:
                guidelines = cta_guidance['funnel_guidelines']
                if funnel_stage in guidelines:
                    stage_guideline = guidelines[funnel_stage]
                    guidance.append(f"CTA: {stage_guideline.get('cta_count', 1)} {stage_guideline.get('cta_type', 'soft_cta')} - {stage_guideline.get('format', 'question-based')}")
        
        return "\n".join(guidance)

