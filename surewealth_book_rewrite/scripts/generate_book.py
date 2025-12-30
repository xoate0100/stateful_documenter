#!/usr/bin/env python3
"""
Book Generation Script with Quality Tracking
Generates book chapters systematically with frequent quality checks
Updates lessons_learned.json as issues are discovered
"""

import sys
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.generate_content_with_quality import generate_content, save_and_validate_content


class BookGenerator:
    """Systematic book generation with quality tracking"""
    
    def __init__(self):
        self.book_structure = [
            {
                'chapter_num': 1,
                'title': 'Retirement Reality Check',
                'topic': 'The Hidden Risks in Your Retirement Plan',
                'funnel_stage': 'top_of_funnel',
                'emotional_state': 'fear',
                'emotional_sub_state': 'mild_fear',
                'persona': 'engineer_retiree',
                'narrative_id': 'ALLEGORY_HOUSE_OF_CARDS',
                'character_ids': [],
                'structure_type': 'statistic_first',
                'length': '3000-4000 words'
            },
            {
                'chapter_num': 2,
                'title': 'The Tax Leak Draining Your Wealth',
                'topic': 'Tax Planning Strategies for Retirement',
                'funnel_stage': 'top_of_funnel',
                'emotional_state': 'concern',
                'emotional_sub_state': 'moderate_concern',
                'persona': 'engineer_retiree',
                'narrative_id': 'ALLEGORY_LEAKY_BUCKET',
                'character_ids': [],
                'structure_type': 'story_first',
                'length': '3000-4000 words'
            },
            {
                'chapter_num': 3,
                'title': 'Social Security: The Claiming Strategy Most People Miss',
                'topic': 'Social Security Optimization',
                'funnel_stage': 'mid_funnel',
                'emotional_state': 'hope',
                'emotional_sub_state': 'growing_hope',
                'persona': 'faith_family_builder',
                'narrative_id': None,  # Will use case study
                'character_ids': [],
                'structure_type': 'question_first',
                'length': '3000-4000 words'
            },
            {
                'chapter_num': 4,
                'title': 'Protecting Your Legacy: Estate Planning That Works',
                'topic': 'Estate Planning and Legacy Protection',
                'funnel_stage': 'mid_funnel',
                'emotional_state': 'confidence',
                'emotional_sub_state': 'emerging_confidence',
                'persona': 'widow_caregiver',
                'narrative_id': None,  # Will use case study
                'character_ids': [],
                'structure_type': 'case_study_first',
                'length': '3000-4000 words'
            },
            {
                'chapter_num': 5,
                'title': 'Healthcare and Longevity: Planning for the Unknown',
                'topic': 'Healthcare Costs and Long-Term Care Planning',
                'funnel_stage': 'mid_funnel',
                'emotional_state': 'confidence',
                'emotional_sub_state': 'growing_confidence',
                'persona': 'engineer_retiree',
                'narrative_id': None,
                'character_ids': [],
                'structure_type': 'problem_first',
                'length': '3000-4000 words'
            },
            {
                'chapter_num': 6,
                'title': 'Real Outcomes: From Crisis to Confidence',
                'topic': 'Success Stories and Next Steps',
                'funnel_stage': 'lower_funnel',
                'emotional_state': 'action',
                'emotional_sub_state': 'readiness',
                'persona': 'engineer_retiree',
                'narrative_id': None,  # Will use case studies
                'character_ids': [],
                'structure_type': 'case_study_first',
                'length': '3000-4000 words'
            }
        ]
        
        self.lessons_updater = LessonsLearnedUpdater()
        self.quality_log = []
        
    def generate_chapter(self, chapter_spec: Dict[str, Any], 
                         generated_content: Optional[str] = None) -> Dict[str, Any]:
        """
        Generate a single chapter with full validation
        
        Args:
            chapter_spec: Chapter specification from book_structure
            generated_content: Pre-generated content (if available)
        
        Returns:
            Generation and validation results
        """
        print(f"\n{'='*80}")
        print(f"GENERATING CHAPTER {chapter_spec['chapter_num']}: {chapter_spec['title']}")
        print(f"{'='*80}\n")
        
        # Step 1: Generate prompt and metadata
        result = generate_content(
            topic=chapter_spec['topic'],
            format_type="chapter",
            platform="book",
            funnel_stage=chapter_spec['funnel_stage'],
            persona=chapter_spec['persona'],
            emotional_goal=chapter_spec['emotional_state'],
            narrative_id=chapter_spec.get('narrative_id'),
            character_ids=chapter_spec.get('character_ids', []),
            chapter_num=chapter_spec['chapter_num'],
            emotional_state=chapter_spec['emotional_state'],
            length=chapter_spec.get('length', '3000-4000 words'),
            output_content=False  # We'll validate after AI generation
        )
        
        print(f"\n[OK] Prompt generated: {result['file_paths']['prompt']}")
        print(f"[OK] Metadata created: {result['file_paths']['metadata']}")
        
        # Step 2: If content provided, validate it
        if generated_content:
            print(f"\n{'-'*80}")
            print("VALIDATING GENERATED CONTENT")
            print(f"{'-'*80}\n")
            
            validation = save_and_validate_content(
                content_id=result['content_id'],
                content=generated_content,
                chapter_num=chapter_spec['chapter_num']
            )
            
            # Step 3: Analyze quality and update lessons learned
            self._analyze_quality(chapter_spec, validation, generated_content)
            
            return {
                'chapter_spec': chapter_spec,
                'generation': result,
                'validation': validation,
                'content': generated_content
            }
        else:
            print(f"\n{'-'*80}")
            print("PROMPT READY FOR AI GENERATION")
            print(f"{'-'*80}")
            print(f"\nNext steps:")
            print(f"1. Use prompt from: {result['file_paths']['prompt']}")
            print(f"2. Generate content with AI (ChatGPT/Claude)")
            print(f"3. Call generate_chapter() again with generated_content parameter")
            
            return {
                'chapter_spec': chapter_spec,
                'generation': result,
                'validation': None,
                'content': None
            }
    
    def _analyze_quality(self, chapter_spec: Dict[str, Any], 
                        validation: Dict[str, Any], content: str):
        """Analyze quality and update lessons learned if issues found"""
        
        print(f"\n{'-'*80}")
        print("QUALITY ANALYSIS")
        print(f"{'-'*80}\n")
        
        issues_found = []
        
        # Check validation results
        if not validation['is_valid']:
            print(f"[FAIL] VALIDATION FAILED: {len(validation['issues'])} critical issues")
            for issue in validation['issues']:
                print(f"   - {issue}")
                issues_found.append({
                    'type': 'validation_failure',
                    'issue': issue,
                    'chapter': chapter_spec['chapter_num']
                })
        
        if validation['warnings']:
            print(f"[WARN] WARNINGS: {len(validation['warnings'])} warnings")
            for warning in validation['warnings']:
                print(f"   - {warning}")
                issues_found.append({
                    'type': 'warning',
                    'issue': warning,
                    'chapter': chapter_spec['chapter_num']
                })
        
        # Check quality metrics
        if validation.get('checkpoint'):
            metrics = validation['checkpoint']['metrics']
            print(f"\n📊 QUALITY METRICS:")
            for metric, value in metrics.items():
                if isinstance(value, (int, float)):
                    status = "[OK]" if value >= 0.90 else "[WARN]" if value >= 0.70 else "[FAIL]"
                    print(f"   {status} {metric.replace('_', ' ').title()}: {value:.1%}")
                    
                    if value < 0.90:
                        issues_found.append({
                            'type': 'quality_threshold',
                            'metric': metric,
                            'value': value,
                            'threshold': 0.90,
                            'chapter': chapter_spec['chapter_num']
                        })
        
        # Analyze content for patterns
        content_analysis = self._analyze_content_patterns(content, chapter_spec)
        if content_analysis.get('issues'):
            issues_found.extend(content_analysis['issues'])
        
        # Update lessons learned if new issues found
        if issues_found:
            print(f"\n{'-'*80}")
            print("UPDATING LESSONS LEARNED")
            print(f"{'-'*80}\n")
            
            for issue in issues_found:
                self.lessons_updater.add_issue(
                    issue_type=issue['type'],
                    description=issue.get('issue', str(issue)),
                    chapter=issue.get('chapter'),
                    context=chapter_spec
                )
                print(f"[OK] Added to lessons learned: {issue['type']}")
        
        # Log quality
        self.quality_log.append({
            'chapter': chapter_spec['chapter_num'],
            'timestamp': datetime.now().isoformat(),
            'validation': validation,
            'issues_found': issues_found,
            'metrics': validation.get('checkpoint', {}).get('metrics', {})
        })
        
        # Save quality log
        self._save_quality_log()
    
    def _analyze_content_patterns(self, content: str, chapter_spec: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze content for patterns that might indicate issues"""
        import re
        
        issues = []
        
        # Check for repetitive phrases
        permission_frames = len(re.findall(r"If you don't mind me asking", content, re.IGNORECASE))
        if permission_frames > 2:
            issues.append({
                'type': 'pattern_repetition',
                'issue': f'Permission frame "If you don\'t mind me asking" used {permission_frames} times',
                'chapter': chapter_spec['chapter_num']
            })
        
        # Check for structure patterns
        # This would be more sophisticated in production
        
        return {'issues': issues}
    
    def _save_quality_log(self):
        """Save quality log to file"""
        log_file = Path("content") / "book_quality_log.json"
        log_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(log_file, 'w', encoding='utf-8') as f:
            json.dump({
                'quality_log': self.quality_log,
                'last_updated': datetime.now().isoformat()
            }, f, indent=2, default=str)
    
    def generate_all_chapters(self, start_from: int = 1):
        """Generate all chapters starting from specified chapter number"""
        print(f"\n{'='*80}")
        print(f"BOOK GENERATION: Starting from Chapter {start_from}")
        print(f"{'='*80}\n")
        
        for chapter_spec in self.book_structure:
            if chapter_spec['chapter_num'] < start_from:
                continue
            
            result = self.generate_chapter(chapter_spec)
            
            if result['validation']:
                # Chapter validated, continue
                print(f"\n[OK] Chapter {chapter_spec['chapter_num']} complete")
            else:
                # Need AI generation
                print(f"\n[PAUSE] Chapter {chapter_spec['chapter_num']} prompt ready")
                print(f"   Waiting for AI-generated content...")
                break  # Stop here, wait for content
        
        print(f"\n{'='*80}")
        print("BOOK GENERATION SESSION COMPLETE")
        print(f"{'='*80}\n")


class LessonsLearnedUpdater:
    """Updates lessons_learned.json with new issues discovered during generation"""
    
    def __init__(self):
        self.lessons_file = Path("meta_framework/content_quality/lessons_learned.json")
        self._load_lessons()
    
    def _load_lessons(self):
        """Load lessons learned"""
        with open(self.lessons_file, 'r', encoding='utf-8') as f:
            self.lessons = json.load(f)
    
    def _save_lessons(self):
        """Save lessons learned"""
        self.lessons['last_updated'] = datetime.now().isoformat()
        with open(self.lessons_file, 'w', encoding='utf-8') as f:
            json.dump(self.lessons, f, indent=2, ensure_ascii=False)
    
    def add_issue(self, issue_type: str, description: str, 
                  chapter: Optional[int] = None, context: Optional[Dict] = None):
        """Add a new issue to lessons learned"""
        
        # Check if this is a new type of issue
        if issue_type not in self.lessons.get('discovered_issues', {}):
            self.lessons.setdefault('discovered_issues', {})[issue_type] = {
                'first_discovered': datetime.now().isoformat(),
                'occurrences': [],
                'description': description
            }
        
        # Add occurrence
        occurrence = {
            'timestamp': datetime.now().isoformat(),
            'chapter': chapter,
            'description': description,
            'context': context
        }
        
        self.lessons['discovered_issues'][issue_type]['occurrences'].append(occurrence)
        
        # Update last updated
        self.lessons['last_updated'] = datetime.now().isoformat()
        
        # Save
        self._save_lessons()


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Generate book with quality tracking")
    parser.add_argument("--chapter", type=int, help="Generate specific chapter number")
    parser.add_argument("--start-from", type=int, default=1, help="Start from chapter number")
    parser.add_argument("--all", action="store_true", help="Generate all chapters")
    
    args = parser.parse_args()
    
    generator = BookGenerator()
    
    if args.chapter:
        # Generate specific chapter
        chapter_spec = next((c for c in generator.book_structure 
                            if c['chapter_num'] == args.chapter), None)
        if chapter_spec:
            generator.generate_chapter(chapter_spec)
        else:
            print(f"Error: Chapter {args.chapter} not found")
    elif args.all:
        # Generate all chapters
        generator.generate_all_chapters(start_from=args.start_from)
    else:
        # Generate first chapter
        generator.generate_chapter(generator.book_structure[0])


if __name__ == "__main__":
    main()

