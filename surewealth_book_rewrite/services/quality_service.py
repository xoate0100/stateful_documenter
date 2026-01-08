#!/usr/bin/env python3
"""
Quality Service
Validates content against all quality dimensions and quantifies scores
"""

import re
from typing import Dict, List, Any, Tuple
from pathlib import Path

# Import existing validators
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from meta_framework.content_quality.content_validator import ContentValidator


class QualityService:
    """
    Validates content and quantifies quality scores
    Provides detailed quality reports with actionable feedback
    """
    
    def __init__(self):
        self.validator = ContentValidator()
        # Will add sales copy validator when implemented
        # self.sales_copy_validator = SalesCopyValidator()
    
    def validate_content(
        self,
        content: str,
        metadata: Dict[str, Any],
        quality_dimensions: List[str] = None
    ) -> Dict[str, Any]:
        """
        Validate content against quality dimensions
        
        Args:
            content: Content to validate
            metadata: Content metadata
            quality_dimensions: List of dimensions to check (None = all)
            
        Returns:
            QualityReport with scores, issues, and suggestions
        """
        if quality_dimensions is None:
            quality_dimensions = [
                'structural',
                'sales_copy',
                'emotional',
                'conversion',
                'authority',
                'trust'
            ]
        
        report = {
            'metrics': {},
            'issues': [],
            'warnings': [],
            'suggestions': []
        }
        
        # Validate each dimension
        for dimension in quality_dimensions:
            if dimension == 'structural':
                score, issues, warnings = self._validate_structural(content, metadata)
                report['metrics']['structural'] = score
                report['issues'].extend(issues)
                report['warnings'].extend(warnings)
            
            elif dimension == 'sales_copy':
                score, issues, warnings = self._validate_sales_copy(content, metadata)
                report['metrics']['sales_copy'] = score
                report['issues'].extend(issues)
                report['warnings'].extend(warnings)
            
            elif dimension == 'emotional':
                score, issues, warnings = self._validate_emotional(content, metadata)
                report['metrics']['emotional'] = score
                report['issues'].extend(issues)
                report['warnings'].extend(warnings)
            
            elif dimension == 'conversion':
                score, issues, warnings = self._validate_conversion(content, metadata)
                report['metrics']['conversion'] = score
                report['issues'].extend(issues)
                report['warnings'].extend(warnings)
            
            elif dimension == 'authority':
                score, issues, warnings = self._validate_authority(content, metadata)
                report['metrics']['authority'] = score
                report['issues'].extend(issues)
                report['warnings'].extend(warnings)
            
            elif dimension == 'trust':
                score, issues, warnings = self._validate_trust(content, metadata)
                report['metrics']['trust'] = score
                report['issues'].extend(issues)
                report['warnings'].extend(warnings)
        
        # Generate suggestions
        report['suggestions'] = self._generate_suggestions(report)
        
        return report
    
    def quantify_quality(
        self,
        content: str,
        metadata: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Quantify quality scores (0.0-1.0) for all dimensions
        
        Returns:
            QualityMetrics with scores for each dimension
        """
        report = self.validate_content(content, metadata)
        return {
            'metrics': report['metrics'],
            'overall_score': self._calculate_overall_score(report['metrics']),
            'issues': report['issues'],
            'warnings': report['warnings']
        }
    
    def _validate_structural(
        self,
        content: str,
        metadata: Dict
    ) -> Tuple[float, List[str], List[str]]:
        """Validate structural quality"""
        is_valid, issues, warnings = self.validator.validate_content(content, metadata)
        
        # Calculate score (1.0 if valid, reduced for issues)
        score = 1.0
        if issues:
            score -= len(issues) * 0.1  # -0.1 per issue
        if warnings:
            score -= len(warnings) * 0.05  # -0.05 per warning
        
        score = max(0.0, min(1.0, score))
        return score, issues, warnings
    
    def _validate_sales_copy(
        self,
        content: str,
        metadata: Dict
    ) -> Tuple[float, List[str], List[str]]:
        """Validate sales copy quality"""
        issues = []
        warnings = []
        score = 0.0
        
        # Check curiosity gaps
        curiosity_score = self._check_curiosity_gaps(content)
        score += curiosity_score * 0.25
        
        # Check emotional tone
        tone_score = self._check_emotional_tone(content)
        score += tone_score * 0.20
        
        # Check conceptual clarity
        clarity_score = self._check_conceptual_clarity(content)
        score += clarity_score * 0.20
        
        # Check future pacing
        pacing_score = self._check_future_pacing(content)
        score += pacing_score * 0.15
        
        # Check actionable tidbits
        actionable_score = self._check_actionable_tidbits(content)
        score += actionable_score * 0.10
        
        # Check delight/discovery
        delight_score = self._check_delight_discovery(content)
        score += delight_score * 0.10
        
        return score, issues, warnings
    
    def _validate_emotional(
        self,
        content: str,
        metadata: Dict
    ) -> Tuple[float, List[str], List[str]]:
        """Validate emotional quality"""
        issues = []
        warnings = []
        score = 0.0
        
        # Check emotional tone consistency
        consistency_score = self._check_emotional_consistency(content)
        score += consistency_score * 0.30
        
        # Check emotional depth
        depth_score = self._check_emotional_depth(content)
        score += depth_score * 0.30
        
        # Check connectedness
        connectedness_score = self._check_connectedness(content)
        score += connectedness_score * 0.25
        
        # Check respect for intelligence
        respect_score = self._check_respect_for_intelligence(content)
        score += respect_score * 0.15
        
        return score, issues, warnings
    
    def _validate_conversion(
        self,
        content: str,
        metadata: Dict
    ) -> Tuple[float, List[str], List[str]]:
        """Validate conversion quality"""
        issues = []
        warnings = []
        score = 0.0
        
        # Check CTA effectiveness
        cta_score = self._check_cta_effectiveness(content, metadata)
        score += cta_score * 0.40
        
        # Check engagement tactics
        engagement_score = self._check_engagement_tactics(content)
        score += engagement_score * 0.35
        
        # Check "wanting more" elements
        wanting_more_score = self._check_wanting_more_elements(content)
        score += wanting_more_score * 0.25
        
        return score, issues, warnings
    
    def _validate_authority(
        self,
        content: str,
        metadata: Dict
    ) -> Tuple[float, List[str], List[str]]:
        """Validate authority quality"""
        issues = []
        warnings = []
        score = 0.0
        
        # Check citations
        citation_score = self._check_citations(content)
        score += citation_score * 0.40
        
        # Check expertise signals
        expertise_score = self._check_expertise_signals(content)
        score += expertise_score * 0.35
        
        # Check credibility
        credibility_score = self._check_credibility(content)
        score += credibility_score * 0.25
        
        return score, issues, warnings
    
    def _validate_trust(
        self,
        content: str,
        metadata: Dict
    ) -> Tuple[float, List[str], List[str]]:
        """Validate trust quality"""
        issues = []
        warnings = []
        score = 0.0
        
        # Check transparency
        transparency_score = self._check_transparency(content)
        score += transparency_score * 0.35
        
        # Check honesty
        honesty_score = self._check_honesty(content)
        score += honesty_score * 0.35
        
        # Check no manipulation
        no_manipulation_score = self._check_no_manipulation(content)
        score += no_manipulation_score * 0.30
        
        return score, issues, warnings
    
    # Placeholder methods for quality checks (to be implemented)
    def _check_curiosity_gaps(self, content: str) -> float:
        """Check for curiosity gaps (0.0-1.0)"""
        # Pattern: Questions without immediate answers
        questions = re.findall(r'\?', content)
        # Pattern: "You'll discover..." or "Coming up..."
        discovery_patterns = len(re.findall(
            r"(you'll discover|coming up|in the next|you'll learn|you'll see)",
            content, re.IGNORECASE
        ))
        
        # Score based on presence of curiosity elements
        if discovery_patterns >= 2 or len(questions) >= 5:
            return 0.8
        elif discovery_patterns >= 1 or len(questions) >= 3:
            return 0.6
        else:
            return 0.3
    
    def _check_emotional_tone(self, content: str) -> float:
        """Check emotional tone consistency (0.0-1.0)"""
        # Check for fawning language
        fawning_patterns = len(re.findall(
            r"(you're so smart|you're clearly|you're obviously|you're such)",
            content, re.IGNORECASE
        ))
        
        # Check for pedantic language
        pedantic_patterns = len(re.findall(
            r"(let me explain this simple|in very basic terms|anyone can understand)",
            content, re.IGNORECASE
        ))
        
        if fawning_patterns > 0 or pedantic_patterns > 0:
            return 0.4  # Penalize fawning/pedantic
        
        # Check for respectful, intelligent tone
        respectful_patterns = len(re.findall(
            r"(if you're|you might|you probably|you're likely)",
            content, re.IGNORECASE
        ))
        
        if respectful_patterns >= 3:
            return 0.9
        else:
            return 0.7
    
    def _check_conceptual_clarity(self, content: str) -> float:
        """Check conceptual clarity (0.0-1.0)"""
        # Check for jargon without explanation
        jargon_patterns = len(re.findall(
            r"\b(RMD|IRA|401\(k\)|Roth|annuity)\b",
            content, re.IGNORECASE
        ))
        
        # Check for explanation patterns
        explanation_patterns = len(re.findall(
            r"(think of it|in other words|to put it simply|here's what)",
            content, re.IGNORECASE
        ))
        
        if jargon_patterns > 0 and explanation_patterns >= jargon_patterns:
            return 0.8
        elif jargon_patterns == 0:
            return 0.9
        else:
            return 0.5
    
    def _check_future_pacing(self, content: str) -> float:
        """Check future pacing (0.0-1.0)"""
        future_patterns = len(re.findall(
            r"(imagine|picture yourself|in \d+ years|by age \d+|envision|visualize)",
            content, re.IGNORECASE
        ))
        
        if future_patterns >= 2:
            return 0.9
        elif future_patterns >= 1:
            return 0.6
        else:
            return 0.3
    
    def _check_actionable_tidbits(self, content: str) -> float:
        """Check actionable tidbits (0.0-1.0)"""
        # Check for "Quick Start" or actionable sections
        actionable_sections = len(re.findall(
            r"(quick start|actionable|you can|steps to|how to)",
            content, re.IGNORECASE
        ))
        
        if actionable_sections >= 3:
            return 0.9
        elif actionable_sections >= 1:
            return 0.6
        else:
            return 0.3
    
    def _check_delight_discovery(self, content: str) -> float:
        """Check delight/discovery elements (0.0-1.0)"""
        discovery_patterns = len(re.findall(
            r"(here's what might surprise you|you might not know|most people don't realize|here's something interesting)",
            content, re.IGNORECASE
        ))
        
        if discovery_patterns >= 2:
            return 0.9
        elif discovery_patterns >= 1:
            return 0.6
        else:
            return 0.3
    
    def _check_emotional_consistency(self, content: str) -> float:
        """Check emotional tone consistency (0.0-1.0)"""
        # Simplified check - would need more sophisticated analysis
        return 0.8
    
    def _check_emotional_depth(self, content: str) -> float:
        """Check emotional depth (0.0-1.0)"""
        # Check for "you" language
        you_count = len(re.findall(r'\byou\b', content, re.IGNORECASE))
        word_count = len(re.findall(r'\b\w+\b', content))
        you_ratio = you_count / word_count if word_count > 0 else 0
        
        if 0.02 <= you_ratio <= 0.05:  # Good balance
            return 0.9
        elif you_ratio > 0.05:
            return 0.7  # Too much "you"
        else:
            return 0.5  # Not enough personal connection
    
    def _check_connectedness(self, content: str) -> float:
        """Check connectedness (0.0-1.0)"""
        # Check for relatable scenarios
        scenario_patterns = len(re.findall(
            r"(if you're like|many people|most retirees|you might be)",
            content, re.IGNORECASE
        ))
        
        if scenario_patterns >= 3:
            return 0.9
        elif scenario_patterns >= 1:
            return 0.6
        else:
            return 0.4
    
    def _check_respect_for_intelligence(self, content: str) -> float:
        """Check respect for intelligence (0.0-1.0)"""
        # Check for fawning
        fawning = len(re.findall(
            r"(you're so|you're clearly|you're obviously)",
            content, re.IGNORECASE
        ))
        
        # Check for pedantic
        pedantic = len(re.findall(
            r"(let me explain this simple|in very basic terms)",
            content, re.IGNORECASE
        ))
        
        if fawning > 0 or pedantic > 0:
            return 0.3
        
        return 0.9
    
    def _check_cta_effectiveness(self, content: str, metadata: Dict) -> float:
        """Check CTA effectiveness (0.0-1.0)"""
        # Check for CTA presence
        cta_patterns = len(re.findall(
            r"(if there were|would you want to know|you can|get started|learn more)",
            content, re.IGNORECASE
        ))
        
        if cta_patterns >= 1:
            return 0.8
        else:
            return 0.4
    
    def _check_engagement_tactics(self, content: str) -> float:
        """Check engagement tactics (0.0-1.0)"""
        # Check for hooks, questions, stories
        hooks = len(re.findall(r'^#', content, re.MULTILINE))
        questions = len(re.findall(r'\?', content))
        
        if hooks >= 3 and questions >= 5:
            return 0.9
        elif hooks >= 2 and questions >= 3:
            return 0.7
        else:
            return 0.5
    
    def _check_wanting_more_elements(self, content: str) -> float:
        """Check "wanting more" elements (0.0-1.0)"""
        # Check for cliffhangers, incomplete thoughts
        wanting_more_patterns = len(re.findall(
            r"(but here's what|the difference\?|you'll discover|coming up)",
            content, re.IGNORECASE
        ))
        
        if wanting_more_patterns >= 3:
            return 0.9
        elif wanting_more_patterns >= 1:
            return 0.6
        else:
            return 0.3
    
    def _check_citations(self, content: str) -> float:
        """Check citations (0.0-1.0)"""
        citation_patterns = len(re.findall(
            r"(according to|based on|research shows|study found|data indicates)",
            content, re.IGNORECASE
        ))
        
        if citation_patterns >= 3:
            return 0.9
        elif citation_patterns >= 1:
            return 0.6
        else:
            return 0.4
    
    def _check_expertise_signals(self, content: str) -> float:
        """Check expertise signals (0.0-1.0)"""
        # Check for specific numbers, calculations, insights
        numbers = len(re.findall(r'\$\d+[,\d]*|\d+%', content))
        
        if numbers >= 5:
            return 0.9
        elif numbers >= 2:
            return 0.7
        else:
            return 0.5
    
    def _check_credibility(self, content: str) -> float:
        """Check credibility (0.0-1.0)"""
        # Simplified - would need more sophisticated analysis
        return 0.8
    
    def _check_transparency(self, content: str) -> float:
        """Check transparency (0.0-1.0)"""
        # Check for honest language
        transparent_patterns = len(re.findall(
            r"(honestly|frankly|to be clear|the truth is)",
            content, re.IGNORECASE
        ))
        
        if transparent_patterns >= 1:
            return 0.9
        else:
            return 0.7
    
    def _check_honesty(self, content: str) -> float:
        """Check honesty (0.0-1.0)"""
        # Check for no false promises
        promise_patterns = len(re.findall(
            r"(guaranteed|promise|always|never fails)",
            content, re.IGNORECASE
        ))
        
        if promise_patterns == 0:
            return 0.9
        else:
            return 0.6
    
    def _check_no_manipulation(self, content: str) -> float:
        """Check for no manipulation (0.0-1.0)"""
        # Check for manipulative language
        manipulative_patterns = len(re.findall(
            r"(act now|limited time|don't miss|urgent|last chance)",
            content, re.IGNORECASE
        ))
        
        if manipulative_patterns == 0:
            return 0.9
        else:
            return 0.5
    
    def _calculate_overall_score(self, metrics: Dict[str, float]) -> float:
        """Calculate overall quality score"""
        weights = {
            'structural': 0.20,
            'sales_copy': 0.25,
            'emotional': 0.20,
            'conversion': 0.15,
            'authority': 0.10,
            'trust': 0.10
        }
        
        score = sum(
            metrics.get(dimension, 0.0) * weight
            for dimension, weight in weights.items()
        )
        return score
    
    def _generate_suggestions(self, report: Dict) -> List[str]:
        """Generate improvement suggestions"""
        suggestions = []
        
        for dimension, score in report['metrics'].items():
            if score < 0.7:
                suggestions.append(
                    f"Improve {dimension} quality (current: {score:.2f}, target: 0.85+)"
                )
        
        return suggestions

