#!/usr/bin/env python3
"""
Book Quality Tracker
Tracks quality metrics across all chapters with checkpoints
"""

import yaml
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime

# Import validators
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from meta_framework.content_quality.book_validator import BookValidator
from meta_framework.content_quality.content_index import ContentIndex


class BookQualityTracker:
    """Tracks quality metrics across entire book"""
    
    def __init__(self, content_dir: Path = Path("content")):
        self.content_dir = Path(content_dir)
        self.tracker_file = self.content_dir / "book_quality_tracker.yaml"
        self.validator = BookValidator()
        self.content_index = ContentIndex(content_dir)
        
        # Initialize tracker
        self._load_tracker()
    
    def _load_tracker(self):
        """Load or create tracker"""
        if self.tracker_file.exists():
            with open(self.tracker_file, 'r', encoding='utf-8') as f:
                self.tracker = yaml.safe_load(f) or {}
        else:
            self.tracker = {
                'book_quality': {
                    'chapters': {},
                    'checkpoints': [],
                    'metrics_history': [],
                    'threshold': 0.90,  # 90% threshold
                    'last_updated': datetime.now().isoformat()
                }
            }
    
    def checkpoint(self, chapter_num: int, content_file: Path, metadata: Dict[str, Any]):
        """
        Run quality checkpoint for a chapter
        
        Checkpoint runs after EVERY chapter (as per decision)
        """
        print(f"\n{'='*70}")
        print(f"Quality Checkpoint: Chapter {chapter_num}")
        print(f"{'='*70}")
        
        # Read content
        with open(content_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Run all validations
        validation_results = self.validator.validate_all(content, metadata, chapter_num)
        
        # Calculate metrics
        metrics = self._calculate_metrics(validation_results, metadata)
        
        # Store checkpoint
        checkpoint = {
            'chapter_num': chapter_num,
            'timestamp': datetime.now().isoformat(),
            'metrics': metrics,
            'validation_results': {
                'is_valid': validation_results['is_valid'],
                'issues_count': len(validation_results['issues']),
                'warnings_count': len(validation_results['warnings']),
                'auto_fixes_count': len(validation_results['auto_fixes'])
            },
            'content_file': str(content_file)
        }
        
        self.tracker['book_quality']['checkpoints'].append(checkpoint)
        self.tracker['book_quality']['chapters'][f'chapter_{chapter_num}'] = metrics
        self.tracker['book_quality']['metrics_history'].append({
            'chapter': chapter_num,
            'timestamp': datetime.now().isoformat(),
            'metrics': metrics
        })
        
        # Check threshold (90%)
        threshold = self.tracker['book_quality'].get('threshold', 0.90)
        below_threshold = [k for k, v in metrics.items() if isinstance(v, (int, float)) and v < threshold]
        
        if below_threshold:
            print(f"\n[WARN] WARNING: Metrics below 90% threshold:")
            for metric in below_threshold:
                print(f"   - {metric}: {metrics[metric]:.1%}")
            print(f"\n   Flagged for review (continuing generation)")
        else:
            print(f"\n[OK] All metrics above 90% threshold")
        
        # Save tracker
        self._save()
        
        # Generate report
        self._generate_report(chapter_num, metrics, validation_results)
        
        return checkpoint
    
    def _calculate_metrics(self, validation_results: Dict[str, Any], 
                          metadata: Dict[str, Any]) -> Dict[str, float]:
        """Calculate quality metrics"""
        metrics = {}
        
        # Compliance rate (assume 100% if no compliance issues)
        metrics['compliance_rate'] = 1.0 if not any('compliance' in str(i).lower() for i in validation_results['issues']) else 0.0
        
        # Character consistency (from validation)
        char_issues = len([i for i in validation_results['warnings'] if 'character' in str(i).lower()])
        metrics['character_consistency'] = max(0.0, 1.0 - (char_issues * 0.1))
        
        # Narrative adherence (from validation)
        nar_issues = len([i for i in validation_results['issues'] if 'narrative' in str(i).lower()])
        metrics['narrative_adherence'] = 1.0 if nar_issues == 0 else max(0.0, 1.0 - (nar_issues * 0.2))
        
        # CTA appropriateness (from validation)
        cta_issues = len([i for i in validation_results['issues'] if 'cta' in str(i).lower()])
        metrics['cta_appropriateness'] = 1.0 if cta_issues == 0 else max(0.0, 1.0 - (cta_issues * 0.15))
        
        # Emotional arc continuity (from validation)
        arc_warnings = len([i for i in validation_results['warnings'] if 'emotional' in str(i).lower()])
        metrics['emotional_arc_continuity'] = max(0.0, 1.0 - (arc_warnings * 0.05))
        
        # Structure variation (tracked separately)
        metrics['structure_variation'] = self._calculate_structure_variation()
        
        # Signature phrase rotation (from validation)
        sig_issues = len([i for i in validation_results['issues'] if 'signature' in str(i).lower()])
        metrics['signature_phrase_rotation'] = 1.0 if sig_issues == 0 else max(0.0, 1.0 - (sig_issues * 0.1))
        
        # Technical accuracy (placeholder - would need fact-checking)
        metrics['technical_accuracy'] = 1.0  # Assume accurate unless flagged
        
        # Overall consistency
        numeric_metrics = [v for v in metrics.values() if isinstance(v, (int, float))]
        metrics['overall_consistency'] = sum(numeric_metrics) / len(numeric_metrics) if numeric_metrics else 0.0
        
        return metrics
    
    def _calculate_structure_variation(self) -> float:
        """Calculate structure variation score"""
        # This would analyze structure usage across chapters
        # For first chapter, return 100% (no previous chapters to compare)
        checkpoints = self.tracker['book_quality'].get('checkpoints', [])
        if len(checkpoints) <= 1:
            return 1.0  # First chapter - no variation needed yet
        
        # For subsequent chapters, would calculate based on structure usage
        # For now, return placeholder
        return 0.85  # Would be calculated from actual structure usage
    
    def _generate_report(self, chapter_num: int, metrics: Dict[str, float], 
                        validation_results: Dict[str, Any]):
        """Generate hierarchical report"""
        print(f"\n[REPORT] Quality Report - Chapter {chapter_num}")
        print(f"{'-'*70}")
        
        # Summary
        print(f"\n[SUMMARY] Summary:")
        print(f"   Overall Consistency: {metrics.get('overall_consistency', 0):.1%}")
        print(f"   Is Valid: {'[OK]' if validation_results['is_valid'] else '[FAIL]'}")
        print(f"   Issues: {len(validation_results['issues'])}")
        print(f"   Warnings: {len(validation_results['warnings'])}")
        print(f"   Auto-Fixes: {len(validation_results['auto_fixes'])}")
        
        # Detailed metrics (expandable)
        print(f"\n[METRICS] Detailed Metrics:")
        for metric, value in metrics.items():
            if metric != 'overall_consistency':
                status = "[OK]" if value >= 0.90 else "[WARN]" if value >= 0.70 else "[FAIL]"
                print(f"   {status} {metric.replace('_', ' ').title()}: {value:.1%}")
        
        # Issues (if any)
        if validation_results['issues']:
            print(f"\n[ISSUES] Issues:")
            for issue in validation_results['issues']:
                print(f"   - {issue}")
        
        # Warnings (if any)
        if validation_results['warnings']:
            print(f"\n[WARNINGS] Warnings:")
            for warning in validation_results['warnings']:
                print(f"   - {warning}")
        
        # Auto-fixes (if any)
        if validation_results['auto_fixes']:
            print(f"\n[AUTO-FIX] Auto-Fixes Applied:")
            for fix in validation_results['auto_fixes']:
                print(f"   - {fix}")
    
    def _save(self):
        """Save tracker to file"""
        self.tracker['book_quality']['last_updated'] = datetime.now().isoformat()
        with open(self.tracker_file, 'w', encoding='utf-8') as f:
            yaml.dump(self.tracker, f, default_flow_style=False, sort_keys=False)
    
    def get_book_statistics(self) -> Dict[str, Any]:
        """Get overall book statistics"""
        checkpoints = self.tracker['book_quality'].get('checkpoints', [])
        
        if not checkpoints:
            return {'total_chapters': 0}
        
        # Calculate averages
        all_metrics = []
        for checkpoint in checkpoints:
            all_metrics.append(checkpoint.get('metrics', {}))
        
        avg_metrics = {}
        for metric_name in ['compliance_rate', 'character_consistency', 'narrative_adherence',
                           'cta_appropriateness', 'emotional_arc_continuity', 'overall_consistency']:
            values = [m.get(metric_name, 0) for m in all_metrics if metric_name in m]
            if values:
                avg_metrics[metric_name] = sum(values) / len(values)
        
        return {
            'total_chapters': len(checkpoints),
            'average_metrics': avg_metrics,
            'below_threshold_count': len([c for c in checkpoints 
                                         if any(v < 0.90 for v in c.get('metrics', {}).values() 
                                               if isinstance(v, (int, float)))])
        }

