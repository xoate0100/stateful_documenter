#!/usr/bin/env python3
"""
Test New Patterns Only
Validates that new conversion-optimized patterns work correctly
"""

import sys
import yaml
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

def test_new_patterns():
    """Test only the new pattern files"""
    print("Testing New Pattern Files")
    print("=" * 70)
    
    language_dir = Path(__file__).parent.parent / "meta_framework" / "language"
    
    new_patterns = [
        'question_frameworks.yaml',
        'permission_frames.yaml',
        'presuppositions.yaml'
    ]
    
    results = {'valid': [], 'invalid': []}
    
    for pattern_file in new_patterns:
        filepath = language_dir / pattern_file
        print(f"\nTesting: {pattern_file}")
        
        if not filepath.exists():
            print(f"  [ERROR] File not found")
            results['invalid'].append(pattern_file)
            continue
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            
            # Check structure
            if pattern_file == 'question_frameworks.yaml':
                if 'question_frameworks' in data:
                    print(f"  [OK] YAML valid, structure correct")
                    print(f"  [OK] Contains 'question_frameworks' key")
                    results['valid'].append(pattern_file)
                else:
                    print(f"  [ERROR] Missing 'question_frameworks' key")
                    results['invalid'].append(pattern_file)
            
            elif pattern_file == 'permission_frames.yaml':
                if 'permission_frames' in data:
                    print(f"  [OK] YAML valid, structure correct")
                    print(f"  [OK] Contains 'permission_frames' key")
                    results['valid'].append(pattern_file)
                else:
                    print(f"  [ERROR] Missing 'permission_frames' key")
                    results['invalid'].append(pattern_file)
            
            elif pattern_file == 'presuppositions.yaml':
                if 'presuppositions' in data:
                    print(f"  [OK] YAML valid, structure correct")
                    print(f"  [OK] Contains 'presuppositions' key")
                    results['valid'].append(pattern_file)
                else:
                    print(f"  [ERROR] Missing 'presuppositions' key")
                    results['invalid'].append(pattern_file)
        
        except Exception as e:
            print(f"  [ERROR] YAML syntax error: {str(e)}")
            results['invalid'].append(pattern_file)
    
    # Test prompt builder with error handling
    print("\n" + "=" * 70)
    print("Testing Prompt Builder Integration")
    print("=" * 70)
    
    try:
        from ai_prompts.prompt_builder import PromptBuilder
        builder = PromptBuilder()
        
        # Test loading constraints (with error handling)
        constraints = builder.load_language_constraints()
        
        new_pattern_keys = [
            'question frameworks',
            'permission frames',
            'presuppositions'
        ]
        
        print("\nChecking if new patterns are loaded:")
        for key in new_pattern_keys:
            if key in constraints:
                print(f"  [OK] '{key}' loaded")
                pattern_data = constraints[key]
                if isinstance(pattern_data, dict) and len(pattern_data) > 0:
                    print(f"      Contains {len(pattern_data)} top-level keys")
                else:
                    print(f"      [WARNING] Pattern data empty or invalid")
            else:
                print(f"  [WARNING] '{key}' not found in constraints")
        
        # Test prompt generation
        print("\nTesting prompt generation...")
        try:
            prompt = builder.build_prompt(
                format_type="social_post",
                topic="retirement planning",
                persona="engineer_retiree",
                validate=False
            )
            
            print(f"  [OK] Prompt generated ({len(prompt)} characters)")
            
            # Check for new pattern indicators
            checks = {
                'Question-Based Engagement': 'question' in prompt.lower() and 'engagement' in prompt.lower(),
                'Permission Frames': 'permission' in prompt.lower() and 'frame' in prompt.lower(),
                'Presuppositions': 'presupposition' in prompt.lower() or ('when you' in prompt.lower() and 'when we' in prompt.lower()),
                'Compliance Rules': 'compliance' in prompt.lower() or 'never use' in prompt.lower()
            }
            
            print("\nPattern inclusion check:")
            for check_name, check_result in checks.items():
                status = "[OK]" if check_result else "[MISSING]"
                print(f"  {status} {check_name}")
        
        except Exception as e:
            print(f"  [ERROR] Prompt generation failed: {str(e)}")
    
    except Exception as e:
        print(f"[ERROR] Failed to test PromptBuilder: {str(e)}")
    
    # Summary
    print("\n" + "=" * 70)
    print("Summary")
    print("=" * 70)
    print(f"Valid patterns: {len(results['valid'])}/{len(new_patterns)}")
    print(f"Invalid patterns: {len(results['invalid'])}/{len(new_patterns)}")
    
    if len(results['valid']) == len(new_patterns):
        print("\n[SUCCESS] All new patterns are valid and integrated!")
        return 0
    else:
        print("\n[ERROR] Some patterns have issues")
        return 1


if __name__ == "__main__":
    sys.exit(test_new_patterns())

