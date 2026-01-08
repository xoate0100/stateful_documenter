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
    
    def validate_content(self, content: str, metadata: Dict[str, Any], 
                        expected_length: str = None) -> Tuple[bool, List[str], List[str]]:
        """
        Validate content against lessons learned and edge cases
        
        Args:
            content: Content to validate
            metadata: Content metadata
            expected_length: Expected length specification (e.g., "3000-4000 words")
        
        Returns: (is_valid, issues, warnings)
        """
        self.issues = []
        self.warnings = []
        
        # P0 - CRITICAL: Length validation (must pass)
        if expected_length:
            self._check_length(content, expected_length)
        
        # P0 - CRITICAL: Compliance validation (must pass)
        self._check_compliance(content)
        
        # P0 - CRITICAL: Required elements validation (must pass)
        self._check_required_elements(content, metadata)
        
        # P0 - CRITICAL: Structure validation (must pass)
        self._check_structure_completeness(content, metadata)
        
        # P1 - HIGH: Content quality checks
        self._check_structure_variation(content, metadata)
        self._check_permission_frames(content)
        self._check_signature_phrases(content, metadata)
        self._check_ctas(content, metadata)
        self._check_story_resolution(content)
        self._check_dialogue(content)
        self._check_numbers(content)
        
        # P1 - HIGH: Repetition and specificity
        self._check_repetition(content)
        self._check_specificity(content)
        
        # P2 - MEDIUM: Additional quality checks
        self._check_citations(content)
        self._check_generic_language(content)
        
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
    
    def _check_length(self, content: str, expected_length: str):
        """P0 - CRITICAL: Validate content length against expected length"""
        word_count = len(re.findall(r'\b\w+\b', content))
        
        # Parse expected length (e.g., "3000-4000 words" or "3000 words")
        if '-' in expected_length:
            min_words, max_words = map(int, expected_length.replace(' words', '').split('-'))
        else:
            min_words = int(expected_length.replace(' words', '').replace('word', '').strip())
            max_words = min_words
        
        # Critical: Reject if below minimum
        if word_count < min_words:
            gap = min_words - word_count
            gap_pct = (gap / min_words * 100) if min_words > 0 else 0
            self.issues.append(
                f"CRITICAL: Content too short - {word_count:,} words (expected {min_words:,}-{max_words:,}). "
                f"Gap: {gap:,} words ({gap_pct:.1f}% short). Content will be rejected."
            )
        # Warning: Above maximum
        elif word_count > max_words:
            excess = word_count - max_words
            excess_pct = (excess / max_words * 100) if max_words > 0 else 0
            self.warnings.append(
                f"Content exceeds maximum - {word_count:,} words (expected {min_words:,}-{max_words:,}). "
                f"Excess: {excess:,} words ({excess_pct:.1f}% over). Consider trimming."
            )
        # Warning: Below target (middle of range)
        elif word_count < (min_words + max_words) / 2:
            target = (min_words + max_words) / 2
            gap = target - word_count
            self.warnings.append(
                f"Content below target - {word_count:,} words (target: ~{target:.0f} words). "
                f"Consider expanding by {gap:.0f} words."
            )
    
    def _check_compliance(self, content: str):
        """P0 - CRITICAL: Check for compliance violations"""
        # Load compliance enforcer
        try:
            from meta_framework.language.compliance_enforcer import ComplianceEnforcer
            enforcer = ComplianceEnforcer()
            violations = enforcer.validate_text(content)
            
            if violations:
                for violation in violations:
                    banned = violation.get('banned_phrase', 'unknown')
                    alternatives = violation.get('alternatives', [])
                    self.issues.append(
                        f"CRITICAL: Compliance violation - '{banned}' found. "
                        f"Use alternatives: {', '.join(alternatives[:3])}"
                    )
        except Exception as e:
            # If compliance enforcer not available, warn but don't block
            self.warnings.append(f"Compliance validation unavailable: {str(e)}")
    
    def _check_required_elements(self, content: str, metadata: Dict[str, Any]):
        """P0 - CRITICAL: Check for required elements based on format type"""
        format_type = metadata.get('format_type', 'unknown')
        
        if format_type == 'chapter':
            # Chapters must have: opening hook, body sections, CTA
            has_hook = bool(re.search(r'## .*[Hh]ook|## .*[Ii]ntroduction|^[^#].*[?!]', content[:500], re.MULTILINE))
            has_body = bool(re.search(r'## .+', content))
            has_cta = bool(re.search(r'## Your Next Step|## Next Step|CTA|call to action', content, re.IGNORECASE))
            
            if not has_hook:
                self.issues.append("CRITICAL: Missing opening hook or introduction")
            if not has_body:
                self.issues.append("CRITICAL: Missing body sections")
            if not has_cta:
                self.issues.append("CRITICAL: Missing CTA section")
        
        # Check for required narratives if specified
        narrative_ids = metadata.get('narrative_ids', [])
        if narrative_ids:
            # Check if narratives are actually used (basic check)
            narrative_mentions = sum(1 for nid in narrative_ids if re.search(nid.replace('_', ' '), content, re.IGNORECASE))
            if narrative_mentions == 0:
                self.warnings.append(f"Specified narratives not clearly used: {', '.join(narrative_ids)}")
    
    def _check_structure_completeness(self, content: str, metadata: Dict[str, Any]):
        """P0 - CRITICAL: Validate structure completeness"""
        format_type = metadata.get('format_type', 'unknown')
        
        if format_type == 'chapter':
            # Check for required chapter sections
            required_sections = [
                r'^# Chapter \d+:',  # Chapter title
                r'## .+',  # At least one section
            ]
            
            for pattern in required_sections:
                if not re.search(pattern, content, re.MULTILINE):
                    self.issues.append(f"CRITICAL: Missing required structure element: {pattern}")
    
    def _check_repetition(self, content: str):
        """P0 - CRITICAL: Check for exact phrase repetition and other repetitive patterns"""
        # P0 - CRITICAL: Check for exact phrase repetition (5+ words)
        words = re.findall(r'\b\w+\b', content.lower())
        
        # Check for exact phrase duplicates (5-word, 6-word, 7-word phrases)
        exact_duplicates = []
        for n in [5, 6, 7, 8, 9, 10]:  # Check 5-10 word phrases
            phrase_counts = {}
            for i in range(len(words) - n + 1):
                phrase = ' '.join(words[i:i+n])
                if phrase not in phrase_counts:
                    phrase_counts[phrase] = []
                phrase_counts[phrase].append(i)
            
            # Find phrases that appear 2+ times
            for phrase, positions in phrase_counts.items():
                if len(positions) > 1:
                    # Filter out common phrases that are okay to repeat
                    if not self._is_common_phrase(phrase):
                        exact_duplicates.append({
                            'phrase': phrase,
                            'count': len(positions),
                            'length': n
                        })
        
        if exact_duplicates:
            # Group by phrase length and get most problematic
            by_length = {}
            for dup in exact_duplicates:
                length = dup['length']
                if length not in by_length:
                    by_length[length] = []
                by_length[length].append(dup)
            
            # Report longest duplicates first (most problematic)
            for length in sorted(by_length.keys(), reverse=True):
                dups = by_length[length]
                if dups:
                    worst = max(dups, key=lambda x: x['count'])
                    self.issues.append(
                        f"CRITICAL: Exact phrase repetition detected: '{worst['phrase'][:80]}...' "
                        f"appears {worst['count']} times ({worst['length']}-word phrase). "
                        f"Must vary language while maintaining meaning."
                    )
                    break  # Report most problematic one
        
        # P0 - CRITICAL: Check for repeated sentences (exact matches, 10+ words)
        sentences = re.split(r'[.!?]+\s+', content)
        sentence_counts = {}
        for sentence in sentences:
            sentence_clean = sentence.strip().lower()
            # Only check longer sentences (10+ words) to avoid false positives
            word_count = len(re.findall(r'\b\w+\b', sentence_clean))
            if word_count >= 10:
                sentence_counts[sentence_clean] = sentence_counts.get(sentence_clean, 0) + 1
        
        repeated_sentences = {s: c for s, c in sentence_counts.items() if c > 1}
        if repeated_sentences:
            worst = max(repeated_sentences.items(), key=lambda x: x[1])
            self.issues.append(
                f"CRITICAL: Exact sentence repetition detected: '{worst[0][:80]}...' "
                f"appears {worst[1]} times. Must vary sentence structure."
            )
        
        # P1 - HIGH: Check for sentence structure repetition
        structure_patterns = [
            r"here's what (.+?) means",
            r"let me show you (.+?)",
            r"the difference\? (.+?)",
            r"but here's what (.+?) doesn't tell you",
            r"this isn't about (.+?), it's about (.+?)",
        ]
        
        structure_counts = {}
        for pattern in structure_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            if len(matches) > 2:
                structure_counts[pattern] = len(matches)
        
        if structure_counts:
            worst_pattern = max(structure_counts.items(), key=lambda x: x[1])
            self.warnings.append(
                f"Repetitive sentence structure detected: pattern appears {worst_pattern[1]} times. "
                f"Consider varying sentence structure."
            )
        
        # P1 - HIGH: Check for word frequency in close proximity (500-word windows)
        word_positions = {}
        for i, word in enumerate(words):
            if word not in word_positions:
                word_positions[word] = []
            word_positions[word].append(i)
        
        # Check for words that appear 3+ times in close proximity
        proximity_issues = []
        for word, positions in word_positions.items():
            if len(positions) >= 3 and not self._is_common_word(word):
                # Check if positions are within 500 words of each other
                for i in range(len(positions) - 2):
                    window = positions[i:i+3]
                    if window[-1] - window[0] < 500:  # Within 500 words
                        proximity_issues.append({
                            'word': word,
                            'count': len([p for p in positions if window[0] <= p <= window[-1]]),
                            'window': window[-1] - window[0]
                        })
                        break
        
        if proximity_issues:
            worst = max(proximity_issues, key=lambda x: x['count'])
            self.warnings.append(
                f"Word repetition in close proximity: '{worst['word']}' appears {worst['count']} times "
                f"within {worst['window']} words. Consider using synonyms or varying terminology."
            )
        
        # P1 - HIGH: Check for transition phrase repetition
        transition_phrases = [
            r"but here's what",
            r"the difference\?",
            r"let me show you",
            r"here's what (.+?) means",
            r"this is about",
        ]
        
        transition_counts = {}
        for pattern in transition_phrases:
            count = len(re.findall(pattern, content, re.IGNORECASE))
            if count > 2:
                transition_counts[pattern] = count
        
        if transition_counts:
            worst = max(transition_counts.items(), key=lambda x: x[1])
            self.warnings.append(
                f"Transition phrase repetition: '{worst[0]}' appears {worst[1]} times. "
                f"Consider rotating transition phrases."
            )
    
    def _is_common_phrase(self, phrase: str) -> bool:
        """Check if phrase is a common phrase that's okay to repeat"""
        common_phrases = [
            'the market is',
            'in retirement',
            'of your',
            'you can',
            'this is',
            'that is',
            'it is',
            'there are',
            'you have',
            'you need',
            'you want',
            'you should',
            'you will',
            'if you',
            'when you',
            'what you',
            'how you',
            'why you',
        ]
        return phrase in common_phrases or any(phrase.startswith(cp) for cp in common_phrases)
    
    def _is_common_word(self, word: str) -> bool:
        """Check if word is a common word that's okay to repeat"""
        common_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
            'of', 'with', 'by', 'from', 'as', 'is', 'are', 'was', 'were', 'be',
            'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will',
            'would', 'could', 'should', 'may', 'might', 'must', 'can', 'this',
            'that', 'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they',
            'your', 'his', 'her', 'its', 'our', 'their', 'retirement', 'retirees',
            'retiree', 'market', 'income', 'tax', 'taxes', 'money', 'dollar',
            'dollars', 'year', 'years', 'time', 'times'
        }
        return word.lower() in common_words
    
    def _check_specificity(self, content: str):
        """P1 - HIGH: Check for generic/vague content"""
        # Check for generic phrases
        generic_phrases = [
            r'\bsome people\b',
            r'\bmany cases\b',
            r'\boften\b',
            r'\bsometimes\b',
            r'\btypically\b',
            r'\bgenerally\b',
        ]
        
        generic_count = sum(len(re.findall(pattern, content, re.IGNORECASE)) for pattern in generic_phrases)
        if generic_count > 10:
            self.warnings.append(f"High use of generic language ({generic_count} instances). Add specific examples and concrete details.")
        
        # Check for proper nouns (specificity indicator)
        proper_nouns = len(re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', content))
        if proper_nouns < 3 and len(content) > 2000:
            self.warnings.append("Low specificity - few proper nouns or specific references. Add concrete examples, names, or specific details.")
    
    def _check_citations(self, content: str):
        """P2 - MEDIUM: Check for citations on statistical claims"""
        # Find statistical claims (numbers with % or dollar amounts in context)
        stats = re.findall(r'[\d,]+%|[\d,]+\s*(percent|percentage|rate)', content, re.IGNORECASE)
        dollar_stats = re.findall(r'\$[\d,]+.*?(cost|spend|save|lose|worth)', content, re.IGNORECASE)
        
        # Check for citation phrases
        citation_phrases = [
            r'according to',
            r'based on',
            r'research shows',
            r'studies indicate',
            r'data from',
        ]
        
        has_citations = any(re.search(pattern, content, re.IGNORECASE) for pattern in citation_phrases)
        
        if (len(stats) + len(dollar_stats)) > 3 and not has_citations:
            self.warnings.append("Statistical claims without citations. Add 'According to...' or 'Based on...' for credibility.")
    
    def _check_generic_language(self, content: str):
        """P2 - MEDIUM: Check for overly generic language"""
        # Check for vague qualifiers
        vague_qualifiers = [
            r'\bvery\b',
            r'\bquite\b',
            r'\brather\b',
            r'\bpretty\b',
            r'\bsomewhat\b',
        ]
        
        vague_count = sum(len(re.findall(pattern, content, re.IGNORECASE)) for pattern in vague_qualifiers)
        if vague_count > 15:
            self.warnings.append(f"High use of vague qualifiers ({vague_count} instances). Use more specific, concrete language.")
    
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

