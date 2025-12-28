#!/usr/bin/env python3
"""
Generate Long-Form Facebook Story Posts
Creates 3 conversion-optimized story posts using integrated patterns
"""

import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from ai_prompts.prompt_builder import PromptBuilder
import yaml


def generate_facebook_post(topic: str, persona: str, narrative_id: str = None, 
                          emotional_goal: str = "curiosity", length: int = 2500):
    """Generate a long-form Facebook post"""
    
    builder = PromptBuilder()
    
    try:
        prompt = builder.build_prompt(
            format_type="social_post",
            topic=topic,
            persona=persona,
            length=str(length),
            emotional_goal=emotional_goal,
            narrative_ids=[narrative_id] if narrative_id else None,
            validate=False  # Skip validation for now
        )
        
        return prompt
    except Exception as e:
        print(f"Error generating prompt: {e}")
        return None


def create_direct_prompt(topic: str, persona: str, narrative_id: str = None, 
                         emotional_goal: str = "curiosity"):
    """Create prompt directly without loading problematic YAML files"""
    
    # Load what we can
    framework_dir = Path("meta_framework")
    language_dir = framework_dir / "language"
    
    # Load new patterns
    patterns = {}
    new_pattern_files = [
        'question_frameworks.yaml',
        'permission_frames.yaml',
        'presuppositions.yaml',
        'reframing_patterns.yaml',
        'emotional_transitions.yaml',
        'normalization_patterns.yaml'
    ]
    
    for pattern_file in new_pattern_files:
        pattern_path = language_dir / pattern_file
        if pattern_path.exists():
            try:
                with open(pattern_path, 'r', encoding='utf-8') as f:
                    patterns[pattern_file.replace('.yaml', '').replace('_', ' ')] = yaml.safe_load(f)
            except:
                pass
    
    # Load signature phrases
    sig_phrases = []
    sig_file = language_dir / "signature_phrases.yaml"
    if sig_file.exists():
        try:
            with open(sig_file, 'r', encoding='utf-8') as f:
                sig_data = yaml.safe_load(f)
                sig_phrases = sig_data.get('signature_phrases', [])
        except:
            pass
    
    # Load narrative if provided
    narrative_content = ""
    if narrative_id:
        narrative_path = framework_dir / "narratives" / "allegories" / f"{narrative_id}.yaml"
        if narrative_path.exists():
            try:
                with open(narrative_path, 'r', encoding='utf-8') as f:
                    narrative_data = yaml.safe_load(f)
                    if 'narrative_structure' in narrative_data:
                        narrative_content = f"""
Narrative Structure to Use:
- Setup: {narrative_data['narrative_structure'].get('setup', '')}
- Conflict: {narrative_data['narrative_structure'].get('conflict', '')}
- Realization: {narrative_data['narrative_structure'].get('realization', '')}
- Resolution: {narrative_data['narrative_structure'].get('resolution', '')}
"""
            except:
                pass
    
    # Build comprehensive prompt
    prompt = f"""You are a conversion-optimized copywriter for SureWealth Solutions, specializing in retirement planning and tax-optimized wealth strategies. Your writing is empathetic, expert-level, and always focused on helping prospects understand their financial situation and take action.

CORE PRINCIPLES:
- Empathetic Expert - not guru or fearmonger
- Focus on outcomes, emotions, and decisions - not mechanics
- Always preserve curiosity gaps
- Every piece must end with action bias toward conversation
- Never suggest financial products directly
- Use plainspoken, non-technical language

VOICE CHARACTERISTICS:
- Plainspoken
- Empathetic
- Confident
- Non-technical
- Authoritative but approachable

SENTENCE STYLE:
- Short paragraphs (1-3 lines)
- Rhetorical questions
- Contrast pairs
- Direct statements

REQUIRED ELEMENTS:
- Use signature phrases naturally: {', '.join(sig_phrases[:3]) if sig_phrases else 'N/A'}
- Include appropriate CTAs
- Maintain emotional arc
- Preserve curiosity gaps
- Apply language patterns from transcript analysis

FORBIDDEN ELEMENTS:
- NEVER use: invest, investment, account, deposit, free, best, always, expert, financial planner, gain, growth, risk free, savings
- AI-sounding phrases ("delve into", "harness the power of", etc.)
- Product pitches
- Guarantees or promises
- Overly technical jargon without explanation

---

QUESTION-BASED ENGAGEMENT:
- Use emotional questions to create engagement: "How do you feel about [situation]?", "What would that mean to you?", "Why is that important to you?"
- Use pre-qualifying questions: "If [benefit], would you like to know how?"
- Add permission frames before questions: "If you don't mind me asking..."

PERMISSION FRAMES:
- Use "If you don't mind me asking..." before personal questions
- Use "Before we go any further..." for transitions
- Use "Let me share something with you..." for important information

PRESUPPOSITIONS:
- Use "When you [desired state]..." instead of "If you..."
- Use "When we work together..." to create partnership
- Use "Once you [action]..." to assume positive outcomes

REFRAMING PATTERNS:
- Transform problems into opportunities: "This is exactly what [strategy] was designed for"
- Reframe crisis to expected: "This is why we plan for [scenario]"
- Use: "This isn't a problem—it's an opportunity to [action]"

EMOTIONAL TRANSITIONS:
- Fear to Calm: "This is normal. Many people feel this way."
- Confusion to Clarity: "Let me simplify this..."
- Shame to Empowerment: "This happens to everyone"
- Overwhelm to Control: "You're in control here"
- Hopelessness to Hope: "You'll get through this"
- Crisis to Opportunity: "This is exactly what [tool/strategy] was designed for"

---

GENERATE A LONG-FORM FACEBOOK STORY POST:

Topic: {topic}
Persona: {persona}
Emotional Goal: {emotional_goal}
Length: 2,000-3,000 words (very long-form story format)
Platform: Facebook (allows up to 5,000 characters, but this should be a comprehensive story)

FORMAT REQUIREMENTS:
- Start with a compelling hook (first 125 characters are critical)
- Use short paragraphs (1-3 lines each)
- Break up text with line breaks
- Use strategic emojis (sparingly, for structure)
- Tell a complete story with narrative arc
- Include emotional journey
- End with soft, question-based CTA

STORY STRUCTURE:
{narrative_content if narrative_content else "- Use narrative arc: Setup → Conflict → Realization → Resolution"}

CONTENT REQUIREMENTS:
- Tell a relatable story (can be composite case study or allegory)
- Use emotional questions throughout
- Include permission frames naturally
- Use presuppositions ("When you...", "When we...")
- Reference pain points and aspirations
- Create curiosity gaps
- Build to emotional resolution
- End with question-based CTA

CTA OPTIONS (use question-based):
- "If there were a way to [benefit], would you like to know how?"
- "Would it be worth 20 minutes of your time to see if this could work for you?"
- "What would [benefit] mean to your retirement?"

SIGNATURE PHRASES TO USE NATURALLY:
{chr(10).join(f"- {p}" for p in sig_phrases[:5]) if sig_phrases else "- Use brand voice naturally"}

---

Generate the complete long-form Facebook story post now. Make it engaging, story-driven, and conversion-optimized. Use all the patterns above naturally throughout the narrative."""
    
    return prompt


