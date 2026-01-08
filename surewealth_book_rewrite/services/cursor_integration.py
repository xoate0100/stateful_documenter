#!/usr/bin/env python3
"""
Cursor IDE Integration Layer
Optimized for Cursor IDE's built-in chat agent
Supports on-the-fly responses and edits
"""

from typing import Dict, List, Any, Optional, Union
from pathlib import Path
import json
from datetime import datetime

from .orchestrator import ContentOrchestrator
from .quality_service import QualityService


class CursorContentAgent:
    """
    Cursor IDE-optimized content generation agent
    Handles both full content generation and incremental edits
    Uses intelligent prompt refinement via Cursor's chat capabilities
    """
    
    def __init__(self, state_dir: Path = None):
        self.orchestrator = ContentOrchestrator(state_dir)
        self.orchestrator.quality_service = QualityService()
        self.cursor_chat: Optional[Callable[[str], str]] = None
    
    def generate_content(
        self,
        request: Union[str, Dict[str, Any]],
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Generate content from Cursor chat request
        
        Args:
            request: Either a string (simple request) or dict (detailed request)
            context: Optional context (file content, selection, etc.)
            
        Returns:
            Content result with generated content and metrics
        """
        # Parse request
        if isinstance(request, str):
            parsed_request = self._parse_simple_request(request, context)
        else:
            parsed_request = request
        
        # Generate content
        result = self.orchestrator.generate_content(
            topic=parsed_request.get('topic', 'Content'),
            metadata=parsed_request.get('metadata', {}),
            target_metrics=parsed_request.get('target_metrics', self._default_metrics()),
            max_iterations=parsed_request.get('max_iterations', 5),
            ai_generator=self._cursor_ai_generator
        )
        
        return result
    
    def improve_content(
        self,
        content: str,
        improvement_request: str,
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Improve existing content based on request
        
        Args:
            content: Existing content to improve
            improvement_request: What to improve (e.g., "add curiosity gaps", "improve emotional tone")
            context: Optional context
            
        Returns:
            Improved content with metrics
        """
        # Analyze current content
        current_metrics = self.orchestrator.quality_service.quantify_quality(
            content,
            context or {}
        )
        
        # Parse improvement request
        improvement_type = self._parse_improvement_request(improvement_request)
        
        # Generate improvement prompt via agentic chat
        improvement_prompt = self._generate_improvement_prompt(
            content,
            improvement_type,
            current_metrics,
            context
        )
        
        # Generate improved content
        improved_content = self._cursor_ai_generator(improvement_prompt)
        
        # Validate improvement
        improved_metrics = self.orchestrator.quality_service.quantify_quality(
            improved_content,
            context or {}
        )
        
        return {
            'content': improved_content,
            'metrics': improved_metrics['metrics'],
            'improvement_delta': self._calculate_improvement_delta(
                current_metrics['metrics'],
                improved_metrics['metrics']
            ),
            'improvement_type': improvement_type
        }
    
    def edit_content(
        self,
        content: str,
        edit_request: str,
        edit_scope: str = "targeted",  # "targeted" (single line/section) or "comprehensive"
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Edit content based on specific request
        
        Args:
            content: Content to edit
            edit_request: Specific edit request (e.g., "fix phrase repetition on line 194")
            edit_scope: "targeted" for single edits, "comprehensive" for category-wide
            context: Optional context (line numbers, selections, etc.)
            
        Returns:
            Edited content with change summary
        """
        # Parse edit request
        edit_instruction = self._parse_edit_request(edit_request, context)
        
        # Generate edit prompt
        edit_prompt = self._generate_edit_prompt(
            content,
            edit_instruction,
            edit_scope,
            context
        )
        
        # Generate edited content
        edited_content = self._cursor_ai_generator(edit_prompt)
        
        # Validate edit
        edited_metrics = self.orchestrator.quality_service.quantify_quality(
            edited_content,
            context or {}
        )
        
        return {
            'content': edited_content,
            'metrics': edited_metrics['metrics'],
            'changes_made': edit_instruction.get('changes', []),
            'edit_scope': edit_scope
        }
    
    def quality_check(
        self,
        content: str,
        dimensions: Optional[List[str]] = None,
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Quality check content and return actionable feedback
        
        Args:
            content: Content to check
            dimensions: Specific dimensions to check (None = all)
            context: Optional context
            
        Returns:
            Quality report with scores, issues, and intelligent suggestions
        """
        report = self.orchestrator.quality_service.validate_content(
            content,
            context or {},
            dimensions
        )
        
        # Generate intelligent improvement suggestions via agentic chat
        suggestions = self._generate_intelligent_suggestions(
            content,
            report,
            context
        )
        
        report['intelligent_suggestions'] = suggestions
        
        return report
    
    def _parse_simple_request(self, request: str, context: Dict = None) -> Dict[str, Any]:
        """Parse simple string request into structured format"""
        # Use agentic chat to parse request intelligently
        parse_prompt = f"""
Parse this content generation request into structured format:

Request: "{request}"
Context: {json.dumps(context or {}, indent=2)}

Extract:
1. Topic/subject
2. Format type (chapter, post, email, etc.)
3. Persona/audience
4. Funnel stage
5. Length requirements
6. Any specific requirements

Return JSON format:
{{
    "topic": "...",
    "metadata": {{
        "format_type": "...",
        "persona": "...",
        "funnel_stage": "...",
        "length": "..."
    }},
    "target_metrics": {{
        "structural": 0.95,
        "sales_copy": 0.90,
        "emotional": 0.85,
        "conversion": 0.90,
        "authority": 0.85,
        "trust": 0.90
    }},
    "max_iterations": 5
}}
"""
        
        # Use Cursor chat to parse
        parsed = self._cursor_chat_parse(parse_prompt)
        return json.loads(parsed) if isinstance(parsed, str) else parsed
    
    def _parse_improvement_request(self, request: str) -> Dict[str, Any]:
        """Parse improvement request into structured format"""
        # Map common requests to improvement types
        improvement_map = {
            'curiosity': 'sales_copy',
            'curiosity gaps': 'sales_copy',
            'emotional': 'emotional',
            'emotional tone': 'emotional',
            'conversion': 'conversion',
            'cta': 'conversion',
            'authority': 'authority',
            'citations': 'authority',
            'trust': 'trust',
            'clarity': 'sales_copy',
            'pacing': 'sales_copy',
            'engagement': 'conversion'
        }
        
        request_lower = request.lower()
        improvement_type = None
        
        for key, value in improvement_map.items():
            if key in request_lower:
                improvement_type = value
                break
        
        return {
            'type': improvement_type or 'general',
            'request': request,
            'priority': 'P0' if any(word in request_lower for word in ['critical', 'must', 'required']) else 'P1'
        }
    
    def _parse_edit_request(self, request: str, context: Dict = None) -> Dict[str, Any]:
        """Parse edit request into structured format"""
        # Use agentic chat to parse edit request
        parse_prompt = f"""
Parse this edit request:

Request: "{request}"
Context: {json.dumps(context or {}, indent=2)}

Extract:
1. Edit type (fix, add, remove, replace, improve)
2. Target location (line number, section, pattern)
3. Specific changes needed
4. Quality dimension affected

Return JSON format:
{{
    "edit_type": "...",
    "target": "...",
    "changes": ["..."],
    "dimension": "..."
}}
"""
        
        parsed = self._cursor_chat_parse(parse_prompt)
        return json.loads(parsed) if isinstance(parsed, str) else parsed
    
    def _generate_improvement_prompt(
        self,
        content: str,
        improvement_type: Dict[str, Any],
        current_metrics: Dict[str, Any],
        context: Optional[Dict] = None
    ) -> str:
        """Generate intelligent improvement prompt via agentic chat"""
        
        improvement_prompt = f"""
You are a content improvement specialist. Improve this content to enhance {improvement_type['type']} quality.

Current Content:
{content[:2000]}...

Current Metrics:
{json.dumps(current_metrics.get('metrics', {}), indent=2)}

Improvement Request: {improvement_type['request']}
Priority: {improvement_type['priority']}

Context: {json.dumps(context or {}, indent=2)}

IMPROVEMENT GUIDELINES:

1. **Preserve existing quality**: Don't break what's already good
2. **Targeted enhancement**: Focus specifically on {improvement_type['type']} dimension
3. **Natural integration**: Make improvements feel natural, not forced
4. **Maintain voice**: Keep the same voice and tone
5. **Respect intelligence**: Don't be pedantic or fawning

For {improvement_type['type']} improvements specifically:
{self._get_improvement_guidelines(improvement_type['type'])}

Generate improved content that:
- Addresses the improvement request
- Maintains or improves other quality dimensions
- Feels natural and human
- Respects reader intelligence
- Optimizes for conversion, authority, and trust

Return the complete improved content.
"""
        
        return improvement_prompt
    
    def _generate_edit_prompt(
        self,
        content: str,
        edit_instruction: Dict[str, Any],
        edit_scope: str,
        context: Optional[Dict] = None
    ) -> str:
        """Generate intelligent edit prompt"""
        
        if edit_scope == "targeted":
            # Single line/section edit
            edit_prompt = f"""
Make this specific edit to the content:

Content:
{content}

Edit Request: {edit_instruction.get('request', '')}
Target: {edit_instruction.get('target', 'entire content')}
Edit Type: {edit_instruction.get('edit_type', 'improve')}
Changes Needed: {edit_instruction.get('changes', [])}

Make ONLY the requested edit. Preserve everything else exactly as is.
Return the complete edited content.
"""
        else:
            # Comprehensive category-wide edit
            edit_prompt = f"""
Make comprehensive edits to improve {edit_instruction.get('dimension', 'quality')}:

Content:
{content}

Edit Request: {edit_instruction.get('request', '')}
Dimension: {edit_instruction.get('dimension', 'general')}
Changes Needed: {edit_instruction.get('changes', [])}

Apply the edits throughout the content where appropriate.
Maintain consistency and natural flow.
Return the complete edited content.
"""
        
        return edit_prompt
    
    def _generate_intelligent_suggestions(
        self,
        content: str,
        report: Dict[str, Any],
        context: Optional[Dict] = None
    ) -> List[Dict[str, Any]]:
        """Generate intelligent improvement suggestions via agentic chat"""
        
        suggestions_prompt = f"""
Analyze this content quality report and generate intelligent, actionable improvement suggestions.

Content (first 1500 chars):
{content[:1500]}...

Quality Report:
{json.dumps(report, indent=2)}

Context: {json.dumps(context or {}, indent=2)}

Generate 3-5 specific, actionable improvement suggestions. For each suggestion:
1. Identify the specific issue
2. Explain why it matters
3. Provide concrete improvement steps
4. Show example of good vs. bad
5. Estimate impact on quality score

Return JSON format:
{{
    "suggestions": [
        {{
            "issue": "...",
            "why_it_matters": "...",
            "improvement_steps": ["..."],
            "example_good": "...",
            "example_bad": "...",
            "estimated_impact": 0.0-1.0,
            "priority": "P0|P1|P2"
        }}
    ]
}}
"""
        
        suggestions = self._cursor_chat_parse(suggestions_prompt)
        return json.loads(suggestions) if isinstance(suggestions, str) else suggestions
    
    def _get_improvement_guidelines(self, improvement_type: str) -> str:
        """Get specific improvement guidelines for type"""
        guidelines = {
            'sales_copy': """
- Add 2-3 strategic curiosity gaps (questions without immediate answers)
- Ensure emotional tone is consistent and authentic
- Improve conceptual clarity without being pedantic
- Add future pacing (visioning language)
- Include actionable tidbits
- Add delight/discovery elements (surprising insights)
""",
            'emotional': """
- Enhance emotional depth (personal connection, relatable scenarios)
- Ensure emotional tone consistency (no jarring shifts)
- Improve connectedness (use "you" language appropriately)
- Validate psychological journey (appropriate emotional transitions)
- Ensure respect for intelligence (not fawning or pedantic)
""",
            'conversion': """
- Improve CTA effectiveness (clear, appropriate for funnel stage)
- Add engagement tactics (hooks, questions, stories)
- Ensure "wanting more" elements (curiosity gaps, cliffhangers)
- Optimize for action (clear next steps)
""",
            'authority': """
- Add specific citations (study names, dates, sources)
- Include expertise signals (calculations, insights, data)
- Enhance credibility (authoritative but approachable tone)
""",
            'trust': """
- Ensure transparency (honest language, no hidden agendas)
- Validate honesty (no false promises, realistic expectations)
- Check for no manipulation (no urgency tactics, no fearmongering)
- Respect intelligence (assume reader is smart)
"""
        }
        
        return guidelines.get(improvement_type, "Improve overall quality while maintaining existing strengths.")
    
    def _cursor_ai_generator(self, prompt: str) -> str:
        """Generate content using Cursor's AI chat"""
        if not self.cursor_chat:
            raise ValueError(
                "Cursor chat not initialized. Set cursor_chat function."
            )
        
        # Use Cursor chat to generate content
        response = self.cursor_chat(prompt)
        if isinstance(response, str):
            return response
        return response.get('content', '')
    
    def _cursor_chat_parse(self, prompt: str) -> Union[str, Dict]:
        """Use Cursor chat for parsing/analysis"""
        if not self.cursor_chat:
            raise ValueError("Cursor chat not initialized.")
        
        response = self.cursor_chat(prompt)
        return response
    
    def _default_metrics(self) -> Dict[str, float]:
        """Default target metrics"""
        return {
            "structural": 0.95,
            "sales_copy": 0.90,
            "emotional": 0.85,
            "conversion": 0.90,
            "authority": 0.85,
            "trust": 0.90
        }
    
    def _calculate_improvement_delta(
        self,
        current_metrics: Dict[str, float],
        improved_metrics: Dict[str, float]
    ) -> Dict[str, float]:
        """Calculate improvement delta"""
        return {
            dimension: improved_metrics.get(dimension, 0.0) - current_metrics.get(dimension, 0.0)
            for dimension in set(current_metrics.keys()) | set(improved_metrics.keys())
        }

