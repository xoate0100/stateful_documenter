#!/usr/bin/env python3
"""
Generate Index Script
Rebuilds indexes from framework elements

Usage:
    python generate_index.py --index all
    python generate_index.py --index characters
    python generate_index.py --index narratives
"""

import yaml
import argparse
from pathlib import Path
from typing import Dict, Any, List


class IndexGenerator:
    """Rebuilds framework indexes from elements"""
    
    def __init__(self, framework_dir: Path = Path("meta_framework")):
        self.framework_dir = Path(framework_dir)
    
    def generate_characters_index(self) -> Dict[str, Any]:
        """Rebuild characters index from character files"""
        index = {"characters": {}}
        
        chars_dir = self.framework_dir / "characters"
        if not chars_dir.exists():
            return index
        
        for char_file in chars_dir.glob("*.yaml"):
            if char_file.name == "characters_index.yaml":
                continue
            
            try:
                with open(char_file, 'r') as f:
                    char_data = yaml.safe_load(f)
                    char = char_data.get('character', {})
                    char_id = char.get('id')
                    
                    if char_id:
                        index["characters"][char_id] = {
                            "name": char.get('name'),
                            "file": f"characters/{char_file.name}",
                            "first_appearance": char.get('first_appearance'),
                            "last_referenced": char.get('last_referenced'),
                            "status": "active"
                        }
            except Exception as e:
                print(f"Error processing {char_file}: {e}")
        
        return index
    
    def generate_narratives_index(self, narrative_type: str) -> Dict[str, Any]:
        """Rebuild narrative index for a specific type"""
        index = {narrative_type: {}}
        
        narratives_dir = self.framework_dir / "narratives" / narrative_type
        if not narratives_dir.exists():
            return index
        
        for narrative_file in narratives_dir.glob("*.yaml"):
            if f"{narrative_type}_index.yaml" in narrative_file.name or "index" in narrative_file.name:
                continue
            
            try:
                with open(narrative_file, 'r') as f:
                    narrative_data = yaml.safe_load(f)
                    narrative = narrative_data.get('story_vault_entry') or narrative_data.get('narrative', {})
                    narrative_id = narrative.get('id')
                    
                    if narrative_id:
                        index[narrative_type][narrative_id] = {
                            "title": narrative.get('title'),
                            "file": f"narratives/{narrative_type}/{narrative_file.name}",
                            "primary_theme": narrative.get('primary_theme'),
                            "used_in_chapters": narrative.get('usage_tracking', {}).get('used_in_chapters', []),
                            "status": "active"
                        }
            except Exception as e:
                print(f"Error processing {narrative_file}: {e}")
        
        return index
    
    def generate_all_indexes(self) -> Dict[str, Any]:
        """Generate all indexes"""
        results = {}
        
        # Characters
        results["characters"] = self.generate_characters_index()
        
        # Narratives
        for narrative_type in ["allegories", "case_studies", "metaphors", "story_threads"]:
            results[narrative_type] = self.generate_narratives_index(narrative_type)
        
        return results
    
    def save_index(self, index_data: Dict[str, Any], index_file: Path):
        """Save index to file"""
        index_file.parent.mkdir(parents=True, exist_ok=True)
        with open(index_file, 'w') as f:
            yaml.dump(index_data, f, default_flow_style=False, sort_keys=False)
        print(f"Index saved to {index_file}")


def main():
    parser = argparse.ArgumentParser(description="Generate framework indexes")
    parser.add_argument("--index", choices=["all", "characters", "allegories", "case_studies", "metaphors", "story_threads"],
                       default="all", help="Which index to generate")
    parser.add_argument("--output-dir", default="meta_framework", help="Output directory")
    
    args = parser.parse_args()
    
    generator = IndexGenerator(args.output_dir)
    
    if args.index == "all":
        results = generator.generate_all_indexes()
        
        # Save each index
        if "characters" in results:
            generator.save_index(results["characters"], Path(args.output_dir) / "characters" / "characters_index.yaml")
        
        for narrative_type in ["allegories", "case_studies", "metaphors", "story_threads"]:
            if narrative_type in results:
                generator.save_index(results[narrative_type], 
                                    Path(args.output_dir) / "narratives" / narrative_type / f"{narrative_type}_index.yaml")
    
    elif args.index == "characters":
        index = generator.generate_characters_index()
        generator.save_index(index, Path(args.output_dir) / "characters" / "characters_index.yaml")
    
    else:
        index = generator.generate_narratives_index(args.index)
        generator.save_index(index, Path(args.output_dir) / "narratives" / args.index / f"{args.index}_index.yaml")
    
    print("Index generation complete!")


if __name__ == "__main__":
    main()

