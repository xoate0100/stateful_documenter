#!/usr/bin/env python3
"""
Compliance Validator Script
Scans all documents in the project for compliance violations

Usage:
    python compliance_validator.py [--path PATH] [--fix] [--report REPORT_FILE]
"""

import argparse
import sys
from pathlib import Path
from typing import List, Dict, Any
import json
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from meta_framework.language.compliance_enforcer import ComplianceEnforcer, Violation


class ComplianceValidator:
    """Validates compliance across project files"""
    
    def __init__(self, project_root: Path):
        self.project_root = Path(project_root)
        self.enforcer = ComplianceEnforcer()
        self.results = []
    
    def find_content_files(self, extensions: List[str] = None) -> List[Path]:
        """Find all content files to validate"""
        if extensions is None:
            extensions = ['.md', '.txt', '.yaml', '.yml']
        
        files = []
        
        # Directories to scan
        scan_dirs = [
            self.project_root / "content",
            self.project_root / "docs",
            self.project_root / "transcripts",
            self.project_root / "meta_framework",
        ]
        
        # Exclude patterns
        exclude_patterns = [
            "**/node_modules/**",
            "**/.git/**",
            "**/__pycache__/**",
            "**/markdown_export/**",  # Exclude converted PDFs
            "**/compliance_rules.yaml",  # Exclude compliance rules file itself (contains examples)
        ]
        
        exclude_files = [
            "compliance_rules.yaml",  # Contains examples of non-compliant terms
        ]
        
        for scan_dir in scan_dirs:
            if not scan_dir.exists():
                continue
            
            for ext in extensions:
                for file_path in scan_dir.rglob(f"*{ext}"):
                    # Check if file should be excluded
                    should_exclude = False
                    for pattern in exclude_patterns:
                        if pattern.replace("**/", "").replace("/**", "") in str(file_path):
                            should_exclude = True
                            break
                    
                    # Check if file should be excluded
                    if should_exclude:
                        continue
                    
                    # Check if filename matches exclude list
                    if file_path.name in exclude_files:
                        continue
                    
                    files.append(file_path)
        
        return files
    
    def validate_file(self, file_path: Path) -> Dict[str, Any]:
        """Validate a single file"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            violations = self.enforcer.validate(content)
            summary = self.enforcer.get_compliance_summary(content)
            
            return {
                'file': str(file_path.relative_to(self.project_root)),
                'path': str(file_path),
                'violations': len(violations),
                'is_compliant': summary['is_compliant'],
                'violations_detail': [
                    {
                        'rule': v.rule_id,
                        'text': v.non_compliant_text,
                        'position': v.location,
                        'alternatives': v.suggested_alternatives,
                        'issue': v.issue
                    }
                    for v in violations
                ],
                'violations_by_rule': summary['violations_by_rule']
            }
        except Exception as e:
            return {
                'file': str(file_path.relative_to(self.project_root)),
                'path': str(file_path),
                'error': str(e),
                'violations': 0,
                'is_compliant': False
            }
    
    def validate_all(self, file_paths: List[Path] = None) -> Dict[str, Any]:
        """Validate all files"""
        if file_paths is None:
            file_paths = self.find_content_files()
        
        results = {
            'timestamp': datetime.now().isoformat(),
            'total_files': len(file_paths),
            'compliant_files': 0,
            'non_compliant_files': 0,
            'total_violations': 0,
            'files': []
        }
        
        print(f"Validating {len(file_paths)} files...")
        
        for file_path in file_paths:
            result = self.validate_file(file_path)
            results['files'].append(result)
            
            if result.get('is_compliant', False):
                results['compliant_files'] += 1
            else:
                results['non_compliant_files'] += 1
            
            results['total_violations'] += result.get('violations', 0)
            
            # Print progress
            status = "OK" if result.get('is_compliant') else "VIOLATIONS"
            violations = result.get('violations', 0)
            print(f"  [{status}] {result['file']} ({violations} violations)")
        
        return results
    
    def generate_report(self, results: Dict[str, Any], output_file: Path = None):
        """Generate compliance report"""
        report_lines = [
            "# Compliance Validation Report",
            f"Generated: {results['timestamp']}",
            "",
            "## Summary",
            f"- Total Files Scanned: {results['total_files']}",
            f"- Compliant Files: {results['compliant_files']}",
            f"- Non-Compliant Files: {results['non_compliant_files']}",
            f"- Total Violations: {results['total_violations']}",
            "",
            "## Non-Compliant Files",
            ""
        ]
        
        # Group by violation count
        non_compliant = [f for f in results['files'] if not f.get('is_compliant', True)]
        non_compliant.sort(key=lambda x: x.get('violations', 0), reverse=True)
        
        for file_result in non_compliant:
            violations = file_result.get('violations', 0)
            if violations == 0:
                continue
            
            report_lines.append(f"### {file_result['file']}")
            report_lines.append(f"**Violations: {violations}**")
            report_lines.append("")
            
            # Group violations by rule
            violations_by_rule = file_result.get('violations_by_rule', {})
            for rule, count in sorted(violations_by_rule.items(), key=lambda x: x[1], reverse=True):
                report_lines.append(f"- **{rule}**: {count} occurrence(s)")
            
            report_lines.append("")
            
            # Show first few violations
            violations_detail = file_result.get('violations_detail', [])[:5]
            if violations_detail:
                report_lines.append("Sample violations:")
                for v in violations_detail:
                    report_lines.append(f"  - Found: '{v['text']}'")
                    report_lines.append(f"    Use instead: {', '.join(v['alternatives'][:3])}")
                report_lines.append("")
        
        report_text = "\n".join(report_lines)
        
        if output_file:
            output_file.parent.mkdir(parents=True, exist_ok=True)
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(report_text)
            print(f"\nReport saved to: {output_file}")
        else:
            print("\n" + report_text)
        
        return report_text


def main():
    parser = argparse.ArgumentParser(description="Validate compliance across project")
    parser.add_argument("--path", default=".", help="Project root path")
    parser.add_argument("--report", help="Output report file path")
    parser.add_argument("--json", help="Output JSON report file path")
    parser.add_argument("--fix", action="store_true", help="Auto-fix violations (creates .fixed files)")
    
    args = parser.parse_args()
    
    project_root = Path(args.path).resolve()
    validator = ComplianceValidator(project_root)
    
    # Validate all files
    results = validator.validate_all()
    
    # Generate report
    report_file = Path(args.report) if args.report else None
    validator.generate_report(results, report_file)
    
    # Save JSON if requested
    if args.json:
        json_file = Path(args.json)
        json_file.parent.mkdir(parents=True, exist_ok=True)
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2)
        print(f"JSON report saved to: {json_file}")
    
    # Auto-fix if requested
    if args.fix:
        print("\nAuto-fixing violations...")
        fixed_count = 0
        for file_result in results['files']:
            if file_result.get('violations', 0) > 0:
                file_path = Path(file_result['path'])
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    enforced_content, violations = validator.enforcer.enforce(content, replace=True)
                    
                    if violations:
                        # Save to .fixed file
                        fixed_file = file_path.with_suffix(file_path.suffix + '.fixed')
                        with open(fixed_file, 'w', encoding='utf-8') as f:
                            f.write(enforced_content)
                        fixed_count += 1
                        print(f"  Fixed: {file_result['file']} -> {fixed_file.name}")
                except Exception as e:
                    print(f"  Error fixing {file_result['file']}: {e}")
        
        print(f"\nFixed {fixed_count} files")
    
    # Return exit code based on compliance
    return 0 if results['total_violations'] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

