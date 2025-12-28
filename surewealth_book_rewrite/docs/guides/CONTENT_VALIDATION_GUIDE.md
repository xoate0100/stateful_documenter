# Content Validation Guide

## Overview

The content validation system provides **robust, context-aware validation** of generated content against framework constraints. It minimizes false positives and provides detailed reporting with idempotent run tracking.

---

## Features

### ✅ Robust Validation
- **Context-aware checking** - Not just simple regex
- **Word boundary matching** - Avoids false positives from partial matches
- **False positive filtering** - Ignores matches in code blocks, URLs, quotes
- **Multiple validation categories** - Banned words, AI phrases, length, tone, signature phrases

### ✅ Idempotent Runs
- **Unique run IDs** - Based on content hash + timestamp
- **Run tracking** - Saves validation results for reuse
- **No duplicate analysis** - Same content = same results (unless forced)

### ✅ Comprehensive Reporting
- **Detailed issues** - Location, context, suggestions
- **Categorized by severity** - Errors, warnings, info
- **JSON output** - Machine-readable reports
- **Human-readable** - Console-friendly format

---

## Usage

### Basic Validation

```bash
# Validate content from file
python scripts/content_validator.py \
  --content-file content/chapters/chapter_01.md \
  --format chapter

# Validate content from stdin/string
python scripts/content_validator.py \
  --content "Your content here..." \
  --format social_post \
  --format-subtype linkedin
```

### With Output

```bash
# Save JSON report
python scripts/content_validator.py \
  --content-file content/emails/email_001.md \
  --format email \
  --output validation_report.json
```

### Idempotent Runs

```bash
# Use specific run ID (for tracking)
python scripts/content_validator.py \
  --content-file content.md \
  --format chapter \
  --run-id my-validation-run-001

# Force revalidation (ignore cached results)
python scripts/content_validator.py \
  --content-file content.md \
  --format chapter \
  --force-revalidate
```

---

## Validation Categories

### 1. Banned Words (Error)
Checks for compliance/positioning banned words:
- `guaranteed_returns`
- `passive_income`
- `infinite_banking`
- `bank_on_yourself`
- `market_beating`
- `loophole`
- `guaranteed` (standalone)

**Features:**
- Word boundary matching (avoids partial matches)
- Case insensitive
- Context-aware (ignores code blocks, URLs)
- Provides location and context

### 2. AI Phrases (Warning)
Checks for AI-sounding phrases:
- "delve into"
- "harness the power of"
- "comprehensive guide"
- "in conclusion"
- "it's important to note"
- "unlock your potential"
- "revolutionizing the landscape"

**Features:**
- Flexible whitespace matching
- Case insensitive
- Context-aware filtering

### 3. Length Validation (Warning)
Checks content length against format requirements:

**Format Limits:**
- **Social Posts:**
  - LinkedIn: 125-3000 chars
  - Twitter: 50-280 chars
  - Facebook: 100-5000 chars
  - Instagram: 100-2200 chars
- **Emails:**
  - Nurture: 200-400 words
  - Conversion: 150-300 words
  - Follow-up: 100-200 words
- **Chapters:** 2000-5000 words
- **Blog Posts:** 500-2000 words

### 4. Signature Phrases (Info)
Checks if signature phrases are used:
- "You've worked too hard to risk it now."
- "This isn't about returns — it's about control."
- "Hope is not a strategy."
- etc.

**Note:** This is informational only - not an error if missing.

### 5. Tone Compliance (Info)
Checks for overly formal language:
- "furthermore", "moreover", "nevertheless"
- "thus", "hence", "therefore"
- "in conclusion", "to summarize"

**Note:** Suggests more conversational language.

---

## False Positive Prevention

The validator uses several techniques to minimize false positives:

1. **Word Boundary Matching**
   - Uses `\b` regex boundaries
   - Prevents partial word matches

2. **Context Filtering**
   - Ignores matches in code blocks (markdown backticks)
   - Ignores matches in URLs
   - Considers quote context

3. **Case Insensitive**
   - Handles variations in capitalization

4. **Flexible Whitespace**
   - Handles variations in spacing for phrases

---

## Run Tracking

### Run IDs
- **Auto-generated:** `{timestamp}-{content_hash}`
- **Custom:** Use `--run-id` for specific tracking
- **Stored:** `tracking/validation_runs/{run_id}.json`

### Run Data
Each run includes:
- Run ID and timestamp
- Content hash (for idempotency)
- Format type
- All issues found
- Summary statistics
- Status (passed/failed/warnings)

### Idempotency
- Same content = same hash = same results
- Use `--force-revalidate` to override
- Runs are cached for efficiency

---

## Integration with Prompt Builder

The prompt builder now includes **pre-generation validation**:

