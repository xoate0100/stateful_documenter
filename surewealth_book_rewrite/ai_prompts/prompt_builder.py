#!/usr/bin/env python3
"""
AI Prompt Builder
Constructs stateful AI prompts with framework constraints

Usage:
    python prompt_builder.py --format social_post --topic tax_planning --persona engineer_retiree
"""

import yaml
import argparse
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional

# Import compliance enforcer and content quality tools
_project_root = Path(__file__).parent.parent
sys.path.insert(0, str(_project_root))
try:
    from meta_framework.language.compliance_enforcer import ComplianceEnforcer
except ImportError:
    ComplianceEnforcer = None

try:
    from meta_framework.content_quality.content_validator import ContentValidator
    from meta_framework.content_quality.content_metadata import ContentMetadata
    from meta_framework.content_quality.content_index import ContentIndex
except ImportError:
    ContentValidator = None
    ContentMetadata = None
    ContentIndex = None


class PromptBuilder:
    """Builds AI prompts with framework constraints"""
    
    def __init__(self, framework_dir: Path = Path("meta_framework")):
        self.framework_dir = Path(framework_dir)
        self.prompts_dir = Path("ai_prompts")
        self._element_cache = {}  # Cache for element existence checks
        # Initialize compliance enforcer if available
        if ComplianceEnforcer:
            try:
                self.compliance_enforcer = ComplianceEnforcer()
            except Exception:
                self.compliance_enforcer = None
        else:
            self.compliance_enforcer = None
        
        # Initialize content quality tools if available
        if ContentValidator:
            try:
                self.content_validator = ContentValidator()
            except Exception:
                self.content_validator = None
        else:
            self.content_validator = None
        
        if ContentMetadata:
            try:
                self.content_metadata = ContentMetadata()
            except Exception:
                self.content_metadata = None
        else:
            self.content_metadata = None
        
        if ContentIndex:
            try:
                self.content_index = ContentIndex()
            except Exception:
                self.content_index = None
        else:
            self.content_index = None
        
    def load_system_prompt(self) -> str:
        """Load base system prompt"""
        with open(self.prompts_dir / "system_prompts" / "base_system_prompt.yaml", 'r') as f:
            system_data = yaml.safe_load(f)
        
        prompt = f"""You are {system_data['system_prompt']['role']}

Core Principles:
{chr(10).join(f"- {p}" for p in system_data['system_prompt']['core_principles'])}

Voice Characteristics:
{chr(10).join(f"- {v}" for v in system_data['system_prompt']['voice_characteristics'])}

Required Elements:
{chr(10).join(f"- {e}" for e in system_data['system_prompt']['required_elements'])}

Forbidden Elements:
{chr(10).join(f"- {f}" for f in system_data['system_prompt']['forbidden_elements'])}
"""
        return prompt
    
    def load_format_prompt(self, format_type: str) -> Dict[str, Any]:
        """Load format-specific prompt template"""
        format_file = self.prompts_dir / "format_prompts" / f"{format_type}_prompt.yaml"
        if not format_file.exists():
            raise ValueError(f"Format prompt not found: {format_type}")
        
        with open(format_file, 'r') as f:
            return yaml.safe_load(f)
    
    def load_framework_elements(self, topic: str, persona: Optional[str] = None) -> Dict[str, Any]:
        """Load relevant framework elements for topic"""
        elements = {
            "narratives": [],
            "characters": [],
            "tools": [],
            "ctas": []
        }
        
        # TODO: Query framework for relevant elements based on topic
        # For now, return structure
        
        return elements
    
    def load_language_constraints(self) -> Dict[str, Any]:
        """Load language constraints"""
        constraints = {}
        
        # Load vocabulary
        vocab_file = self.framework_dir / "language" / "vocabulary.yaml"
        if vocab_file.exists():
            with open(vocab_file, 'r') as f:
                vocab = yaml.safe_load(f)
                constraints['banned_words'] = vocab.get('banned_words', [])
                constraints['approved_words'] = vocab.get('approved_power_words', [])
        
        # Load signature phrases
        phrases_file = self.framework_dir / "language" / "signature_phrases.yaml"
        if phrases_file.exists():
            with open(phrases_file, 'r') as f:
                phrases = yaml.safe_load(f)
                constraints['signature_phrases'] = phrases.get('signature_phrases', [])
        
        # Load transcript-derived language patterns (Phase 1 integration)
        pattern_files = [
            'normalization_patterns.yaml',
            'reframing_patterns.yaml',
            'mathematical_proof_patterns.yaml',
            'empowerment_patterns.yaml',
            'future_visioning_patterns.yaml',
            'celebration_patterns.yaml',
            'confirmation_patterns.yaml',
            'friction_resolution.yaml',
            'emotional_transitions.yaml',
            'psychological_principles.yaml',
            'question_frameworks.yaml',  # New: Question-based engagement
            'permission_frames.yaml',  # New: Permission language
            'presuppositions.yaml'  # New: NLP presuppositions
        ]
        
        for pattern_file in pattern_files:
            pattern_path = self.framework_dir / "language" / pattern_file
            if pattern_path.exists():
                try:
                    with open(pattern_path, 'r') as f:
                        pattern_data = yaml.safe_load(f)
                        # Extract key patterns for prompt
                        pattern_name = pattern_file.replace('.yaml', '').replace('_', ' ')
                        constraints[pattern_name] = pattern_data
                except Exception as e:
                    # Log error but continue - don't block other patterns
                    import logging
                    logging.warning(f"Failed to load {pattern_file}: {str(e)}")
                    continue
        
        return constraints
    
    def format_exists(self, format_type: str) -> bool:
        """Check if format prompt exists"""
        format_file = self.prompts_dir / "format_prompts" / f"{format_type}_prompt.yaml"
        return format_file.exists()
    
    def persona_exists(self, persona: str) -> bool:
        """Check if persona exists"""
        personas_file = self.framework_dir.parent / "personas" / "persona_profiles.yaml"
        if not personas_file.exists():
            return False
        
        with open(personas_file, 'r') as f:
            personas = yaml.safe_load(f)
            return persona in personas.get('personas', {})
    
    def narrative_exists(self, narrative_id: str) -> bool:
        """Check if narrative element exists"""
        # Check all narrative subdirectories
        narratives_dir = self.framework_dir / "narratives"
        for subdir in ["allegories", "case_studies", "metaphors", "story_threads"]:
            narrative_file = narratives_dir / subdir / f"{narrative_id}.yaml"
            if narrative_file.exists():
                return True
        
        # Also check indexes
        for index_file in narratives_dir.rglob("*index.yaml"):
            with open(index_file, 'r') as f:
                index_data = yaml.safe_load(f)
                # Check various index structures
                for key in ['allegories', 'metaphors', 'case_studies', 'story_threads']:
                    if key in index_data:
                        items = index_data[key]
                        if isinstance(items, list):
                            if narrative_id in items:
                                return True
                        elif isinstance(items, dict):
                            if narrative_id in items:
                                return True
        
        return False
    
    def character_exists(self, character_id: str) -> bool:
        """Check if character exists"""
        char_file = self.framework_dir / "characters" / f"{character_id}.yaml"
        if char_file.exists():
            return True
        
        # Check index
        index_file = self.framework_dir / "characters" / "characters_index.yaml"
        if index_file.exists():
            with open(index_file, 'r') as f:
                index_data = yaml.safe_load(f)
                if character_id in index_data.get('characters', {}):
                    return True
        
        return False
    
    def tool_exists(self, tool_id: str) -> bool:
        """Check if tool exists"""
        tools_file = self.framework_dir / "tools_ctas" / "tools_index.yaml"
        if not tools_file.exists():
            return False
        
        with open(tools_file, 'r') as f:
            tools = yaml.safe_load(f)
            return tool_id in tools.get('tools', {})
    
    def validate_request(self, 
                        format_type: str,
                        persona: Optional[str],
                        narrative_ids: Optional[List[str]],
                        character_ids: Optional[List[str]],
                        tool_ids: Optional[List[str]]) -> List[str]:
        """Validate request before building prompt"""
        errors = []
        
        # Validate format
        if not self.format_exists(format_type):
            errors.append(f"Invalid format: {format_type}")
        
        # Validate persona
        if persona and not self.persona_exists(persona):
            errors.append(f"Persona not found: {persona}")
        
        # Validate narratives
        if narrative_ids:
            for narrative_id in narrative_ids:
                if not self.narrative_exists(narrative_id):
                    errors.append(f"Narrative not found: {narrative_id}")
        
        # Validate characters
        if character_ids:
            for char_id in character_ids:
                if not self.character_exists(char_id):
                    errors.append(f"Character not found: {char_id}")
        
        # Validate tools
        if tool_ids:
            for tool_id in tool_ids:
                if not self.tool_exists(tool_id):
                    errors.append(f"Tool not found: {tool_id}")
        
        return errors
    
    def build_prompt(self, 
                    format_type: str,
                    topic: str,
                    persona: Optional[str] = None,
                    length: Optional[str] = None,
                    emotional_goal: Optional[str] = None,
                    narrative_ids: Optional[List[str]] = None,
                    character_ids: Optional[List[str]] = None,
                    tool_ids: Optional[List[str]] = None,
                    validate: bool = True) -> str:
        """Build complete AI prompt"""
        
        # Validate request if requested
        if validate:
            validation_errors = self.validate_request(
                format_type=format_type,
                persona=persona,
                narrative_ids=narrative_ids or [],
                character_ids=character_ids or [],
                tool_ids=tool_ids or []
            )
            
            if validation_errors:
                raise ValueError(f"Validation errors:\n" + "\n".join(f"  - {e}" for e in validation_errors))
        
        # Load components
        system_prompt = self.load_system_prompt()
        format_template = self.load_format_prompt(format_type)
        language_constraints = self.load_language_constraints()
        framework_elements = self.load_framework_elements(topic, persona)
        
        # Build user prompt
        user_prompt = f"""Generate a {format_type} about {topic}"""
        
        if persona:
            user_prompt += f" for persona: {persona}"
        
        if length:
            user_prompt += f"\n- Length: {length}"
        
        if emotional_goal:
            user_prompt += f"\n- Emotional goal: {emotional_goal}"
        
        if narrative_ids:
            user_prompt += f"\n- Use narratives: {', '.join(narrative_ids)}"
        
        if character_ids:
            user_prompt += f"\n- Reference characters: {', '.join(character_ids)}"
        
        if tool_ids:
            user_prompt += f"\n- Include tools: {', '.join(tool_ids)}"
        
        # Add language constraints
        if language_constraints.get('banned_words'):
            user_prompt += f"\n\nNEVER use these words: {', '.join(language_constraints['banned_words'][:10])}"
        
        if language_constraints.get('signature_phrases'):
            user_prompt += f"\n\nConsider using these signature phrases naturally: {', '.join(language_constraints['signature_phrases'][:3])}"
        
        # Add transcript-derived language patterns
        pattern_guidance = []
        if 'normalization patterns' in language_constraints:
            patterns = language_constraints['normalization patterns'].get('normalization_patterns', {}).get('general_normalization', [])
            if patterns:
                pattern_guidance.append(f"Use normalization patterns to reduce shame/anxiety: {patterns[0] if patterns else ''}")
        
        if 'reframing patterns' in language_constraints:
            patterns = language_constraints['reframing patterns'].get('reframing_patterns', {}).get('crisis_to_opportunity', [])
            if patterns:
                pattern_guidance.append(f"Reframe problems as opportunities: {patterns[0] if patterns else ''}")
        
        if 'mathematical proof patterns' in language_constraints:
            patterns = language_constraints['mathematical proof patterns'].get('mathematical_proof_patterns', {}).get('daily_cost_calculation', [])
            if patterns:
                pattern_guidance.append(f"Use numbers to create objective truth: Break down to daily/monthly amounts")
        
        if 'friction resolution' in language_constraints:
            friction = language_constraints['friction resolution'].get('friction_resolution', {})
            if friction:
                pattern_guidance.append("Proactively prevent confusion: Use 'You might be wondering...' sections, break down complex concepts, provide visual breaks")
        
        if pattern_guidance:
            user_prompt += f"\n\nLanguage Pattern Guidance:\n" + "\n".join(f"- {g}" for g in pattern_guidance)
        
        # Add question frameworks if available
        if 'question frameworks' in language_constraints:
            qf = language_constraints['question frameworks'].get('question_frameworks', {})
            if qf:
                user_prompt += f"\n\nQuestion-Based Engagement:\n"
                user_prompt += "- Use emotional questions to create engagement\n"
                user_prompt += "- Use pre-qualifying questions: 'If [benefit], would you like to know how?'\n"
                user_prompt += "- Add permission frames before questions: 'If you don't mind me asking...'\n"
        
        # Add permission frames if available
        if 'permission frames' in language_constraints:
            pf = language_constraints['permission frames'].get('permission_frames', {})
            if pf:
                user_prompt += f"\n\nPermission Frames:\n"
                user_prompt += "- Use 'If you don't mind me asking...' before personal questions\n"
                user_prompt += "- Use 'Before we go any further...' for transitions\n"
        
        # Add presuppositions if available
        if 'presuppositions' in language_constraints:
            presup = language_constraints['presuppositions'].get('presuppositions', {})
            if presup:
                user_prompt += f"\n\nPresuppositions:\n"
                user_prompt += "- Use 'When you [desired state]...' instead of 'If you...'\n"
                user_prompt += "- Use 'When we work together...' to create partnership\n"
        
        # Add compliance requirements (CRITICAL)
        if self.compliance_enforcer:
            compliance_instructions = self.compliance_enforcer.get_compliance_prompt_instructions()
            user_prompt += f"\n\n{compliance_instructions}"
        
        # Add lessons learned guidance if available
        if self.content_validator:
            # Determine funnel stage from format or default
            funnel_stage = self._determine_funnel_stage(format_type, topic)
            lessons_guidance = self.content_validator.get_lessons_guidance(funnel_stage)
            if lessons_guidance:
                user_prompt += f"\n\nLESSONS LEARNED - Critical Guidelines:\n{lessons_guidance}"
                user_prompt += "\n\nIMPORTANT: Follow these guidelines to avoid common issues:"
                user_prompt += "\n- Vary structure from previous pieces (don't use same formula)"
                user_prompt += "\n- Use permission frames strategically (max 2 per piece)"
                user_prompt += "\n- Rotate signature phrases (don't repeat same ones)"
                user_prompt += "\n- Match CTA to funnel stage (1 soft CTA for top/mid-funnel)"
                user_prompt += "\n- Provide concrete story resolutions (not vague)"
                user_prompt += "\n- Use indirect quotes or narrative style (not scripted dialogue)"
                user_prompt += "\n- Balance number specificity (not too perfect, not too vague)"
        
        # Add content index insights if available
        if self.content_index:
            # Check for similar content to avoid repetition
            funnel_stage = self._determine_funnel_stage(format_type, topic)
            similar_content = []
            
            if persona:
                similar_by_persona = self.content_index.search_by_persona(persona)
                similar_content.extend(similar_by_persona[:3])  # Get 3 most recent
            
            if topic:
                topic_slug = topic.lower().replace(' ', '_')
                similar_by_topic = self.content_index.search_by_topic(topic_slug)
                similar_content.extend(similar_by_topic[:2])
            
            if similar_content:
                user_prompt += f"\n\nCONTENT INDEX INSIGHTS:"
                user_prompt += f"\n- Found {len(similar_content)} similar pieces in index"
                user_prompt += f"\n- Ensure this content is unique and doesn't repeat previous structure"
                user_prompt += f"\n- Vary your approach from existing content on this topic/persona"
        
        # Add format-specific requirements
        if 'structure' in format_template:
            user_prompt += f"\n\nFollow this structure:\n{yaml.dump(format_template['structure'], default_flow_style=False)}"
        
        # Combine
        full_prompt = f"""{system_prompt}

---

{user_prompt}

Generate the content now, following all constraints and maintaining brand voice."""
        
        return full_prompt
    
    def _determine_funnel_stage(self, format_type: str, topic: str) -> str:
        """Determine funnel stage from format and topic"""
        # Default mapping - can be enhanced
        if format_type in ['social_post', 'blog_post']:
            return 'top_of_funnel'
        elif format_type in ['email', 'webinar']:
            return 'mid_funnel'
        elif format_type in ['case_study', 'comparison']:
            return 'lower_funnel'
        return 'mid_funnel'  # Default
    
    def save_prompt(self, prompt: str, output_file: Path):
        """Save generated prompt to file"""
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w') as f:
            f.write(prompt)
        print(f"Prompt saved to {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Build AI prompts with framework constraints")
    parser.add_argument("--format", required=True, help="Content format (social_post, email, chapter, blog)")
    parser.add_argument("--topic", required=True, help="Content topic")
    parser.add_argument("--persona", help="Target persona")
    parser.add_argument("--length", help="Content length")
    parser.add_argument("--emotional-goal", help="Emotional goal")
    parser.add_argument("--narratives", nargs="+", help="Narrative IDs to use")
    parser.add_argument("--characters", nargs="+", help="Character IDs to reference")
    parser.add_argument("--tools", nargs="+", help="Tool IDs to include")
    parser.add_argument("--output", help="Output file path")
    parser.add_argument("--skip-validation", action="store_true", help="Skip pre-generation validation")
    
    args = parser.parse_args()
    
    builder = PromptBuilder()
    
    try:
        prompt = builder.build_prompt(
            format_type=args.format,
            topic=args.topic,
            persona=args.persona,
            length=args.length,
            emotional_goal=args.emotional_goal,
            narrative_ids=args.narratives,
            character_ids=args.characters,
            tool_ids=args.tools,
            validate=not args.skip_validation
        )
        
        if args.output:
            builder.save_prompt(prompt, Path(args.output))
        else:
            print(prompt)
    except ValueError as e:
        print(f"Validation Error: {e}", file=sys.stderr)
        return 1
    
    return 0


if __name__ == "__main__":
    main()

