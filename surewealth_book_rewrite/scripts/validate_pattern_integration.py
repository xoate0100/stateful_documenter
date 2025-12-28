#!/usr/bin/env python3
"""
Pattern Integration Validation Script
Verifies all patterns are properly integrated and cross-referenced

Usage:
    python scripts/validate_pattern_integration.py
"""

import sys
import yaml
from pathlib import Path
from typing import Dict, List, Set, Any
from collections import defaultdict

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from ai_prompts.prompt_builder import PromptBuilder


class PatternValidator:
    """Validates pattern integration and cross-referencing"""
    
    def __init__(self, project_root: Path = None):
        if project_root is None:
            project_root = Path(__file__).parent.parent
        self.project_root = Path(project_root)
        self.framework_dir = self.project_root / "meta_framework"
        self.language_dir = self.framework_dir / "language"
        self.errors = []
        self.warnings = []
        self.info = []
        
    def validate_file_exists(self, filepath: Path, description: str) -> bool:
        """Check if file exists"""
        if not filepath.exists():
            self.errors.append(f"Missing {description}: {filepath}")
            return False
        return True
    
    def validate_yaml_structure(self, filepath: Path, required_keys: List[str] = None) -> Dict[str, Any]:
        """Validate YAML file structure"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            
            if required_keys:
                for key in required_keys:
                    if key not in data:
                        self.warnings.append(f"Missing key '{key}' in {filepath.name}")
            
            return data
        except Exception as e:
            self.errors.append(f"Error loading {filepath.name}: {str(e)}")
            return {}
    
    def validate_cross_references(self, pattern_file: Path, data: Dict[str, Any]) -> List[str]:
        """Validate cross-references in pattern file"""
        missing_refs = []
        
        if 'cross_references' in data:
            refs = data['cross_references']
            if isinstance(refs, list):
                for ref in refs:
                    # Convert relative path to absolute
                    if ref.startswith('meta_framework/'):
                        ref_path = self.project_root / ref
                    else:
                        ref_path = self.language_dir / ref
                    
                    if not ref_path.exists():
                        missing_refs.append(f"  - {ref} (referenced in {pattern_file.name})")
        
        return missing_refs
    
    def validate_prompt_builder_integration(self) -> Dict[str, Any]:
        """Validate that PromptBuilder loads all patterns"""
        results = {
            'loaded_patterns': [],
            'missing_patterns': [],
            'integration_issues': []
        }
        
        try:
            builder = PromptBuilder()
            constraints = builder.load_language_constraints()
            
            # Expected patterns
            expected_patterns = [
                'normalization patterns',
                'reframing patterns',
                'mathematical proof patterns',
                'empowerment patterns',
                'future visioning patterns',
                'celebration patterns',
                'confirmation patterns',
                'friction resolution',
                'emotional transitions',
                'psychological principles',
                'question frameworks',  # New
                'permission frames',  # New
                'presuppositions'  # New
            ]
            
            for pattern in expected_patterns:
                if pattern in constraints:
                    results['loaded_patterns'].append(pattern)
                else:
                    results['missing_patterns'].append(pattern)
            
            # Check if new patterns have content
            new_patterns = ['question frameworks', 'permission frames', 'presuppositions']
            for pattern in new_patterns:
                if pattern in constraints:
                    pattern_data = constraints[pattern]
                    if not pattern_data or not isinstance(pattern_data, dict):
                        results['integration_issues'].append(f"{pattern} loaded but empty or invalid")
                    elif pattern == 'question frameworks':
                        if 'question_frameworks' not in pattern_data:
                            results['integration_issues'].append(f"{pattern} missing 'question_frameworks' key")
                    elif pattern == 'permission frames':
                        if 'permission_frames' not in pattern_data:
                            results['integration_issues'].append(f"{pattern} missing 'permission_frames' key")
                    elif pattern == 'presuppositions':
                        if 'presuppositions' not in pattern_data:
                            results['integration_issues'].append(f"{pattern} missing 'presuppositions' key")
            
            return results
            
        except Exception as e:
            self.errors.append(f"Error testing PromptBuilder: {str(e)}")
            return results
    
    def validate_cta_integration(self) -> Dict[str, Any]:
        """Validate CTA library integration"""
        results = {
            'cta_file_exists': False,
            'question_based_ctas': False,
            'performance_data': False
        }
        
        cta_file = self.framework_dir / "tools_ctas" / "cta_library.yaml"
        if cta_file.exists():
            results['cta_file_exists'] = True
            data = self.validate_yaml_structure(cta_file)
            
            if 'ctas' in data:
                ctas = data['ctas']
                if 'question_based_ctas' in ctas:
                    results['question_based_ctas'] = True
                
                if 'performance_data' in data:
                    results['performance_data'] = True
        
        return results
    
    def validate_prompt_output(self) -> Dict[str, Any]:
        """Test actual prompt generation"""
        results = {
            'prompt_generated': False,
            'includes_question_frameworks': False,
            'includes_permission_frames': False,
            'includes_presuppositions': False,
            'includes_compliance': False,
            'prompt_length': 0
        }
        
        try:
            builder = PromptBuilder()
            prompt = builder.build_prompt(
                format_type="social_post",
                topic="retirement planning",
                persona="engineer_retiree",
                validate=False  # Skip validation for test
            )
            
            results['prompt_generated'] = True
            results['prompt_length'] = len(prompt)
            
            # Check for key pattern indicators
            if 'question' in prompt.lower() and 'framework' in prompt.lower():
                results['includes_question_frameworks'] = True
            
            if 'permission' in prompt.lower() and 'frame' in prompt.lower():
                results['includes_permission_frames'] = True
            
            if 'presupposition' in prompt.lower() or 'when you' in prompt.lower():
                results['includes_presuppositions'] = True
            
            if 'compliance' in prompt.lower() or 'never use' in prompt.lower():
                results['includes_compliance'] = True
            
            return results, prompt
            
        except Exception as e:
            self.errors.append(f"Error generating test prompt: {str(e)}")
            return results, None
    
    def validate_all_patterns(self) -> Dict[str, Any]:
        """Validate all pattern files"""
        results = {
            'files_checked': 0,
            'files_valid': 0,
            'missing_cross_refs': [],
            'invalid_yaml': []
        }
        
        pattern_files = [
            'question_frameworks.yaml',
            'permission_frames.yaml',
            'presuppositions.yaml',
            'reframing_patterns.yaml',
            'emotional_transitions.yaml',
            'normalization_patterns.yaml',
            'mathematical_proof_patterns.yaml',
            'empowerment_patterns.yaml',
            'future_visioning_patterns.yaml',
            'celebration_patterns.yaml',
            'confirmation_patterns.yaml',
            'friction_resolution.yaml',
            'psychological_principles.yaml'
        ]
        
        for pattern_file in pattern_files:
            filepath = self.language_dir / pattern_file
            results['files_checked'] += 1
            
            if filepath.exists():
                try:
                    data = self.validate_yaml_structure(filepath)
                    if data:
                        results['files_valid'] += 1
                        
                        # Check cross-references
                        missing_refs = self.validate_cross_references(filepath, data)
                        if missing_refs:
                            results['missing_cross_refs'].extend(missing_refs)
                except Exception as e:
                    results['invalid_yaml'].append(f"{pattern_file}: {str(e)}")
            else:
                self.warnings.append(f"Pattern file not found: {pattern_file}")
        
        return results
    
    def run_full_validation(self) -> Dict[str, Any]:
        """Run complete validation"""
        print("=" * 70)
        print("Pattern Integration Validation")
        print("=" * 70)
        print()
        
        results = {
            'file_validation': {},
            'prompt_builder': {},
            'cta_integration': {},
            'prompt_output': {},
            'pattern_files': {}
        }
        
        # 1. Validate pattern files exist and are valid
        print("1. Validating pattern files...")
        results['pattern_files'] = self.validate_all_patterns()
        print(f"   [OK] Checked {results['pattern_files']['files_checked']} files")
        print(f"   [OK] {results['pattern_files']['files_valid']} files valid")
        
        # 2. Validate PromptBuilder integration
        print("\n2. Validating PromptBuilder integration...")
        results['prompt_builder'] = self.validate_prompt_builder_integration()
        print(f"   [OK] Loaded {len(results['prompt_builder']['loaded_patterns'])} patterns")
        if results['prompt_builder']['missing_patterns']:
            print(f"   ⚠ Missing {len(results['prompt_builder']['missing_patterns'])} patterns")
        
        # 3. Validate CTA integration
        print("\n3. Validating CTA library integration...")
        results['cta_integration'] = self.validate_cta_integration()
        if results['cta_integration']['cta_file_exists']:
            print("   [OK] CTA library exists")
        if results['cta_integration']['question_based_ctas']:
            print("   [OK] Question-based CTAs found")
        
        # 4. Test actual prompt generation
        print("\n4. Testing prompt generation...")
        prompt_results, test_prompt = self.validate_prompt_output()
        results['prompt_output'] = prompt_results
        if prompt_results['prompt_generated']:
            print(f"   [OK] Prompt generated ({prompt_results['prompt_length']} chars)")
            if prompt_results['includes_question_frameworks']:
                print("   [OK] Question frameworks included")
            if prompt_results['includes_permission_frames']:
                print("   [OK] Permission frames included")
            if prompt_results['includes_presuppositions']:
                print("   [OK] Presuppositions included")
            if prompt_results['includes_compliance']:
                print("   [OK] Compliance rules included")
        
        # Print summary
        print("\n" + "=" * 70)
        print("Validation Summary")
        print("=" * 70)
        
        if self.errors:
            print(f"\n[ERROR] ERRORS ({len(self.errors)}):")
            for error in self.errors:
                print(f"   - {error}")
        
        if self.warnings:
            print(f"\n[WARNING] WARNINGS ({len(self.warnings)}):")
            for warning in self.warnings:
                print(f"   - {warning}")
        
        if results['pattern_files']['missing_cross_refs']:
            print(f"\n[WARNING] Missing Cross-References ({len(results['pattern_files']['missing_cross_refs'])}):")
            for ref in results['pattern_files']['missing_cross_refs'][:5]:  # Show first 5
                print(f"   {ref}")
            if len(results['pattern_files']['missing_cross_refs']) > 5:
                print(f"   ... and {len(results['pattern_files']['missing_cross_refs']) - 5} more")
        
        if not self.errors and not self.warnings:
            print("\n[SUCCESS] All validations passed!")
        
        # Return test prompt for inspection
        if test_prompt:
            results['test_prompt'] = test_prompt[:500] + "..." if len(test_prompt) > 500 else test_prompt
        
        return results


def main():
    validator = PatternValidator()
    results = validator.run_full_validation()
    
    # Exit with error code if issues found
    if validator.errors:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

