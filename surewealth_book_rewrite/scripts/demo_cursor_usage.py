#!/usr/bin/env python3
"""
Real Cursor IDE Usage Demonstration
Shows how to use the system in Cursor IDE with actual content generation
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from services.cursor_wrapper import create_cursor_agent
from ai_prompts.prompt_builder import PromptBuilder
from scripts.generate_content_with_quality import generate_content


def demonstrate_cursor_usage():
    """
    Demonstrate how to use the system in Cursor IDE
    
    In Cursor IDE, you would:
    1. Import the agent
    2. Use Cursor's chat function
    3. Generate/improve/edit content
    """
    
    print("=" * 80)
    print("CURSOR IDE USAGE DEMONSTRATION")
    print("=" * 80)
    print()
    
    # Step 1: Initialize (in Cursor IDE, cursor_chat would be the actual chat function)
    print("STEP 1: Initialize Agent")
    print("-" * 80)
    print("""
# In Cursor IDE Python file or chat:

from services.cursor_wrapper import create_cursor_agent

# cursor_chat is Cursor IDE's chat function
agent = create_cursor_agent(cursor_chat)
""")
    print()
    
    # Step 2: Generate blog post
    print("STEP 2: Generate Blog Post")
    print("-" * 80)
    print("""
# In Cursor chat, simply ask:

"Generate a blog post about SECURE Act 2.0 changes for engineers approaching retirement, 1500-2000 words, top of funnel"

# Or in Python:

result = agent.generate(
    "Generate a blog post about SECURE Act 2.0 changes for engineers approaching retirement, 1500-2000 words, top of funnel",
    context={
        "format_type": "blog_post",
        "persona": "engineer_retiree",
        "funnel_stage": "top_of_funnel"
    }
)
""")
    print()
    
    # Step 3: Quality check
    print("STEP 3: Quality Check")
    print("-" * 80)
    print("""
# In Cursor chat:

"Quality check this blog post and suggest improvements"

# Or in Python:

report = agent.quality_check(result['content'])
print(f"Scores: {report['metrics']}")
print(f"Suggestions: {report['intelligent_suggestions']}")
""")
    print()
    
    # Step 4: Improve content
    print("STEP 4: Improve Content")
    print("-" * 80)
    print("""
# In Cursor chat:

"Improve this blog post: add curiosity gaps and enhance emotional tone"

# Or in Python:

improved = agent.improve(
    result['content'],
    "add curiosity gaps and enhance emotional tone"
)
""")
    print()
    
    # Step 5: Targeted edits
    print("STEP 5: Targeted Edits")
    print("-" * 80)
    print("""
# In Cursor chat:

"Fix phrase repetition on line 45"
"Add citation for statistic about RMD changes"
"Improve the CTA at the end"

# Or in Python:

edited = agent.edit(
    content,
    "Fix phrase repetition on line 45",
    scope="targeted"
)
""")
    print()
    
    # Step 6: Comprehensive improvements
    print("STEP 6: Comprehensive Improvements")
    print("-" * 80)
    print("""
# In Cursor chat:

"Improve all CTAs in this blog post to be more engaging"
"Add citations throughout for all statistical claims"

# Or in Python:

improved = agent.edit(
    content,
    "Improve all CTAs to be more engaging",
    scope="comprehensive"
)
""")
    print()
    
    print("=" * 80)
    print("SYSTEM FEATURES")
    print("=" * 80)
    print()
    print("✓ Intelligent request parsing")
    print("✓ Agentic chat for analysis and suggestions")
    print("✓ Quality-driven iterative improvement")
    print("✓ On-the-fly targeted and comprehensive edits")
    print("✓ Quantifiable quality metrics")
    print("✓ Human-centered emotional elements")
    print("✓ Conversion, authority, and trust optimization")
    print()


if __name__ == "__main__":
    demonstrate_cursor_usage()

