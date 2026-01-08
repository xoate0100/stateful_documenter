#!/usr/bin/env python3
"""
Persona Selection Logic
Intelligently selects personas based on topic, context, and priority
Prioritizes Tier 1 (MUST HAVE) personas for maximum conversion
"""

import yaml
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import random


class PersonaSelector:
    """Selects appropriate personas based on context and priority"""
    
    def __init__(self, personas_file: Path = None):
        if personas_file is None:
            personas_file = Path(__file__).parent / "persona_profiles.yaml"
        
        with open(personas_file, 'r', encoding='utf-8') as f:
            self.personas_data = yaml.safe_load(f)
        
        self.personas = self.personas_data.get('personas', {})
    
    def get_tier_1_personas(self) -> List[str]:
        """Get all Tier 1 (MUST HAVE) personas"""
        tier_1 = []
        for persona_id, persona_data in self.personas.items():
            if persona_data.get('tier') == 1:
                tier_1.append(persona_id)
        return tier_1
    
    def get_tier_2_personas(self) -> List[str]:
        """Get all Tier 2 (HIGH NEED) personas"""
        tier_2 = []
        for persona_id, persona_data in self.personas.items():
            if persona_data.get('tier') == 2:
                tier_2.append(persona_id)
        return tier_2
    
    def get_tier_3_personas(self) -> List[str]:
        """Get all Tier 3 (MODERATE NEED) personas"""
        tier_3 = []
        for persona_id, persona_data in self.personas.items():
            if persona_data.get('tier') == 3:
                tier_3.append(persona_id)
        return tier_3
    
    def select_persona(
        self,
        topic: Optional[str] = None,
        context: Optional[Dict] = None,
        prefer_tier: Optional[int] = None,
        exclude_legacy: bool = True
    ) -> str:
        """
        Select persona based on topic, context, and priority
        
        Args:
            topic: Content topic (may hint at persona)
            context: Additional context (life stage, financial architecture, etc.)
            prefer_tier: Preferred tier (1, 2, or 3)
            exclude_legacy: Exclude legacy personas (engineer_retiree, etc.)
        
        Returns:
            Selected persona ID
        """
        # Filter personas
        available = list(self.personas.keys())
        
        if exclude_legacy:
            legacy_personas = ['engineer_retiree', 'faith_family_builder', 'widow_caregiver']
            available = [p for p in available if p not in legacy_personas]
        
        # If topic hints at persona, try to match
        if topic:
            topic_lower = topic.lower()
            # Check for keywords
            if any(word in topic_lower for word in ['retire', 'retirement', 'retired']):
                # Check if "just retired" or "early retiree"
                if any(word in topic_lower for word in ['just retired', 'recently retired', 'early retiree']):
                    if 'early_retiree_immediate_need' in available:
                        return 'early_retiree_immediate_need'
            
            if any(word in topic_lower for word in ['executive', 'corporate', 'vp', 'director']):
                if 'late_career_executive_retirement_window' in available:
                    return 'late_career_executive_retirement_window'
            
            if any(word in topic_lower for word in ['business', 'business owner', 'exit', 'exit strategy']):
                if 'successful_business_owner_exit_strategy' in available:
                    return 'successful_business_owner_exit_strategy'
            
            if any(word in topic_lower for word in ['pension', 'teacher', 'nurse', 'public servant']):
                if 'public_servant_pension_gap' in available:
                    return 'public_servant_pension_gap'
            
            if any(word in topic_lower for word in ['education', 'tuition', 'college', 'kids']):
                if 'squeeze_parent_retirement_education' in available:
                    return 'squeeze_parent_retirement_education'
        
        # If context provides hints
        if context:
            life_stage = context.get('life_stage')
            financial_architecture = context.get('financial_architecture')
            
            if life_stage == "just_retired" or life_stage == "0-2_years_retired":
                if 'early_retiree_immediate_need' in available:
                    return 'early_retiree_immediate_need'
            
            if financial_architecture == "no_pension" or financial_architecture == "401k_only":
                if 'dual_income_professional_no_pension' in available:
                    return 'dual_income_professional_no_pension'
        
        # Select by tier preference
        if prefer_tier == 1:
            tier_1 = self.get_tier_1_personas()
            tier_1_available = [p for p in tier_1 if p in available]
            if tier_1_available:
                return random.choice(tier_1_available)
        
        if prefer_tier == 2:
            tier_2 = self.get_tier_2_personas()
            tier_2_available = [p for p in tier_2 if p in available]
            if tier_2_available:
                return random.choice(tier_2_available)
        
        # Default: Prefer Tier 1, then Tier 2, then Tier 3
        tier_1 = self.get_tier_1_personas()
        tier_1_available = [p for p in tier_1 if p in available]
        if tier_1_available:
            return random.choice(tier_1_available)
        
        tier_2 = self.get_tier_2_personas()
        tier_2_available = [p for p in tier_2 if p in available]
        if tier_2_available:
            return random.choice(tier_2_available)
        
        tier_3 = self.get_tier_3_personas()
        tier_3_available = [p for p in tier_3 if p in available]
        if tier_3_available:
            return random.choice(tier_3_available)
        
        # Fallback: Return first available
        if available:
            return available[0]
        
        # Last resort: Return first persona
        return list(self.personas.keys())[0]
    
    def get_persona_by_id(self, persona_id: str) -> Optional[Dict]:
        """Get persona data by ID"""
        return self.personas.get(persona_id)
    
    def get_recommended_personas(self, count: int = 3, prefer_tier: int = 1) -> List[str]:
        """
        Get recommended personas for content generation
        Prioritizes Tier 1, rotates to avoid repetition
        """
        if prefer_tier == 1:
            tier_1 = self.get_tier_1_personas()
            tier_2 = self.get_tier_2_personas()
            # Mix Tier 1 and Tier 2
            recommended = tier_1[:2] + tier_2[:1]
        elif prefer_tier == 2:
            tier_2 = self.get_tier_2_personas()
            tier_1 = self.get_tier_1_personas()
            recommended = tier_2[:2] + tier_1[:1]
        else:
            tier_1 = self.get_tier_1_personas()
            recommended = tier_1[:count]
        
        return recommended[:count]
    
    def get_persona_story_examples(self, persona_id: str) -> List[str]:
        """Get story examples for persona"""
        persona = self.get_persona_by_id(persona_id)
        if persona:
            return persona.get('example_scenarios', [])
        return []
    
    def get_persona_metaphors(self, persona_id: str) -> List[str]:
        """Get recommended metaphors for persona"""
        persona = self.get_persona_by_id(persona_id)
        if persona:
            financial_arch = persona.get('demographics', {}).get('financial_architecture', '')
            # Map financial architecture to metaphors
            if 'pension' in financial_arch.lower() and 'gap' in financial_arch.lower():
                return ['bridge', 'gap', 'foundation']
            elif 'equity' in financial_arch.lower() and 'liquidity' in financial_arch.lower():
                return ['building', 'legacy', 'foundation']
            elif 'education' in financial_arch.lower():
                return ['balance', 'foundation', 'legacy']
            elif 'immediate' in financial_arch.lower() or 'just retired' in financial_arch.lower():
                return ['protection', 'foundation', 'security']
        return []

