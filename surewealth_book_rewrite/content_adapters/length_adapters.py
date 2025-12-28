#!/usr/bin/env python3
"""
Content Length Adapters
Condense or expand content while maintaining core message and emotional arc

Usage:
    python length_adapters.py --input content.md --target-length 280 --format social_post
"""

import argparse
from pathlib import Path
from typing import Dict, Any
import re


class LengthAdapter:
    """Adapts content length while preserving core message"""
    
    def __init__(self):
        self.preservation_rules = {
            "cta": "Always preserve CTAs",
            "emotional_hook": "Preserve emotional hooks",
            "framework_references": "Keep character/story references",
            "key_statistics": "Preserve important numbers",
            "signature_phrases": "Maintain signature phrases"
        }
    
    def condense(self, content: str, target_length: int, format_type: str = "general") -> str:
        """Condense content to target length"""
        
        # Extract critical elements first
        critical_elements = self._extract_critical_elements(content)
        
        # Condense paragraphs
        condensed = self._condense_paragraphs(content, target_length)
        
        # Re-insert critical elements
        condensed = self._reinsert_critical_elements(condensed, critical_elements)
        
        # Final length check
        if len(condensed) > target_length:
            condensed = self._aggressive_condense(condensed, target_length)
        
        return condensed
    
    def expand(self, content: str, target_length: int, format_type: str = "general") -> str:
        """Expand content to target length"""
        
        # Identify expansion opportunities
        expansion_points = self._find_expansion_points(content)
        
        # Add details, examples, stories
        expanded = self._add_expansion_content(content, expansion_points, target_length)
        
        return expanded
    
    def _extract_critical_elements(self, content: str) -> Dict[str, Any]:
        """Extract elements that must be preserved"""
        elements = {
            "ctas": [],
            "hooks": [],
            "references": [],
            "statistics": [],
            "signature_phrases": []
        }
        
        # Extract CTAs (common patterns)
        cta_patterns = [
            r"Let's [^.]*",
            r"Get your [^.]*",
            r"See where [^.]*",
            r"What's your [^.]*"
        ]
        for pattern in cta_patterns:
            elements["ctas"].extend(re.findall(pattern, content, re.IGNORECASE))
        
        # Extract statistics (numbers with context)
        stat_pattern = r"\$?\d+[,\d]*(?:%|years?|months?|dollars?)"
        elements["statistics"] = re.findall(stat_pattern, content)
        
        # Extract framework references (uppercase IDs)
        ref_pattern = r"[A-Z_]{3,}"
        elements["references"] = re.findall(ref_pattern, content)
        
        return elements
    
    def _condense_paragraphs(self, content: str, target_length: int) -> str:
        """Condense paragraphs while maintaining flow"""
        paragraphs = content.split('\n\n')
        condensed_paragraphs = []
        current_length = 0
        
        for para in paragraphs:
            if current_length + len(para) <= target_length:
                condensed_paragraphs.append(para)
                current_length += len(para)
            else:
                # Condense this paragraph
                remaining = target_length - current_length
                if remaining > 50:  # Only if meaningful space
                    condensed_para = self._condense_single_paragraph(para, remaining)
                    condensed_paragraphs.append(condensed_para)
                break
        
        return '\n\n'.join(condensed_paragraphs)
    
    def _condense_single_paragraph(self, paragraph: str, max_length: int) -> str:
        """Condense a single paragraph"""
        sentences = re.split(r'[.!?]+', paragraph)
        condensed_sentences = []
        current_length = 0
        
        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue
            
            if current_length + len(sentence) <= max_length:
                condensed_sentences.append(sentence)
                current_length += len(sentence)
            else:
                break
        
        return '. '.join(condensed_sentences) + '.'
    
    def _reinsert_critical_elements(self, content: str, elements: Dict[str, Any]) -> str:
        """Re-insert critical elements that may have been removed"""
        # Ensure CTAs are present
        if elements["ctas"] and not any(cta.lower() in content.lower() for cta in elements["ctas"]):
            content += f"\n\n{elements['ctas'][0]}"
        
        return content
    
    def _aggressive_condense(self, content: str, target_length: int) -> str:
        """Aggressively condense when needed"""
        # Remove filler words
        filler_words = ['very', 'really', 'quite', 'rather', 'somewhat', 'fairly']
        for word in filler_words:
            content = re.sub(rf'\b{word}\s+', '', content, flags=re.IGNORECASE)
        
        # Shorten common phrases
        replacements = {
            'in order to': 'to',
            'due to the fact that': 'because',
            'at this point in time': 'now',
            'for the purpose of': 'for'
        }
        for old, new in replacements.items():
            content = content.replace(old, new)
        
        # If still too long, take first N characters
        if len(content) > target_length:
            content = content[:target_length-3] + "..."
        
        return content
    
    def _find_expansion_points(self, content: str) -> List[Dict[str, Any]]:
        """Find places where content can be expanded"""
        expansion_points = []
        
        # Find short paragraphs
        paragraphs = content.split('\n\n')
        for i, para in enumerate(paragraphs):
            if len(para) < 100:
                expansion_points.append({
                    "type": "paragraph",
                    "index": i,
                    "current_length": len(para)
                })
        
        return expansion_points
    
    def _add_expansion_content(self, content: str, expansion_points: List[Dict], target_length: int) -> str:
        """Add content at expansion points"""
        # For now, simple expansion by adding examples
        # TODO: Use AI to generate relevant expansion content
        
        current_length = len(content)
        needed = target_length - current_length
        
        if needed > 0:
            # Add expansion placeholder
            content += f"\n\n[Expand with examples, stories, or details - {needed} characters needed]"
        
        return content


def main():
    parser = argparse.ArgumentParser(description="Adapt content length")
    parser.add_argument("--input", required=True, help="Input content file")
    parser.add_argument("--target-length", type=int, required=True, help="Target length in characters")
    parser.add_argument("--format", default="general", help="Content format")
    parser.add_argument("--direction", choices=["condense", "expand"], default="condense")
    parser.add_argument("--output", help="Output file")
    
    args = parser.parse_args()
    
    adapter = LengthAdapter()
    
    with open(args.input, 'r') as f:
        content = f.read()
    
    if args.direction == "condense":
        result = adapter.condense(content, args.target_length, args.format)
    else:
        result = adapter.expand(content, args.target_length, args.format)
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write(result)
        print(f"Content adapted and saved to {args.output}")
    else:
        print(result)


if __name__ == "__main__":
    main()

