#!/usr/bin/env python3
"""
Reference Check Script
Checks character/narrative consistency across content

Usage:
    python reference_check.py --character JOHN_SMITH
    python reference_check.py --narrative ALLEGORY_LEAKY_BUCKET
    python reference_check.py --all
"""

import yaml
import argparse
from pathlib import Path
from typing import Dict, List, Any, Optional


class ReferenceChecker:
    """Checks consistency of framework element references"""
    
    def __init__(self, framework_dir: Path = Path("meta_framework")):
        self.framework_dir = Path(framework_dir)
        self.content_dir = Path("content")
        
    def check_character_references(self, character_id: str) -> Dict[str, Any]:
        """Check all references to a character"""
        results = {
            "character_id": character_id,
            "references_found": [],
            "inconsistencies": [],
            "missing_profile": False
        }
        
        # Load character profile
        char_file = self.framework_dir / "characters" / f"{character_id}.yaml"
        if not char_file.exists():
            results["missing_profile"] = True
            return results
        
        with open(char_file, 'r') as f:
            char_data = yaml.safe_load(f)
        
        char_profile = char_data.get('character', {})
        
        # Search content for references
        # TODO: Implement content search
        # For now, return structure
        
        return results
    
    def check_narrative_references(self, narrative_id: str) -> Dict[str, Any]:
        """Check all references to a narrative element"""
        results = {
            "narrative_id": narrative_id,
            "references_found": [],
            "inconsistencies": [],
            "missing_element": False
        }
        
        # Try to find narrative file
        narrative_file = None
        for subdir in ["allegories", "case_studies", "metaphors", "story_threads"]:
            test_file = self.framework_dir / "narratives" / subdir / f"{narrative_id}.yaml"
            if test_file.exists():
                narrative_file = test_file
                break
        
        if not narrative_file:
            results["missing_element"] = True
            return results
        
        # Load narrative
        with open(narrative_file, 'r') as f:
            narrative_data = yaml.safe_load(f)
        
        # Search content for references
        # TODO: Implement content search
        
        return results
    
    def check_all_references(self) -> Dict[str, Any]:
        """Check all framework element references"""
        results = {
            "characters": {},
            "narratives": {},
            "summary": {
                "total_characters": 0,
                "total_narratives": 0,
                "issues_found": 0
            }
        }
        
        # Check all characters
        chars_dir = self.framework_dir / "characters"
        if chars_dir.exists():
            for char_file in chars_dir.glob("*.yaml"):
                if char_file.name != "characters_index.yaml":
                    with open(char_file, 'r') as f:
                        char_data = yaml.safe_load(f)
                        char_id = char_data.get('character', {}).get('id')
                        if char_id:
                            results["characters"][char_id] = self.check_character_references(char_id)
        
        # Check all narratives
        narratives_dir = self.framework_dir / "narratives"
        if narratives_dir.exists():
            for narrative_file in narratives_dir.rglob("*.yaml"):
                if "index" not in narrative_file.name:
                    with open(narrative_file, 'r') as f:
                        narrative_data = yaml.safe_load(f)
                        narrative = narrative_data.get('story_vault_entry') or narrative_data.get('narrative', {})
                        narrative_id = narrative.get('id')
                        if narrative_id:
                            results["narratives"][narrative_id] = self.check_narrative_references(narrative_id)
        
        # Calculate summary
        results["summary"]["total_characters"] = len(results["characters"])
        results["summary"]["total_narratives"] = len(results["narratives"])
        
        return results


def main():
    parser = argparse.ArgumentParser(description="Check framework element references")
    parser.add_argument("--character", help="Character ID to check")
    parser.add_argument("--narrative", help="Narrative ID to check")
    parser.add_argument("--all", action="store_true", help="Check all references")
    parser.add_argument("--output", help="Output file for results")
    
    args = parser.parse_args()
    
    checker = ReferenceChecker()
    
    if args.character:
        results = checker.check_character_references(args.character)
    elif args.narrative:
        results = checker.check_narrative_references(args.narrative)
    elif args.all:
        results = checker.check_all_references()
    else:
        print("Specify --character, --narrative, or --all")
        return
    
    if args.output:
        with open(args.output, 'w') as f:
            yaml.dump(results, f, default_flow_style=False)
        print(f"Results saved to {args.output}")
    else:
        print(yaml.dump(results, default_flow_style=False))


if __name__ == "__main__":
    main()

