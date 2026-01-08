#!/usr/bin/env python3
"""
Agentic Chat Service
Intelligent service-to-service communication
Uses Cursor chat for intelligent analysis and suggestions
"""

from typing import Dict, List, Any, Optional, Callable
import json


class AgenticChatService:
    """
    Provides intelligent analysis and suggestions via agentic chat
    Used by services to communicate and improve content
    """
    
    def __init__(self, chat_function: Optional[Callable] = None):
        """
        Initialize with chat function
        
        Args:
            chat_function: Function that takes prompt and returns response
                          (Cursor chat, OpenAI, etc.)
        """
        self.chat_function = chat_function
    
    def analyze_issue(
        self,
        issue: Dict[str, Any],
        context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Analyze an issue and provide intelligent insights
        
        Args:
            issue: Issue to analyze (from quality service)
            context: Context (content, metrics, etc.)
            
        Returns:
            Analysis with root cause, impact, and recommendations
        """
        prompt = f"""
Analyze this content quality issue:

Issue: {json.dumps(issue, indent=2)}
Context: {json.dumps(context, indent=2)}

Provide analysis:
1. Root cause: Why does this issue exist?
2. Impact: How does this affect quality scores and reader experience?
3. Recommendations: Specific steps to fix
4. Priority: P0 (critical), P1 (high), P2 (medium)

Return JSON format:
{{
    "root_cause": "...",
    "impact": {{
        "quality_score_impact": 0.0-1.0,
        "reader_experience_impact": "high|medium|low",
        "conversion_impact": "high|medium|low"
    }},
    "recommendations": [
        {{
            "action": "...",
            "rationale": "...",
            "expected_improvement": 0.0-1.0
        }}
    ],
    "priority": "P0|P1|P2"
}}
"""
        
        response = self._chat(prompt)
        return self._parse_json_response(response)
    
    def suggest_improvement(
        self,
        issue: Dict[str, Any],
        current_content: str,
        target_metrics: Dict[str, float],
        improvement_type: str
    ) -> Dict[str, Any]:
        """
        Suggest specific improvement
        
        Args:
            issue: Issue to address
            current_content: Current content
            target_metrics: Target quality metrics
            improvement_type: Type of improvement (sales_copy, emotional, etc.)
            
        Returns:
            Improvement suggestion with specific instructions
        """
        prompt = f"""
Suggest a specific improvement to address this issue:

Issue: {json.dumps(issue, indent=2)}
Improvement Type: {improvement_type}
Target Metrics: {json.dumps(target_metrics, indent=2)}

Current Content (relevant section):
{current_content[:1500]}...

Generate improvement suggestion:
1. Specific change needed
2. Where to apply it
3. How to implement it
4. Expected outcome
5. Prompt instruction for AI to make the change

Return JSON format:
{{
    "change_description": "...",
    "target_location": "...",
    "implementation_steps": ["..."],
    "expected_outcome": "...",
    "prompt_instruction": "...",
    "estimated_improvement": 0.0-1.0
}}
"""
        
        response = self._chat(prompt)
        return self._parse_json_response(response)
    
    def refine_prompt(
        self,
        current_prompt: str,
        quality_issues: List[Dict[str, Any]],
        target_improvements: List[str]
    ) -> str:
        """
        Refine prompt based on quality feedback
        
        Args:
            current_prompt: Current prompt
            quality_issues: Issues found in generated content
            target_improvements: What to improve
            
        Returns:
            Refined prompt
        """
        prompt = f"""
Refine this content generation prompt to address quality issues:

Current Prompt:
{current_prompt}

Quality Issues Found:
{json.dumps(quality_issues, indent=2)}

Target Improvements:
{json.dumps(target_improvements, indent=2)}

Refine the prompt to:
1. Address the specific quality issues
2. Include instructions to prevent these issues
3. Add guidance for the target improvements
4. Maintain all existing good instructions
5. Make instructions clear and actionable

Return the complete refined prompt.
"""
        
        response = self._chat(prompt)
        return response if isinstance(response, str) else response.get('prompt', current_prompt)
    
    def test_hypothesis(
        self,
        hypothesis: str,
        content: str,
        test_criteria: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Test a hypothesis about content improvement
        
        Args:
            hypothesis: Hypothesis to test (e.g., "Adding curiosity gaps will improve engagement")
            content: Content to test
            test_criteria: Criteria for success
            
        Returns:
            Test results with validation
        """
        prompt = f"""
Test this hypothesis about content improvement:

Hypothesis: {hypothesis}
Content: {content[:2000]}...
Test Criteria: {json.dumps(test_criteria, indent=2)}

Analyze:
1. Does the content support the hypothesis?
2. What evidence supports/contradicts it?
3. What would need to change to validate it?
4. Confidence level (0.0-1.0)

Return JSON format:
{{
    "hypothesis": "{hypothesis}",
    "supported": true|false,
    "evidence": ["..."],
    "required_changes": ["..."],
    "confidence": 0.0-1.0
}}
"""
        
        response = self._chat(prompt)
        return self._parse_json_response(response)
    
    def generate_edit_instruction(
        self,
        edit_request: str,
        content: str,
        context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Generate specific edit instruction from natural language request
        
        Args:
            edit_request: Natural language edit request
            content: Content to edit
            context: Context (line numbers, selections, etc.)
            
        Returns:
            Structured edit instruction
        """
        prompt = f"""
Convert this edit request into a structured edit instruction:

Edit Request: "{edit_request}"
Content: {content[:2000]}...
Context: {json.dumps(context, indent=2)}

Generate structured instruction:
1. Edit type (add, remove, replace, improve, fix)
2. Target location (specific line, section, pattern)
3. Specific changes needed
4. Quality dimension affected
5. Implementation steps

Return JSON format:
{{
    "edit_type": "...",
    "target": "...",
    "changes": ["..."],
    "dimension": "...",
    "implementation_steps": ["..."],
    "prompt_instruction": "..."
}}
"""
        
        response = self._chat(prompt)
        return self._parse_json_response(response)
    
    def _chat(self, prompt: str) -> str:
        """Call chat function"""
        if not self.chat_function:
            raise ValueError("Chat function not initialized")
        
        return self.chat_function(prompt)
    
    def _parse_json_response(self, response: str) -> Dict[str, Any]:
        """Parse JSON response, handling markdown code blocks"""
        if isinstance(response, dict):
            return response
        
        # Try to extract JSON from markdown code blocks
        import re
        json_match = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', response, re.DOTALL)
        if json_match:
            return json.loads(json_match.group(1))
        
        # Try to parse as JSON directly
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            # Return as string if not JSON
            return {"response": response}

