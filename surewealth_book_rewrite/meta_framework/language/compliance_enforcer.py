#!/usr/bin/env python3
"""
Compliance Enforcement Module
Validates and enforces word/phrase compliance rules across all content

Usage:
    from compliance_enforcer import ComplianceEnforcer
    enforcer = ComplianceEnforcer()
    validated_text = enforcer.enforce(text)
    violations = enforcer.validate(text)
"""

import re
import yaml
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass


@dataclass
class Violation:
    """Represents a compliance violation"""
    rule_id: str
    non_compliant_text: str
    location: Tuple[int, int]  # (start, end) character positions
    issue: str
    suggested_alternatives: List[str]
    severity: str  # "error" | "warning"


class ComplianceEnforcer:
    """Enforces compliance rules on content"""
    
    def __init__(self, rules_file: Optional[Path] = None):
        """
        Initialize compliance enforcer
        
        Args:
            rules_file: Path to compliance_rules.yaml. If None, uses default location.
        """
        if rules_file is None:
            rules_file = Path(__file__).parent / "compliance_rules.yaml"
        
        self.rules_file = Path(rules_file)
        self.rules = self._load_rules()
        self._build_pattern_cache()
    
    def _load_rules(self) -> Dict[str, Any]:
        """Load compliance rules from YAML"""
        if not self.rules_file.exists():
            raise FileNotFoundError(f"Compliance rules file not found: {self.rules_file}")
        
        with open(self.rules_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        return data
    
    def _build_pattern_cache(self):
        """Build regex patterns for efficient matching"""
        self.patterns = []
        
        for idx, rule in enumerate(self.rules.get('rules', [])):
            non_compliant = rule.get('non_compliant', '')
            variants = rule.get('variants', [non_compliant])
            match_type = rule.get('match_type', 'word_boundary')
            case_sensitive = rule.get('case_sensitive', False)
            
            # Build pattern for all variants
            pattern_parts = []
            for variant in variants:
                if match_type == 'word_boundary':
                    # Match whole words only
                    escaped = re.escape(variant)
                    pattern_parts.append(rf'\b{escaped}\b')
                elif match_type == 'phrase':
                    # Match as phrase (allowing word boundaries around it)
                    escaped = re.escape(variant)
                    pattern_parts.append(rf'\b{escaped}\b')
                else:  # partial or exact
                    escaped = re.escape(variant)
                    pattern_parts.append(escaped)
            
            # Combine all variants with OR
            pattern = '|'.join(pattern_parts)
            
            flags = 0 if case_sensitive else re.IGNORECASE
            
            self.patterns.append({
                'rule_index': idx,
                'pattern': re.compile(pattern, flags),
                'rule': rule,
                'match_type': match_type
            })
    
    def validate(self, text: str) -> List[Violation]:
        """
        Validate text and return list of violations
        
        Args:
            text: Text to validate
            
        Returns:
            List of Violation objects
        """
        violations = []
        
        for pattern_info in self.patterns:
            pattern = pattern_info['pattern']
            rule = pattern_info['rule']
            
            # Find all matches
            for match in pattern.finditer(text):
                start, end = match.span()
                matched_text = match.group()
                
                # Check for exceptions
                if self._check_exceptions(rule, text, start, end):
                    continue
                
                # Check context requirements
                if rule.get('context_required'):
                    if not self._check_context(rule, text, start, end):
                        continue
                
                violation = Violation(
                    rule_id=rule.get('non_compliant', ''),
                    non_compliant_text=matched_text,
                    location=(start, end),
                    issue=rule.get('issue', ''),
                    suggested_alternatives=rule.get('alternatives', []),
                    severity='error'  # All compliance violations are errors
                )
                violations.append(violation)
        
        return violations
    
    def _check_exceptions(self, rule: Dict, text: str, start: int, end: int) -> bool:
        """Check if match falls under an exception"""
        exceptions = rule.get('exceptions', [])
        if not exceptions:
            return False
        
        # Get context around match
        context_start = max(0, start - 100)
        context_end = min(len(text), end + 100)
        context = text[context_start:context_end].lower()
        
        for exception in exceptions:
            exception_context = exception.get('context', '').lower()
            if exception_context in context and exception.get('allowed', False):
                return True
        
        return False
    
    def _check_context(self, rule: Dict, text: str, start: int, end: int) -> bool:
        """Check if context requirement is met"""
        # Get context around match
        context_start = max(0, start - 100)
        context_end = min(len(text), end + 100)
        context = text[context_start:context_end].lower()
        
        # For now, assume context is met if we can't determine otherwise
        # This is a simplified check - can be enhanced
        return True
    
    def enforce(self, text: str, replace: bool = True) -> Tuple[str, List[Violation]]:
        """
        Enforce compliance rules on text
        
        Args:
            text: Text to enforce rules on
            replace: If True, automatically replace violations. If False, only validate.
            
        Returns:
            Tuple of (enforced_text, violations_found)
        """
        violations = self.validate(text)
        
        if not replace or not violations:
            return text, violations
        
        # Sort violations by position (reverse order for safe replacement)
        violations_sorted = sorted(violations, key=lambda v: v.location[0], reverse=True)
        
        enforced_text = text
        replacements_made = []
        
        for violation in violations_sorted:
            start, end = violation.location
            matched_text = enforced_text[start:end]
            
            # Get first alternative (or use original if no alternatives)
            if violation.suggested_alternatives:
                replacement = violation.suggested_alternatives[0]
                
                # Replace in text
                enforced_text = enforced_text[:start] + replacement + enforced_text[end:]
                replacements_made.append({
                    'original': matched_text,
                    'replacement': replacement,
                    'rule': violation.rule_id
                })
        
        return enforced_text, violations
    
    def get_compliance_summary(self, text: str) -> Dict[str, Any]:
        """
        Get summary of compliance status
        
        Returns:
            Dictionary with compliance statistics
        """
        violations = self.validate(text)
        
        return {
            'total_violations': len(violations),
            'is_compliant': len(violations) == 0,
            'violations_by_rule': self._group_violations_by_rule(violations),
            'violations': [
                {
                    'rule': v.rule_id,
                    'text': v.non_compliant_text,
                    'position': v.location,
                    'alternatives': v.suggested_alternatives
                }
                for v in violations
            ]
        }
    
    def _group_violations_by_rule(self, violations: List[Violation]) -> Dict[str, int]:
        """Group violations by rule ID"""
        grouped = {}
        for violation in violations:
            rule_id = violation.rule_id
            grouped[rule_id] = grouped.get(rule_id, 0) + 1
        return grouped
    
    def get_compliance_prompt_instructions(self) -> str:
        """
        Get prompt instructions for AI content generation
        
        Returns:
            String with compliance instructions for AI prompts
        """
        instructions = [
            "COMPLIANCE REQUIREMENTS - CRITICAL:",
            "",
            "You MUST follow these word/phrase substitution rules. These are regulatory requirements:",
            ""
        ]
        
        # Add key rules (limit to most important for prompt)
        important_rules = [
            r for r in self.rules.get('rules', [])
            if r.get('non_compliant') in [
                'Invest', 'Investments', 'Account', 'Deposit', 'Free',
                'Best', 'Always', 'Expert', 'Financial Planner', 'Gain',
                'Growth', 'Risk free', 'Guaranteed returns', 'Savings'
            ]
        ]
        
        for rule in important_rules[:15]:  # Limit to 15 most important
            non_compliant = rule.get('non_compliant', '')
            alternatives = rule.get('alternatives', [])
            issue = rule.get('issue', '')[:100]  # Truncate issue
            
            instructions.append(f"NEVER use: '{non_compliant}'")
            instructions.append(f"  Reason: {issue}")
            instructions.append(f"  Use instead: {', '.join(alternatives[:3])}")
            instructions.append("")
        
        instructions.append("For complete rules, reference compliance_rules.yaml")
        instructions.append("")
        instructions.append("Before finalizing content, validate all text against compliance rules.")
        
        return "\n".join(instructions)


def main():
    """CLI for testing compliance enforcement"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Compliance enforcement tool")
    parser.add_argument("--text", help="Text to validate")
    parser.add_argument("--file", help="File to validate")
    parser.add_argument("--enforce", action="store_true", help="Auto-replace violations")
    parser.add_argument("--rules", help="Path to compliance rules YAML")
    
    args = parser.parse_args()
    
    enforcer = ComplianceEnforcer(rules_file=Path(args.rules) if args.rules else None)
    
    if args.file:
        with open(args.file, 'r', encoding='utf-8') as f:
            text = f.read()
    elif args.text:
        text = args.text
    else:
        print("Error: Must provide --text or --file")
        return 1
    
    if args.enforce:
        enforced_text, violations = enforcer.enforce(text, replace=True)
        print("ENFORCED TEXT:")
        print(enforced_text)
        print(f"\nFound {len(violations)} violations (auto-replaced)")
    else:
        violations = enforcer.validate(text)
        summary = enforcer.get_compliance_summary(text)
        
        print(f"Compliance Status: {'COMPLIANT' if summary['is_compliant'] else 'NON-COMPLIANT'}")
        print(f"Total Violations: {summary['total_violations']}")
        
        if violations:
            print("\nViolations:")
            for v in violations:
                print(f"  - '{v.non_compliant_text}' at position {v.location}")
                print(f"    Rule: {v.rule_id}")
                print(f"    Alternatives: {', '.join(v.suggested_alternatives[:3])}")
                print()
    
    return 0 if summary['is_compliant'] else 1


if __name__ == "__main__":
    import sys
    sys.exit(main())