def main():
    """Generate 3 Facebook posts"""
    
    posts = [
        {
            "topic": "The Hidden Tax Leak Draining Your Retirement (And How Most People Never See It)",
            "persona": "engineer_retiree",
            "narrative": "ALLEGORY_LEAKY_BUCKET",
            "emotional_goal": "curiosity",
            "filename": "facebook_post_1_tax_leak.md"
        },
        {
            "topic": "Why Your 401k Might Not Be Enough: The Retirement Income Gap Nobody Talks About",
            "persona": "faith_family_builder",
            "narrative": "ALLEGORY_HOUSE_OF_CARDS",
            "emotional_goal": "empathy",
            "filename": "facebook_post_2_401k_gap.md"
        },
        {
            "topic": "The Retirement Income Gap: What Happens When Social Security Isn't Enough",
            "persona": "widow_caregiver",
            "narrative": None,
            "emotional_goal": "hope",
            "filename": "facebook_post_3_income_gap.md"
        }
    ]
    
    output_dir = Path("content/social")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print("=" * 70)
    print("Generating 3 Long-Form Facebook Story Posts")
    print("=" * 70)
    print()
    
    for i, post_config in enumerate(posts, 1):
        print(f"Generating Post {i}: {post_config['topic']}")
        print(f"  Persona: {post_config['persona']}")
        print(f"  Emotional Goal: {post_config['emotional_goal']}")
        
        # Generate prompt
        prompt = create_direct_prompt(
            topic=post_config['topic'],
            persona=post_config['persona'],
            narrative_id=post_config['narrative'],
            emotional_goal=post_config['emotional_goal']
        )
        
        # Save prompt
        prompt_file = output_dir / f"{post_config['filename'].replace('.md', '_prompt.txt')}"
        with open(prompt_file, 'w', encoding='utf-8') as f:
            f.write(prompt)
        
        print(f"  [OK] Prompt saved to: {prompt_file}")
        print()
    
    print("=" * 70)
    print("Next Steps:")
    print("=" * 70)
    print("1. Copy each prompt from the generated files")
    print("2. Paste into ChatGPT, Claude, or your AI tool")
    print("3. AI will generate the long-form story posts")
    print("4. Review and refine as needed")
    print()
    print("Generated prompt files:")
    for post_config in posts:
        print(f"  - content/social/{post_config['filename'].replace('.md', '_prompt.txt')}")


if __name__ == "__main__":
    main()

