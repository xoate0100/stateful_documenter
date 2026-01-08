#!/usr/bin/env python3
"""
Content Generation Orchestrator
Manages workflow, state, and iterative improvement loop
"""

import uuid
from datetime import datetime
from typing import Dict, List, Any, Optional
from pathlib import Path
import json
import yaml


class ContentOrchestrator:
    """
    Orchestrates content generation with iterative improvement
    Manages state, coordinates services, tracks metrics
    """
    
    def __init__(self, state_dir: Path = None):
        if state_dir is None:
            state_dir = Path(__file__).parent.parent / "state" / "generation"
        self.state_dir = state_dir
        self.state_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize services (will be injected)
        self.prompt_service = None
        self.quality_service = None
        self.emotional_service = None
        self.conversion_service = None
        self.authority_service = None
        self.trust_service = None
        self.agentic_chat = None
        
        # Cursor integration
        self.cursor_chat = None  # Will be injected with Cursor chat function
    
    def generate_content(
        self,
        topic: str,
        metadata: Dict[str, Any],
        target_metrics: Dict[str, float],
        max_iterations: int = 5,
        ai_generator=None
    ) -> Dict[str, Any]:
        """
        Generate content with iterative improvement
        
        Args:
            topic: Content topic
            metadata: Content metadata
            target_metrics: Target quality scores (0.0-1.0)
            max_iterations: Maximum improvement iterations
            ai_generator: AI content generator function
            
        Returns:
            ContentResult with final content and metrics
        """
        request_id = str(uuid.uuid4())
        state = self._initialize_state(request_id, topic, metadata, target_metrics)
        
        # Phase 1: Initial Generation
        initial_content = self._generate_initial_content(topic, metadata, ai_generator)
        initial_metrics = self._validate_content(initial_content, metadata)
        
        state['iterations'].append({
            'iteration_number': 1,
            'timestamp': datetime.now().isoformat(),
            'content_version': 'v1',
            'prompt_version': 'v1',
            'quality_metrics': initial_metrics,
            'issues_found': self._identify_issues(initial_metrics, target_metrics),
            'improvements_made': [],
            'service_calls': [],
            'improvement_delta': 0.0
        })
        
        self._save_state(state)
        
        # Phase 2: Iterative Improvement
        current_content = initial_content
        current_metrics = initial_metrics
        current_score = self._calculate_overall_score(current_metrics)
        
        for iteration in range(2, max_iterations + 1):
            # Check if we've met targets
            if self._meets_targets(current_metrics, target_metrics):
                break
            
            # Identify highest-priority issues
            issues = self._prioritize_issues(current_metrics, target_metrics)
            if not issues:
                break
            
            # Improve content
            improved_content, improvements = self._improve_content(
                current_content,
                issues,
                metadata,
                ai_generator
            )
            
            # Validate improved content
            improved_metrics = self._validate_content(improved_content, metadata)
            improved_score = self._calculate_overall_score(improved_metrics)
            
            # Check if we improved
            if improved_score <= current_score:
                # No improvement, try different approach or stop
                break
            
            # Update state
            iteration_state = {
                'iteration_number': iteration,
                'timestamp': datetime.now().isoformat(),
                'content_version': f'v{iteration}',
                'quality_metrics': improved_metrics,
                'issues_found': self._identify_issues(improved_metrics, target_metrics),
                'improvements_made': improvements,
                'service_calls': [],  # Will be populated by services
                'improvement_delta': improved_score - current_score
            }
            state['iterations'].append(iteration_state)
            
            current_content = improved_content
            current_metrics = improved_metrics
            current_score = improved_score
            
            self._save_state(state)
        
        # Phase 3: Final Validation
        final_metrics = self._validate_content(current_content, metadata)
        final_score = self._calculate_overall_score(final_metrics)
        
        state['final_content'] = current_content
        state['final_metrics'] = final_metrics
        state['total_iterations'] = len(state['iterations'])
        state['improvement_trend'] = self._calculate_improvement_trend(state['iterations'])
        state['completed_at'] = datetime.now().isoformat()
        
        self._save_state(state)
        
        return {
            'request_id': request_id,
            'content': current_content,
            'metrics': final_metrics,
            'overall_score': final_score,
            'iterations': len(state['iterations']),
            'improvement_delta': final_score - self._calculate_overall_score(initial_metrics),
            'state_file': self.state_dir / f"{request_id}.yaml"
        }
    
    def _initialize_state(
        self,
        request_id: str,
        topic: str,
        metadata: Dict,
        target_metrics: Dict
    ) -> Dict:
        """Initialize generation state"""
        return {
            'request_id': request_id,
            'topic': topic,
            'metadata': metadata,
            'target_metrics': target_metrics,
            'iterations': [],
            'final_content': None,
            'final_metrics': {},
            'total_iterations': 0,
            'improvement_trend': None,
            'created_at': datetime.now().isoformat(),
            'completed_at': None
        }
    
    def _generate_initial_content(
        self,
        topic: str,
        metadata: Dict,
        ai_generator
    ) -> str:
        """Generate initial content"""
        if not self.prompt_service:
            raise ValueError("Prompt service not initialized")
        
        prompt = self.prompt_service.generate_prompt(topic, metadata)
        content = ai_generator(prompt)
        return content
    
    def _validate_content(self, content: str, metadata: Dict) -> Dict[str, float]:
        """Validate content and return metrics"""
        if not self.quality_service:
            raise ValueError("Quality service not initialized")
        
        report = self.quality_service.quantify_quality(content, metadata)
        return report['metrics']
    
    def _identify_issues(
        self,
        current_metrics: Dict[str, float],
        target_metrics: Dict[str, float]
    ) -> List[Dict[str, Any]]:
        """Identify issues based on gaps between current and target metrics"""
        issues = []
        for dimension, target_score in target_metrics.items():
            current_score = current_metrics.get(dimension, 0.0)
            gap = target_score - current_score
            if gap > 0.05:  # Significant gap
                issues.append({
                    'dimension': dimension,
                    'current_score': current_score,
                    'target_score': target_score,
                    'gap': gap,
                    'priority': 'P0' if gap > 0.20 else 'P1' if gap > 0.10 else 'P2'
                })
        return sorted(issues, key=lambda x: x['gap'], reverse=True)
    
    def _prioritize_issues(
        self,
        current_metrics: Dict[str, float],
        target_metrics: Dict[str, float]
    ) -> List[Dict[str, Any]]:
        """Prioritize issues by impact"""
        issues = self._identify_issues(current_metrics, target_metrics)
        # Return top 3 highest-priority issues
        return issues[:3]
    
    def _improve_content(
        self,
        content: str,
        issues: List[Dict],
        metadata: Dict,
        ai_generator
    ) -> tuple[str, List[Dict]]:
        """Improve content based on issues"""
        improvements = []
        improved_content = content
        
        for issue in issues:
            dimension = issue['dimension']
            
            # Route to appropriate service
            if dimension == 'emotional':
                if self.emotional_service:
                    enhanced, improvement = self.emotional_service.enhance_emotional_depth(
                        improved_content,
                        {'gap': issue['gap'], 'target_score': issue['target_score']}
                    )
                    improved_content = enhanced
                    improvements.append(improvement)
            
            elif dimension == 'conversion' or dimension == 'sales_copy':
                if self.conversion_service:
                    enhanced, improvement = self.conversion_service.enhance_conversion(
                        improved_content,
                        {'gap': issue['gap'], 'target_score': issue['target_score']}
                    )
                    improved_content = enhanced
                    improvements.append(improvement)
            
            elif dimension == 'authority':
                if self.authority_service:
                    enhanced, improvement = self.authority_service.enhance_authority(
                        improved_content,
                        {'gap': issue['gap'], 'target_score': issue['target_score']}
                    )
                    improved_content = enhanced
                    improvements.append(improvement)
            
            elif dimension == 'trust':
                if self.trust_service:
                    enhanced, improvement = self.trust_service.enhance_trust(
                        improved_content,
                        {'gap': issue['gap'], 'target_score': issue['target_score']}
                    )
                    improved_content = enhanced
                    improvements.append(improvement)
        
        return improved_content, improvements
    
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
    
    def _meets_targets(
        self,
        current_metrics: Dict[str, float],
        target_metrics: Dict[str, float]
    ) -> bool:
        """Check if current metrics meet targets"""
        for dimension, target_score in target_metrics.items():
            current_score = current_metrics.get(dimension, 0.0)
            if current_score < target_score - 0.05:  # Allow 0.05 tolerance
                return False
        return True
    
    def _calculate_improvement_trend(self, iterations: List[Dict]) -> str:
        """Calculate improvement trend"""
        if len(iterations) < 2:
            return "insufficient_data"
        
        scores = [
            self._calculate_overall_score(iter['quality_metrics'])
            for iter in iterations
        ]
        
        if scores[-1] > scores[0] + 0.05:
            return "positive"
        elif scores[-1] < scores[0] - 0.05:
            return "negative"
        else:
            return "plateau"
    
    def _save_state(self, state: Dict):
        """Save state to file"""
        state_file = self.state_dir / f"{state['request_id']}.yaml"
        with open(state_file, 'w', encoding='utf-8') as f:
            yaml.dump(state, f, default_flow_style=False, allow_unicode=True)

