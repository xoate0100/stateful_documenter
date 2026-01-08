# Cursor IDE Integration Guide

## Overview

This system is optimized for use with Cursor IDE's built-in chat agent. It supports:
- Full content generation
- Incremental improvements
- On-the-fly edits (single line or category-wide)
- Intelligent quality checks
- Agentic analysis

## Quick Start

### 1. Initialize in Cursor IDE

```python
# In Cursor chat or Python file
from services.cursor_wrapper import create_cursor_agent

# cursor_chat is Cursor IDE's chat function
# In Cursor, you can access it via the chat interface
agent = create_cursor_agent(cursor_chat_function)
```

### 2. Generate Content

**In Cursor Chat:**
```
Generate a chapter about retirement planning for engineers, 3000-4000 words, top of funnel
```

**In Python:**
```python
result = agent.generate(
    "Generate a chapter about retirement planning for engineers",
    context={
        "format_type": "chapter",
        "persona": "engineer_retiree",
        "funnel_stage": "top_of_funnel",
        "length": "3000-4000 words"
    }
)

print(result['content'])
print(f"Quality Score: {result['overall_score']:.2f}")
```

### 3. Improve Content

**In Cursor Chat:**
```
Improve this content: add curiosity gaps and enhance emotional tone
```

**In Python:**
```python
improved = agent.improve(
    content=existing_content,
    improvement="add curiosity gaps and enhance emotional tone"
)

print(improved['content'])
print(f"Improvement: {improved['improvement_delta']}")
```

### 4. Edit Content

**Targeted Edit (Single Line/Section):**
```
Fix phrase repetition on line 194
```

**Comprehensive Edit (Category-Wide):**
```
Improve all CTAs in this chapter to be more engaging
```

**In Python:**
```python
# Targeted edit
edited = agent.edit(
    content=existing_content,
    edit_request="Fix phrase repetition on line 194",
    scope="targeted",
    context={"line_number": 194}
)

# Comprehensive edit
edited = agent.edit(
    content=existing_content,
    edit_request="Improve all CTAs to be more engaging",
    scope="comprehensive"
)
```

### 5. Quality Check

**In Cursor Chat:**
```
Quality check this chapter and suggest improvements
```

**In Python:**
```python
report = agent.quality_check(
    content=existing_content,
    dimensions=["sales_copy", "emotional", "conversion"]
)

print(f"Scores: {report['metrics']}")
print(f"Issues: {report['issues']}")
print(f"Suggestions: {report['intelligent_suggestions']}")
```

## Usage Patterns

### Pattern 1: Generate and Iterate

```python
# Generate initial content
result = agent.generate("Chapter about tax planning")

# Check quality
report = agent.quality_check(result['content'])

# Improve based on issues
if report['metrics']['sales_copy'] < 0.85:
    improved = agent.improve(
        result['content'],
        "improve sales copy quality: add curiosity gaps and future pacing"
    )
    result = improved
```

### Pattern 2: Incremental Edits

```python
# Start with existing content
content = existing_chapter_content

# Make targeted improvements
content = agent.edit(content, "fix phrase repetition on line 194")['content']
content = agent.edit(content, "add citation for statistic on line 87")['content']
content = agent.edit(content, "improve CTA at end of chapter")['content']

# Final quality check
final_report = agent.quality_check(content)
```

### Pattern 3: Category-Wide Improvements

```python
# Improve entire category
content = agent.edit(
    content,
    "improve all emotional elements throughout: add depth and connectedness",
    scope="comprehensive"
)['content']

# Improve all CTAs
content = agent.edit(
    content,
    "make all CTAs more engaging and conversion-optimized",
    scope="comprehensive"
)['content']
```

## Intelligent Features

### 1. Automatic Request Parsing

The system intelligently parses natural language requests:

```
"Generate chapter about retirement" 
→ Parses to: format_type="chapter", topic="retirement"

"Improve emotional tone"
→ Parses to: improvement_type="emotional", priority="P1"

"Fix phrase repetition on line 194"
→ Parses to: edit_type="fix", target="line 194", dimension="repetition"
```

### 2. Agentic Analysis

The system uses agentic chat to:
- Analyze issues intelligently
- Suggest specific improvements
- Generate edit instructions
- Test hypotheses

### 3. Quality-Driven Iteration

Content automatically improves through iterations:
- Initial generation
- Quality check identifies issues
- Agentic chat suggests improvements
- Content regenerated with improvements
- Re-checked until targets met

## Integration with Existing System

The Cursor integration works with existing systems:

```python
from services.cursor_wrapper import create_cursor_agent
from ai_prompts.prompt_builder import PromptBuilder
from meta_framework.content_quality.content_validator import ContentValidator

# Initialize
agent = create_cursor_agent(cursor_chat)

# Uses existing:
# - PromptBuilder for prompt generation
# - ContentValidator for quality checks
# - Lessons learned for guidance
# - All framework elements (narratives, personas, etc.)
```

## Future: MCP Server

The system is designed to be abstracted into an MCP server:

```python
from services.mcp_server_abstraction import MCPContentServer, ChatProvider

class MyChatProvider(ChatProvider):
    def chat(self, prompt: str) -> str:
        # Your chat implementation
        return response

server = MCPContentServer(MyChatProvider())

# Use with any MCP client
result = server.handle_request("generate", {
    "request": "Generate chapter",
    "context": {...}
})
```

## Best Practices

1. **Start with Quality Check**: Always check quality before making changes
2. **Iterate Incrementally**: Make small, targeted improvements
3. **Use Context**: Provide context (line numbers, selections) for better edits
4. **Check After Edits**: Re-validate after each edit
5. **Use Comprehensive Scope**: For category-wide improvements, use scope="comprehensive"

## Examples

### Example 1: Generate Chapter

```python
result = agent.generate(
    "Generate Chapter 3: Social Security claiming strategies for engineers approaching retirement",
    context={
        "format_type": "chapter",
        "persona": "engineer_retiree",
        "funnel_stage": "top_of_funnel",
        "length": "3000-4000 words",
        "chapter_num": 3
    }
)
```

### Example 2: Fix Specific Issue

```python
# Quality check finds issue
report = agent.quality_check(content)

# Issue: "Missing curiosity gaps"
# Fix it
improved = agent.improve(
    content,
    "add 2-3 strategic curiosity gaps in the opening section"
)
```

### Example 3: Comprehensive Improvement

```python
# Improve entire sales copy quality
improved = agent.edit(
    content,
    "improve sales copy quality throughout: add curiosity gaps, enhance emotional tone, improve future pacing, add actionable tidbits",
    scope="comprehensive"
)
```

