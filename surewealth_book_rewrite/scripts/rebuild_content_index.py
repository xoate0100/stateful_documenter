#!/usr/bin/env python3
"""
Rebuild Content Index
Rebuilds the content index from all metadata files
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from meta_framework.content_quality.content_index import ContentIndex


def main():
    """Rebuild content index"""
    print("Rebuilding content index...")
    
    index_manager = ContentIndex()
    index_manager.rebuild_index()
    
    stats = index_manager.get_statistics()
    
    print("\n" + "=" * 70)
    print("Content Index Rebuilt")
    print("=" * 70)
    print(f"Total pieces: {stats['total_pieces']}")
    print(f"\nBy Funnel:")
    for funnel, count in stats['by_funnel'].items():
        print(f"  {funnel}: {count}")
    print(f"\nBy Persona:")
    for persona, count in stats['by_persona'].items():
        print(f"  {persona}: {count}")
    print(f"\nBy Topic:")
    for topic, count in stats['by_topic'].items():
        print(f"  {topic}: {count}")
    print(f"\nBy Platform:")
    for platform, count in stats['by_platform'].items():
        print(f"  {platform}: {count}")
    print(f"\nLast updated: {stats.get('last_updated', 'N/A')}")


if __name__ == "__main__":
    main()