```bash
# Validation happens automatically
python ai_prompts/prompt_builder.py \
  --format chapter \
  --topic tax_planning \
  --narratives ALLEGORY_LEAKY_BUCKET \
  --characters JOHN_SMITH

# Skip validation if needed
python ai_prompts/prompt_builder.py \
  --format chapter \
  --topic tax_planning \
  --skip-validation
```

**Validates:**
- Format exists
- Persona exists
- Narrative IDs exist
- Character IDs exist
- Tool IDs exist

**Errors prevent prompt generation** - Fix issues before proceeding.

---

## Example Output

```
============================================================
Content Validation Report
============================================================
Run ID: 20240101120000-abc12345
Format: chapter
Status: WARNINGS
Timestamp: 2024-01-01T12:00:00

Summary:
  Total Issues: 3
  Errors: 0
  Warnings: 2
  Info: 1
  Word Count: 3245
  Char Count: 18234

============================================================
Issues Found:
============================================================

AI_PHRASE (1 issues):
  [WARNING] AI-sounding phrase found: 'delve into'
    Location: Line 45
    Context: ...we will delve into the mechanics of...
    Suggestion: Rephrase to sound more natural and human

LENGTH (1 issues):
  [WARNING] Content too long: 3245 words (maximum: 3000)
    Location: Overall
    Suggestion: Condense content to meet maximum length requirement

SIGNATURE_PHRASES (1 issues):
  [INFO] No signature phrases found
    Location: Overall
    Suggestion: Consider using signature phrases naturally in content

============================================================
```

---

## JSON Report Format

```json
{
  "run_id": "20240101120000-abc12345",
  "timestamp": "2024-01-01T12:00:00",
  "content_hash": "abc123...",
  "format_type": "chapter",
  "status": "warnings",
  "issues": [
    {
      "severity": "warning",
      "category": "ai_phrase",
      "message": "AI-sounding phrase found: 'delve into'",
      "location": "Line 45, position 1234",
      "context": "...we will delve into the mechanics...",
      "suggestion": "Rephrase to sound more natural and human"
    }
  ],
  "summary": {
    "total_issues": 3,
    "errors": 0,
    "warnings": 2,
    "info": 1,
    "word_count": 3245,
    "char_count": 18234
  }
}
```

---

## Best Practices

### 1. Validate After Generation
Always validate content after AI generation:

```bash
# Generate content
python ai_prompts/prompt_builder.py --format chapter --topic tax_planning > prompt.txt
# (Use prompt with AI to generate content)
# Save to content/chapters/chapter_01.md

# Validate generated content
python scripts/content_validator.py \
  --content-file content/chapters/chapter_01.md \
  --format chapter
```

### 2. Use Run IDs for Tracking
Track validation runs for specific content:

```bash
python scripts/content_validator.py \
  --content-file content.md \
  --format chapter \
  --run-id chapter-01-v2 \
  --output validation_reports/chapter-01-v2.json
```

### 3. Integrate into Workflow
Add validation to your content generation workflow:

```bash
#!/bin/bash
# generate_and_validate.sh

# Generate prompt
python ai_prompts/prompt_builder.py \
  --format chapter \
  --topic "$1" \
  --output prompts/chapter_prompt.txt

# (Generate content using prompt)

# Validate content
python scripts/content_validator.py \
  --content-file "content/chapters/$1.md" \
  --format chapter \
  --output "validation_reports/$1.json"

# Check exit code
if [ $? -eq 0 ]; then
  echo "✅ Validation passed"
else
  echo "❌ Validation failed - check report"
  exit 1
fi
```

### 4. Review Reports
- Check JSON reports for detailed analysis
- Use context to understand issues
- Apply suggestions to fix problems

---

## Troubleshooting

### False Positives
If you get false positives:
1. Check the context in the report
2. Verify it's not in a code block or URL
3. If legitimate, consider adding exception rules

### Missing Validations
If expected validations aren't running:
1. Check format type is correct
2. Verify format limits are defined
3. Check vocabulary file exists

### Run ID Conflicts
If run IDs conflict:
1. Use custom run IDs with `--run-id`
2. Use `--force-revalidate` to override cache
3. Check `tracking/validation_runs/` for existing runs

---

## Advanced Usage

### Batch Validation

```bash
# Validate all chapters
for file in content/chapters/*.md; do
  python scripts/content_validator.py \
    --content-file "$file" \
    --format chapter \
    --output "validation_reports/$(basename $file .md).json"
done
```

### CI/CD Integration

```yaml
# Example GitHub Actions
- name: Validate Content
  run: |
    python scripts/content_validator.py \
      --content-file content/chapters/chapter_01.md \
      --format chapter
```

---

*For questions or issues, see the main documentation or check validation run files in `tracking/validation_runs/`.*

