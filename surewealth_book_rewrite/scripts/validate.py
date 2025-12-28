#!/usr/bin/env python3
"""
Validation Script
Validates framework files against templates and checks for consistency

Usage:
    python validate.py --framework-dir meta_framework/
"""

import yaml
import argparse
from pathlib import Path
from typing import Dict, List, Any


class FrameworkValidator:
    """Validates meta framework files"""
    
    def __init__(self, framework_dir: Path):
        self.framework_dir = Path(framework_dir)
        self.errors = []
        self.warnings = []
        
    def validate_character(self, char_file: Path) -> List[str]:
        """Validate a character profile"""
        errors = []
        try:
            with open(char_file, 'r', encoding='utf-8') as f:
                char_data = yaml.safe_load(f)
            
            char = char_data.get('character', {})
            
            # Required fields
            required = ['id', 'name', 'type', 'first_appearance']
            for field in required:
                if not char.get(field):
                    errors.append(f"{char_file}: Missing required field 'character.{field}'")
            
            # Validate ID format
            if char.get('id') and not char['id'].isupper():
                errors.append(f"{char_file}: Character ID should be UPPERCASE")
                
        except Exception as e:
            errors.append(f"{char_file}: Error reading file - {e}")
            
        return errors
    
    def validate_narrative(self, narrative_file: Path) -> List[str]:
        """Validate a narrative element (story_vault_entry)"""
        errors = []
        try:
            # Skip schema file
            if narrative_file.name == "story_vault_schema.yaml":
                return errors
                
            with open(narrative_file, 'r', encoding='utf-8') as f:
                narrative_data = yaml.safe_load(f)
            
            # Support both old 'narrative' and new 'story_vault_entry' formats
            narrative = narrative_data.get('story_vault_entry') or narrative_data.get('narrative', {})
            
            if not narrative:
                errors.append(f"{narrative_file}: Missing 'story_vault_entry' or 'narrative' key")
                return errors
            
            # Required fields
            required = ['id', 'type', 'title']
            for field in required:
                if not narrative.get(field):
                    errors.append(f"{narrative_file}: Missing required field '{field}'")
            
            # Validate type
            valid_types = ['allegory', 'composite_case_study', 'foil_story', 'legacy_parable', 
                          'metaphor', 'case_study', 'story_thread']  # Support both old and new
            if narrative.get('type') not in valid_types:
                errors.append(f"{narrative_file}: Invalid narrative type '{narrative.get('type')}'")
            
            # Validate ID format
            if narrative.get('id') and not narrative['id'].isupper():
                errors.append(f"{narrative_file}: Narrative ID should be UPPERCASE")
                
        except Exception as e:
            errors.append(f"{narrative_file}: Error reading file - {e}")
            
        return errors
    
    def validate_indexes(self) -> List[str]:
        """Validate that all indexed files exist"""
        errors = []
        # TODO: Implement index validation
        return errors
    
    def validate_all(self) -> Dict[str, List[str]]:
        """Validate entire framework"""
        all_errors = []
        all_warnings = []
        
        # Validate characters
        chars_dir = self.framework_dir / "characters"
        if chars_dir.exists():
            for char_file in chars_dir.glob("*.yaml"):
                if char_file.name != "characters_index.yaml":
                    all_errors.extend(self.validate_character(char_file))
        
        # Validate narratives
        narratives_dir = self.framework_dir / "narratives"
        if narratives_dir.exists():
            for narrative_file in narratives_dir.rglob("*.yaml"):
                if "index" not in narrative_file.name and narrative_file.name != "story_vault_schema.yaml":
                    all_errors.extend(self.validate_narrative(narrative_file))
        
        return {
            "errors": all_errors,
            "warnings": all_warnings
        }


def main():
    parser = argparse.ArgumentParser(description="Validate meta framework")
    parser.add_argument("--framework-dir", default="meta_framework", help="Framework directory")
    
    args = parser.parse_args()
    
    validator = FrameworkValidator(args.framework_dir)
    results = validator.validate_all()
    
    if results["errors"]:
        print("[ERROR] Validation Errors:")
        for error in results["errors"]:
            print(f"  - {error}")
        exit(1)
    else:
        print("[OK] Framework validation passed!")
        
    if results["warnings"]:
        print("\n[WARNING] Warnings:")
        for warning in results["warnings"]:
            print(f"  - {warning}")


if __name__ == "__main__":
    main()

