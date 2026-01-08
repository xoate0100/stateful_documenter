# Quick Start: Using in Cursor IDE

## Setup

In Cursor IDE, you can use this system directly in the chat interface or in Python files.

### Option 1: Direct Chat Usage

Simply ask Cursor chat to use the content generation system:

```
Use the content generation system to create a chapter about retirement planning for engineers
```

### Option 2: Python Integration

```python
# In a Python file or Cursor chat
from services.cursor_wrapper import create_cursor_agent

# Initialize (cursor_chat is Cursor's chat function)
agent = create_cursor_agent(cursor_chat)

# Generate content
result = agent.generate("Generate Chapter 3: Social Security strategies")
```

## Common Use Cases

### 1. Generate New Content

**Cursor Chat:**
```
Generate a chapter about tax planning strategies for engineers approaching retirement, 3000-4000 words, top of funnel
```

### 2. Improve Existing Content

**Cursor Chat:**
```
Improve this content: add curiosity gaps and enhance emotional tone
```

### 3. Fix Specific Issues

**Cursor Chat:**
```
Fix phrase repetition on line 194
```

### 4. Quality Check

**Cursor Chat:**
```
Quality check this chapter and suggest improvements
```

### 5. Comprehensive Edit

**Cursor Chat:**
```
Improve all CTAs in this chapter to be more engaging
```

## How It Works

1. **Intelligent Parsing**: Your request is parsed into structured format
2. **Agentic Analysis**: System analyzes what's needed
3. **Prompt Refinement**: Generates intelligent prompts (not hardcoded)
4. **Content Generation**: Creates/improves content
5. **Quality Validation**: Checks quality and iterates if needed
6. **Returns Result**: Content + metrics + suggestions

## Example Workflow

```
You: "Generate chapter about retirement planning"

System:
1. Parses request → topic, format, persona, etc.
2. Generates initial prompt
3. Creates content (3000 words)
4. Quality check → Scores: structural: 0.92, sales_copy: 0.65, ...
5. Identifies issues → "Missing curiosity gaps"
6. Agentic chat analyzes → "Add 2-3 strategic questions"
7. Refines prompt → Adds curiosity gap instructions
8. Regenerates improved content
9. Re-checks → Scores improved
10. Returns final content + metrics
```

## Key Features

✅ **Intelligent, Not Hardcoded**: Uses agentic chat for analysis  
✅ **On-the-Fly Edits**: Single line or category-wide  
✅ **Quality-Driven**: Iterates until targets met  
✅ **Human-Centered**: Preserves emotional elements  
✅ **Future-Proof**: Ready for MCP server

