"""
Microservices Architecture for Content Generation
Stateful, quantifiable, atomic operations for iterative content improvement
Optimized for Cursor IDE integration
"""

__version__ = "1.0.0"

# Main exports
from .cursor_wrapper import CursorContentWrapper, create_cursor_agent
from .orchestrator import ContentOrchestrator
from .quality_service import QualityService
from .agentic_chat_service import AgenticChatService
from .cursor_integration import CursorContentAgent

__all__ = [
    'CursorContentWrapper',
    'create_cursor_agent',
    'ContentOrchestrator',
    'QualityService',
    'AgenticChatService',
    'CursorContentAgent'
]
