#!/usr/bin/env python3
"""
Content Validator
Robust validation of generated content against framework constraints

Features:
- Context-aware checking (not just simple regex)
- Word boundary matching
- False positive minimization
- Idempotent validation runs with unique IDs
- Comprehensive reporting

Usage:
    python content_validator.py --content content/chapters/chapter_01.md --format chapter
    python content_validator.py --content content/emails/email_001.md --format email --run-id abc123
    python content_validator.py --content-file content.txt --format social_post --output report.json
"""

import yaml
import json
import re
import argparse
import hashlib
import uuid
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple, Set
from datetime import datetime
from dataclasses import dataclass, asdict
from collections import defaultdict


@dataclass
class ValidationIssue:
    """Represents a validation issue"""
    severity: str  # error, warning, info
    category: str  # banned_word, ai_phrase, length, tone, etc.
    message: str
    location: Optional[str] = None  # line number, section, etc.
    context: Optional[str] = None  # surrounding text
    suggestion: Optional[str] = None


@dataclass
class ValidationRun:
    """Represents a validation run"""
    run_id: str
    timestamp: str
    content_hash: str
    format_type: str
    issues: List[Dict[str, Any]]
    summary: Dict[str, Any]
    status: str  # passed, failed, warnings


class ContentValidator:
    """Robust content validator with context-aware checking"""
    
    def __init__(self, framework_dir: Path = Path("meta_framework")):
        self.framework_dir = Path(framework_dir)
        self.runs_dir = Path("tracking/validation_runs")
        self.runs_dir.mkdir(parents=True, exist_ok=True)
        
        # Load constraints
        self.banned_words = self._load_banned_words()
        self.banned_ai_phrases = self._load_banned_ai_phrases()
        self.signature_phrases = self._load_signature_phrases()
        self.format_limits = self._load_format_limits()
        
        # Compile regex patterns for efficiency
        self._compile_patterns()
    
    def _load_banned_words(self) -> List[str]:
        """Load banned words from vocabulary"""
        vocab_file = self.framework_dir / "language" / "vocabulary.yaml"
        if not vocab_file.exists():
            return []
        
        with open(vocab_file, 'r', encoding='utf-8') as f:
            vocab = yaml.safe_load(f)
            return vocab.get('banned_words', [])
    
    def _load_banned_ai_phrases(self) -> List[str]:
        """Load banned AI phrases"""
        vocab_file = self.framework_dir / "language" / "vocabulary.yaml"
        if not vocab_file.exists():
            return []
        
        with open(vocab_file, 'r', encoding='utf-8') as f:
            vocab = yaml.safe_load(f)
            return vocab.get('banned_ai_phrases', [])
    
    def _load_signature_phrases(self) -> List[str]:
        """Load signature phrases"""
        phrases_file = self.framework_dir / "language" / "signature_phrases.yaml"
        if not phrases_file.exists():
            return []
        
        with open(phrases_file, 'r', encoding='utf-8') as f:
            phrases = yaml.safe_load(f)
            return phrases.get('signature_phrases', [])
    
    def _load_format_limits(self) -> Dict[str, Dict[str, int]]:
        """Load format-specific length limits"""
        return {
            'social_post': {
                'linkedin': {'min': 125, 'max': 3000},
                'twitter': {'min': 50, 'max': 280},
                'facebook': {'min': 100, 'max': 5000},
                'instagram': {'min': 100, 'max': 2200}
            },
            'email': {
                'nurture': {'min': 200, 'max': 400},
                'conversion': {'min': 150, 'max': 300},
                'follow_up': {'min': 100, 'max': 200}
            },
            'chapter': {
                'min': 2000,
                'max': 5000
            },
            'blog': {
                'min': 500,
                'max': 2000
            }
        }
    
    def _compile_patterns(self):
        """Compile regex patterns for efficient matching"""
        # Word boundary patterns for banned words
        self.banned_word_patterns = {}
        for word in self.banned_words:
            # Handle underscores and hyphens
            word_clean = word.replace('_', '[-_ ]?')
            # Word boundary pattern - handles case insensitivity
            pattern = rf'\b{re.escape(word_clean)}\b'
            self.banned_word_patterns[word] = re.compile(pattern, re.IGNORECASE)
        
        # Phrase patterns (case insensitive, flexible whitespace)
        self.ai_phrase_patterns = {}
        for phrase in self.banned_ai_phrases:
            # Allow flexible whitespace
            phrase_pattern = r'\s+'.join(re.escape(word) for word in phrase.split())
            pattern = rf'\b{phrase_pattern}\b'
            self.ai_phrase_patterns[phrase] = re.compile(pattern, re.IGNORECASE)
    
    def _check_word_boundary(self, text: str, word: str, pattern: re.Pattern) -> List[Tuple[int, str]]:
        """Check for word with proper boundaries, returns (position, context)"""
        matches = []
        for match in pattern.finditer(text):
            start = match.start()
            end = match.end()
            
            # Get context (50 chars before and after)
            context_start = max(0, start - 50)
            context_end = min(len(text), end + 50)
            context = text[context_start:context_end]
            
            # Check if it's a false positive (e.g., in quotes, URLs, code blocks)
            if self._is_false_positive(text, start, end):
                continue
            
            matches.append((start, context))
        
        return matches
    
    def _is_false_positive(self, text: str, start: int, end: int) -> bool:
        """Check if match is likely a false positive"""
        # Check if in code block (markdown)
        before = text[:start]
        after = text[end:]
        
        # Count backticks before
        backticks_before = before.count('`')
        if backticks_before % 2 == 1:  # Inside code block
            return True
        
        # Check if in URL
        url_pattern = r'https?://[^\s]+'
        if re.search(url_pattern, text[max(0, start-20):end+20]):
            return True
        
        # Check if in quotes (might be acceptable in quotes)
        quote_before = before.rfind('"')
        quote_after = after.find('"')
        if quote_before != -1 and quote_after != -1:
            # Might be quoting someone else - less severe
            pass
        
        return False
    
    def _check_banned_words(self, content: str) -> List[ValidationIssue]:
        """Check for banned words with context awareness"""
        issues = []
        content_lower = content.lower()
        
        for word, pattern in self.banned_word_patterns.items():
            matches = self._check_word_boundary(content, word, pattern)
            
            for pos, context in matches:
                # Additional context check - is it part of a larger word?
                if pos > 0 and content[pos-1].isalnum():
                    continue
                if pos + len(word) < len(content) and content[pos + len(word)].isalnum():
                    continue
                
                # Get line number
                line_num = content[:pos].count('\n') + 1
                
                issues.append(ValidationIssue(
                    severity='error',
                    category='banned_word',
                    message=f"Banned word found: '{word}'",
                    location=f"Line {line_num}, position {pos}",
                    context=context.strip(),
                    suggestion=f"Replace with approved alternative or rephrase"
                ))
        
        return issues
    
    def _check_ai_phrases(self, content: str) -> List[ValidationIssue]:
        """Check for banned AI phrases"""
        issues = []
        
        for phrase, pattern in self.ai_phrase_patterns.items():
            matches = pattern.finditer(content)
            
            for match in matches:
                start = match.start()
                end = match.end()
                
                # Check false positive
                if self._is_false_positive(content, start, end):
                    continue
                
                # Get context
                context_start = max(0, start - 50)
                context_end = min(len(content), end + 50)
                context = content[context_start:context_end]
                
                line_num = content[:start].count('\n') + 1
                
                issues.append(ValidationIssue(
                    severity='warning',
                    category='ai_phrase',
                    message=f"AI-sounding phrase found: '{phrase}'",
                    location=f"Line {line_num}",
                    context=context.strip(),
                    suggestion="Rephrase to sound more natural and human"
                ))
        
        return issues
    
    def _check_length(self, content: str, format_type: str, format_subtype: Optional[str] = None) -> List[ValidationIssue]:
        """Check content length against format requirements"""
        issues = []
        
        # Count words (simple approximation)
        word_count = len(content.split())
        char_count = len(content)
        
        limits = self.format_limits.get(format_type, {})
        
        if format_type == 'social_post' and format_subtype:
            limits = limits.get(format_subtype, {})
        
        if not limits:
            return issues
        
        min_words = limits.get('min', 0)
        max_words = limits.get('max', float('inf'))
        
        # Convert character limits to approximate word limits (5 chars per word avg)
        if 'min' in limits and isinstance(limits['min'], int) and limits['min'] < 1000:
            # Likely character limit
            min_words = limits['min'] // 5
        if 'max' in limits and isinstance(limits['max'], int) and limits['max'] < 1000:
            max_words = limits['max'] // 5
        
        if word_count < min_words:
            issues.append(ValidationIssue(
                severity='warning',
                category='length',
                message=f"Content too short: {word_count} words (minimum: {min_words})",
                location="Overall",
                suggestion=f"Expand content to meet minimum length requirement"
            ))
        
        if word_count > max_words:
            issues.append(ValidationIssue(
                severity='warning',
                category='length',
                message=f"Content too long: {word_count} words (maximum: {max_words})",
                location="Overall",
                suggestion=f"Condense content to meet maximum length requirement"
            ))
        
        return issues
    
    def _check_signature_phrases(self, content: str) -> List[ValidationIssue]:
        """Check if signature phrases are used (info, not error)"""
        issues = []
        content_lower = content.lower()
        
        found_phrases = []
        for phrase in self.signature_phrases:
            if phrase.lower() in content_lower:
                found_phrases.append(phrase)
        
        if not found_phrases:
            issues.append(ValidationIssue(
                severity='info',
                category='signature_phrases',
                message="No signature phrases found",
                location="Overall",
                suggestion="Consider using signature phrases naturally in content"
            ))
        
        return issues
    
    def _check_tone_compliance(self, content: str) -> List[ValidationIssue]:
        """Check basic tone compliance"""
        issues = []
        
        # Check for overly formal language
        formal_indicators = [
            r'\b(?:furthermore|moreover|nevertheless|consequently)\b',
            r'\b(?:thus|hence|therefore)\b',
            r'\b(?:in conclusion|to summarize|in summary)\b'
        ]
        
        for pattern_str in formal_indicators:
            pattern = re.compile(pattern_str, re.IGNORECASE)
            if pattern.search(content):
                issues.append(ValidationIssue(
                    severity='info',
                    category='tone',
                    message="Formal language detected",
                    location="Overall",
                    suggestion="Consider using more conversational, plainspoken language"
                ))
                break
        
        return issues
    
    def _generate_run_id(self, content: str) -> str:
        """Generate unique run ID based on content hash"""
        content_hash = hashlib.md5(content.encode('utf-8')).hexdigest()[:8]
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        return f"{timestamp}-{content_hash}"
    
    def _get_content_hash(self, content: str) -> str:
        """Get content hash for idempotency"""
        return hashlib.sha256(content.encode('utf-8')).hexdigest()
    
    def _load_existing_run(self, run_id: str) -> Optional[ValidationRun]:
        """Load existing validation run"""
        run_file = self.runs_dir / f"{run_id}.json"
        if not run_file.exists():
            return None
        
        with open(run_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return ValidationRun(**data)
    
    def validate(self, 
                 content: str, 
                 format_type: str,
                 format_subtype: Optional[str] = None,
                 run_id: Optional[str] = None,
                 force_revalidate: bool = False) -> ValidationRun:
        """Validate content with idempotent run tracking"""
        
        content_hash = self._get_content_hash(content)
        
        # Generate or use provided run ID
        if not run_id:
            run_id = self._generate_run_id(content)
        
        # Check for existing run (idempotency)
        if not force_revalidate:
            existing_run = self._load_existing_run(run_id)
            if existing_run and existing_run.content_hash == content_hash:
                return existing_run
        
        # Perform validation
        all_issues = []
        
        # Check banned words
        all_issues.extend(self._check_banned_words(content))
        
        # Check AI phrases
        all_issues.extend(self._check_ai_phrases(content))
        
        # Check length
        all_issues.extend(self._check_length(content, format_type, format_subtype))
        
        # Check signature phrases
        all_issues.extend(self._check_signature_phrases(content))
        
        # Check tone
        all_issues.extend(self._check_tone_compliance(content))
        
        # Convert issues to dict for serialization
        issues_dict = [asdict(issue) for issue in all_issues]
        
        # Calculate summary
        error_count = sum(1 for issue in all_issues if issue.severity == 'error')
        warning_count = sum(1 for issue in all_issues if issue.severity == 'warning')
        info_count = sum(1 for issue in all_issues if issue.severity == 'info')
        
        # Determine status
        if error_count > 0:
            status = 'failed'
        elif warning_count > 0:
            status = 'warnings'
        else:
            status = 'passed'
        
        summary = {
            'total_issues': len(all_issues),
            'errors': error_count,
            'warnings': warning_count,
            'info': info_count,
            'word_count': len(content.split()),
            'char_count': len(content)
        }
        
        # Create validation run
        validation_run = ValidationRun(
            run_id=run_id,
            timestamp=datetime.now().isoformat(),
            content_hash=content_hash,
            format_type=format_type,
            issues=issues_dict,
            summary=summary,
            status=status
        )
        
        # Save run
        self._save_run(validation_run)
        
        return validation_run
    
    def _save_run(self, run: ValidationRun):
        """Save validation run to file"""
        run_file = self.runs_dir / f"{run.run_id}.json"
        with open(run_file, 'w', encoding='utf-8') as f:
            json.dump(asdict(run), f, indent=2, ensure_ascii=False)
    
    def print_report(self, run: ValidationRun):
        """Print human-readable validation report"""
        print(f"\n{'='*60}")
        print(f"Content Validation Report")
        print(f"{'='*60}")
        print(f"Run ID: {run.run_id}")
        print(f"Format: {run.format_type}")
        print(f"Status: {run.status.upper()}")
        print(f"Timestamp: {run.timestamp}")
        print(f"\nSummary:")
        print(f"  Total Issues: {run.summary['total_issues']}")
        print(f"  Errors: {run.summary['errors']}")
        print(f"  Warnings: {run.summary['warnings']}")
        print(f"  Info: {run.summary['info']}")
        print(f"  Word Count: {run.summary['word_count']}")
        print(f"  Char Count: {run.summary['char_count']}")
        
        if run.issues:
            print(f"\n{'='*60}")
            print(f"Issues Found:")
            print(f"{'='*60}")
            
            # Group by category
            by_category = defaultdict(list)
            for issue in run.issues:
                by_category[issue['category']].append(issue)
            
            for category, issues in by_category.items():
                print(f"\n{category.upper()} ({len(issues)} issues):")
                for issue in issues:
                    print(f"  [{issue['severity'].upper()}] {issue['message']}")
                    if issue.get('location'):
                        print(f"    Location: {issue['location']}")
                    if issue.get('context'):
                        print(f"    Context: ...{issue['context']}...")
                    if issue.get('suggestion'):
                        print(f"    Suggestion: {issue['suggestion']}")
                    print()
        else:
            print(f"\n✅ No issues found!")
        
        print(f"{'='*60}\n")


def main():
    parser = argparse.ArgumentParser(description="Validate content against framework constraints")
    parser.add_argument("--content", help="Content text to validate")
    parser.add_argument("--content-file", help="File containing content to validate")
    parser.add_argument("--format", required=True, help="Content format (social_post, email, chapter, blog)")
    parser.add_argument("--format-subtype", help="Format subtype (e.g., linkedin, twitter, nurture, conversion)")
    parser.add_argument("--run-id", help="Specific run ID (for idempotency)")
    parser.add_argument("--force-revalidate", action="store_true", help="Force revalidation even if run exists")
    parser.add_argument("--output", help="Output file for JSON report")
    parser.add_argument("--quiet", action="store_true", help="Suppress console output")
    
    args = parser.parse_args()
    
    # Load content
    if args.content_file:
        with open(args.content_file, 'r', encoding='utf-8') as f:
            content = f.read()
    elif args.content:
        content = args.content
    else:
        print("Error: Must provide --content or --content-file")
        return 1
    
    # Validate
    validator = ContentValidator()
    run = validator.validate(
        content=content,
        format_type=args.format,
        format_subtype=args.format_subtype,
        run_id=args.run_id,
        force_revalidate=args.force_revalidate
    )
    
    # Print report
    if not args.quiet:
        validator.print_report(run)
    
    # Save JSON output if requested
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(asdict(run), f, indent=2, ensure_ascii=False)
        if not args.quiet:
            print(f"Report saved to {args.output}")
    
    # Return exit code based on status
    return 0 if run.status == 'passed' else 1


if __name__ == "__main__":
    exit(main())

