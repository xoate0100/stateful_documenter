#!/usr/bin/env python3
"""
Cursor IDE Wrapper
Provides easy integration with Cursor IDE's chat agent
Can be used directly in Cursor chat or as a module
"""

from typing import Dict, List, Any, Optional, Callable

from .cursor_integration import CursorContentAgent
from .agentic_chat_service import AgenticChatService


class CursorContentWrapper:
    """
    Wrapper for easy use in Cursor IDE
    Provides simple interface for content generation and improvement
    """
    
    def __init__(self, cursor_chat_function: Optional[Callable] = None):
        """
        Initialize with Cursor chat function
        
        Args:
            cursor_chat_function: Function that takes prompt and returns response
                                  In Cursor IDE, this would be the chat agent
        """
        # Initialize agentic chat service
        self.agentic_chat = AgenticChatService(cursor_chat_function)
        
        # Initialize content agent
        self.content_agent = CursorContentAgent()
        self.content_agent.cursor_chat = cursor_chat_function
        
        # Inject agentic chat into orchestrator services
        if self.content_agent.orchestrator:
            # Services will use agentic chat when implemented
            pass
    
    def generate(
        self,
        request: str,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Generate content from simple request
        
        Usage in Cursor chat:
        "Generate a chapter about retirement planning for engineers"
        "Create a blog post about tax strategies, 2000 words"
        """
        return self.content_agent.generate_content(request, kwargs.get('context'))
    
    def improve(
        self,
        content: str,
        improvement: str,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Improve existing content
        
        Usage in Cursor chat:
        "Improve this content: add curiosity gaps"
        "Enhance emotional tone in this chapter"
        """
        return self.content_agent.improve_content(
            content,
            improvement,
            kwargs.get('context')
        )
    
    def edit(
        self,
        content: str,
        edit_request: str,
        scope: str = "targeted",
        **kwargs
    ) -> Dict[str, Any]:
        """
        Edit content based on specific request
        
        Usage in Cursor chat:
        "Fix phrase repetition on line 194"
        "Add citations throughout this chapter"
        "Improve all CTAs in this content"
        """
        return self.content_agent.edit_content(
            content,
            edit_request,
            scope,
            kwargs.get('context')
        )
    
    def quality_check(
        self,
        content: str,
        dimensions: Optional[List[str]] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Quality check content
        
        Usage in Cursor chat:
        "Quality check this chapter"
        "Check sales copy quality in this content"
        """
        return self.content_agent.quality_check(
            content,
            dimensions,
            kwargs.get('context')
        )
    
    def analyze(
        self,
        content: str,
        analysis_request: str,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Analyze content with intelligent insights
        
        Usage in Cursor chat:
        "Analyze why this content lacks engagement"
        "What's preventing this from converting better?"
        """
        # Use agentic chat for analysis
        issue = {
            'type': 'analysis',
            'request': analysis_request,
            'content': content[:2000]
        }
        
        return self.agentic_chat.analyze_issue(
            issue,
            kwargs.get('context', {})
        )


# Convenience function for Cursor IDE
def create_cursor_agent(cursor_chat_function: Callable) -> CursorContentWrapper:
    """
    Create Cursor content agent with chat function
    
    Usage in Cursor IDE:
    ```python
    from services.cursor_wrapper import create_cursor_agent
    
    # cursor_chat is the Cursor IDE chat function
    agent = create_cursor_agent(cursor_chat)
    
    # Use in Cursor chat:
    result = agent.generate("Create a chapter about retirement planning")
    ```
    """
    return CursorContentWrapper(cursor_chat_function)

