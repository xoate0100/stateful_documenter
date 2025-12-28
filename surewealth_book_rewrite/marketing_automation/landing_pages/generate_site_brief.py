#!/usr/bin/env python3
"""
Landing Page Site Brief Generator
Generates site briefs for the white-paper-sites project using SITE_BRIEF_TEMPLATE.md

Usage:
    python generate_site_brief.py --topic tax_planning --persona engineer_retiree --tool lifetime_tax_calculator
"""

import argparse
import yaml
import json
from pathlib import Path
from typing import Dict, Any, Optional
from datetime import datetime


class SiteBriefGenerator:
    """Generate site briefs for landing pages"""
    
    def __init__(self, framework_dir: Path = Path("meta_framework")):
        self.framework_dir = Path(framework_dir)
        self.templates_dir = Path("docs/templates")
        
    def load_framework_elements(self, topic: str, persona: Optional[str] = None,
                               narrative_ids: Optional[list] = None,
                               tool_id: Optional[str] = None) -> Dict[str, Any]:
        """Load relevant framework elements"""
        elements = {
            "narratives": [],
            "characters": [],
            "tools": [],
            "persona": None,
            "language_constraints": {}
        }
        
        # Load persona if specified
        if persona:
            persona_file = Path("personas/persona_profiles.yaml")
            if persona_file.exists():
                with open(persona_file, 'r') as f:
                    personas = yaml.safe_load(f)
                    elements["persona"] = personas.get("personas", {}).get(persona)
        
        # Load narratives if specified
        if narrative_ids:
            for narrative_id in narrative_ids:
                # Try to find narrative file
                narrative_file = self.framework_dir / "narratives" / "allegories" / f"{narrative_id}.yaml"
                if not narrative_file.exists():
                    narrative_file = self.framework_dir / "narratives" / "case_studies" / f"CASE_STUDY_{narrative_id}.yaml"
                
                if narrative_file.exists():
                    with open(narrative_file, 'r') as f:
                        narrative = yaml.safe_load(f)
                        elements["narratives"].append(narrative)
        
        # Load tool if specified
        if tool_id:
            tool_file = Path("marketing_automation/calculator_integration/calculator_system.yaml")
            if tool_file.exists():
                with open(tool_file, 'r') as f:
                    tools = yaml.safe_load(f)
                    elements["tools"] = [t for t in tools.get("calculator_system", {}).get("calculators", {}).values() 
                                       if t.get("id") == tool_id]
        
        # Load language constraints
        vocab_file = self.framework_dir / "language" / "vocabulary.yaml"
        if vocab_file.exists():
            with open(vocab_file, 'r') as f:
                elements["language_constraints"]["vocabulary"] = yaml.safe_load(f)
        
        phrases_file = self.framework_dir / "language" / "signature_phrases.yaml"
        if phrases_file.exists():
            with open(phrases_file, 'r') as f:
                elements["language_constraints"]["phrases"] = yaml.safe_load(f)
        
        return elements
    
    def generate_site_brief(self, topic: str, tool_id: str, persona: Optional[str] = None,
                           narrative_ids: Optional[list] = None,
                           output_file: Optional[Path] = None) -> Dict[str, Any]:
        """Generate a site brief following SITE_BRIEF_TEMPLATE.md structure"""
        
        # Load framework elements
        elements = self.load_framework_elements(topic, persona, narrative_ids, tool_id)
        
        # Get persona data
        persona_data = elements.get("persona", {})
        narrative = elements.get("narratives", [{}])[0] if elements.get("narratives") else {}
        tool = elements.get("tools", [{}])[0] if elements.get("tools") else {}
        
        # Build site brief structure
        site_brief = {
            "projectOverview": {
                "siteName": f"{tool.get('name', 'Calculator')} Landing Page",
                "primaryPurpose": f"Convert visitors to use {tool.get('name', 'the calculator')} and book a strategy call",
                "targetOutcome": "Email capture + calculator completion → strategy call booking",
                "businessContext": "SureWealth Solutions retirement planning and tax optimization",
                "successMetrics": {
                    "primaryKPI": "Calculator completions with email capture",
                    "secondaryKPIs": ["Strategy call bookings", "White paper downloads"],
                    "conversionFunnelStages": ["Awareness", "Interest", "Consideration", "Action"]
                }
            },
            "targetAudience": {
                "demographics": {
                    "ageRange": persona_data.get("demographics", {}).get("age", "55-65"),
                    "incomeLevel": persona_data.get("demographics", {}).get("income", "$100k-$200k"),
                    "assetLevel": "Retirement accounts, savings",
                    "geographicFocus": "United States",
                    "occupationBackground": persona_data.get("demographics", {}).get("occupation", "Professional"),
                    "educationLevel": persona_data.get("demographics", {}).get("education", "College degree")
                },
                "psychographics": {
                    "sophisticationLevel": persona_data.get("psychographics", {}).get("decision_style", "Medium"),
                    "financialLiteracy": persona_data.get("psychographics", {}).get("decision_style", "Above average"),
                    "decisionStyle": persona_data.get("psychographics", {}).get("decision_style", "Analytical"),
                    "informationConsumption": persona_data.get("psychographics", {}).get("communication_preference", "Detailed content"),
                    "trustThreshold": "High - need proof and validation"
                },
                "emotionalDrivers": {
                    "primaryFears": [
                        {"fear": f, "context": ""} for f in persona_data.get("emotional_profile", {}).get("primary_fears", [])
                    ],
                    "primaryDesires": [
                        {"desire": d, "context": ""} for d in persona_data.get("emotional_profile", {}).get("aspirations", [])
                    ],
                    "currentEmotionalState": {
                        "dominantEmotion": narrative.get("story_vault_entry", {}).get("emotional_start_state", ["anxious"])[0] if narrative else "curious",
                        "secondaryEmotions": narrative.get("story_vault_entry", {}).get("emotional_start_state", [])[1:] if narrative else [],
                        "emotionalJourneyGoal": narrative.get("story_vault_entry", {}).get("emotional_end_state", ["confident"])[0] if narrative else "confident"
                    }
                },
                "avatarPersona": {
                    "name": persona_data.get("name", "Target Prospect"),
                    "oneSentenceDescription": f"{persona_data.get('name', 'Target')} seeking {topic} solutions",
                    "keyQuote": persona_data.get("cta_angle", "I need to understand my options")
                }
            },
            "marketingCopy": {
                "coreValueProposition": {
                    "headline": tool.get("name", "Get Your Personalized Analysis"),
                    "subheadline": f"Discover your {topic} impact and see what you might be missing",
                    "elevatorPitch": f"Use our {tool.get('name', 'calculator')} to understand your {topic} situation and get personalized recommendations",
                    "uniqueSellingProposition": "Personalized analysis based on your specific situation, not generic advice"
                },
                "keyMessages": [
                    {
                        "message": narrative.get("story_vault_entry", {}).get("narrative_structure", {}).get("realization", "Key insight") if narrative else "Key message 1",
                        "supportingPoints": narrative.get("story_vault_entry", {}).get("pain_points", [])[:3] if narrative else [],
                        "proofPoints": []
                    }
                ],
                "copyTone": {
                    "tone": persona_data.get("voice_adaptation", {}).get("tone", "Professional yet approachable"),
                    "voiceCharacteristics": {
                        "formalityLevel": "Semi-formal",
                        "sentenceStructure": "Mix of short and medium sentences",
                        "vocabulary": "Plainspoken with clear explanations"
                    },
                    "dos": [
                        "Use data to support claims",
                        "Address objections directly",
                        "Maintain empathetic tone"
                    ],
                    "donts": [
                        "Avoid financial jargon without explanation",
                        "Don't make unrealistic promises",
                        "Never use banned words"
                    ]
                },
                "objectionHandling": [
                    {
                        "objection": "This seems too good to be true",
                        "responseStrategy": "Provide proof and transparency",
                        "keyPhrases": ["Let's run your numbers", "See the math for yourself"]
                    }
                ]
            },
            "storyFramework": {
                "narrativeFramework": "PAS (Problem, Agitate, Solution)",
                "frameworkRationale": "Works well for analytical personas who need to understand the problem before accepting solutions",
                "coreStoryArc": {
                    "act1": narrative.get("story_vault_entry", {}).get("narrative_structure", {}).get("setup", "Current situation") if narrative else "Current situation",
                    "act2": narrative.get("story_vault_entry", {}).get("narrative_structure", {}).get("conflict", "The problem") if narrative else "The problem",
                    "act3": narrative.get("story_vault_entry", {}).get("narrative_structure", {}).get("resolution", "The solution") if narrative else "The solution"
                },
                "metaphors": [
                    {
                        "metaphor": narrative.get("story_vault_entry", {}).get("metaphors_symbols", {}).get("primary_metaphor", "Metaphor") if narrative else "Metaphor",
                        "usage": "Throughout the page to explain concepts",
                        "visualRepresentation": "Illustration or graphic"
                    }
                ],
                "storyElements": {
                    "hero": "The visitor",
                    "guide": "SureWealth Solutions",
                    "villain": "Financial uncertainty and tax inefficiency",
                    "transformation": "From uncertainty to clarity and confidence"
                }
            },
            "seo": {
                "primaryKeywords": [
                    {
                        "keyword": f"{topic} calculator",
                        "searchIntent": "Informational",
                        "searchVolume": "Medium",
                        "competitionLevel": "Medium"
                    }
                ],
                "secondaryKeywords": [],
                "longTailKeywords": [],
                "seoMeta": {
                    "metaTitle": f"{tool.get('name', 'Calculator')} - {topic.title()} Analysis",
                    "metaDescription": f"Use our {tool.get('name', 'calculator')} to understand your {topic} situation. Get personalized recommendations.",
                    "h1Strategy": "Benefit-focused headline",
                    "h2H6Strategy": "Clear hierarchy supporting main message"
                },
                "contentSeo": {
                    "targetWordCount": "1500-2500 words",
                    "keywordDensity": "Primary: 1-2%, Secondary: 0.5-1%",
                    "internalLinking": "Link to relevant book chapters and resources",
                    "externalLinking": "Authoritative financial sources"
                }
            },
            "ctaStrategy": {
                "primaryCta": {
                    "ctaText": tool.get("cta_angle", "Get Your Personalized Analysis"),
                    "ctaType": "Calculator",
                    "ctaPlacement": "Above fold, mid-page, end of content",
                    "ctaRationale": "Multiple touchpoints for different engagement levels"
                },
                "secondaryCtas": [
                    {
                        "text": "Book Your Strategy Call",
                        "type": "Schedule",
                        "placement": "End of content",
                        "purpose": "Convert calculator completers"
                    }
                ],
                "ctaPsychology": {
                    "urgencyElements": ["Limited consultation slots", "Tax deadlines approaching"],
                    "valueProposition": "Free personalized analysis",
                    "riskReduction": "No obligation, cancel anytime",
                    "socialProofIntegration": "Client testimonials and success stories"
                }
            },
            "layoutFlow": {
                "pageStructure": {
                    "layoutType": "Single-page scroll",
                    "totalSections": 6,
                    "estimatedScrollDepth": "Long-form: 3000px+"
                },
                "userFlow": [
                    {
                        "sectionName": "Hero Section",
                        "moduleType": "Hero",
                        "purpose": "Grab attention and introduce value",
                        "keyContent": ["Headline", "Subheadline", "Calculator CTA"],
                        "ctaPresent": True,
                        "visualRequirements": ["Hero image or illustration"]
                    },
                    {
                        "sectionName": "Problem Section",
                        "moduleType": "Key Idea",
                        "purpose": "Establish the problem",
                        "keyContent": ["Problem statement", "Pain points"],
                        "ctaPresent": False,
                        "visualRequirements": ["Supporting graphic"]
                    },
                    {
                        "sectionName": "Calculator Section",
                        "moduleType": "Calculator",
                        "purpose": "Engage with interactive tool",
                        "keyContent": ["Calculator embed", "Instructions"],
                        "ctaPresent": True,
                        "visualRequirements": ["Calculator interface"]
                    },
                    {
                        "sectionName": "Solution Preview",
                        "moduleType": "Key Idea",
                        "purpose": "Show what they'll learn",
                        "keyContent": ["Benefits", "What's included"],
                        "ctaPresent": False,
                        "visualRequirements": ["Icon or graphic"]
                    },
                    {
                        "sectionName": "Social Proof",
                        "moduleType": "Testimonials",
                        "purpose": "Build trust",
                        "keyContent": ["Client testimonials", "Success metrics"],
                        "ctaPresent": False,
                        "visualRequirements": ["Client photos or graphics"]
                    },
                    {
                        "sectionName": "Final CTA",
                        "moduleType": "CTA",
                        "purpose": "Convert to strategy call",
                        "keyContent": ["Urgency", "Value prop", "Booking CTA"],
                        "ctaPresent": True,
                        "visualRequirements": ["CTA button design"]
                    }
                ],
                "engagementPoints": {
                    "interactiveElements": ["Calculator", "Email capture form"],
                    "engagementRationale": "Calculator provides value while capturing leads",
                    "progressiveDisclosure": "Results revealed after email capture"
                },
                "mobileConsiderations": {
                    "mobileFirstElements": ["Calculator", "CTA buttons"],
                    "simplifiedFlow": "Streamlined for mobile interaction",
                    "touchTargets": "Minimum 44px for interactive elements"
                }
            },
            "designSpecs": {
                "visualIdentity": {
                    "colorPalette": {
                        "primaryColor": "#0C4A6E",
                        "accentColor": "#EAB308",
                        "backgroundColors": ["#FFFFFF", "#F9FAFB"],
                        "textColors": ["#1F2937", "#6B7280"],
                        "colorPsychology": "Blue for trust, gold for value"
                    },
                    "typography": {
                        "primaryFont": "Inter, system-ui, sans-serif",
                        "headingFont": "Inter, system-ui, sans-serif",
                        "fontSizes": {
                            "h1": "48px",
                            "h2": "36px",
                            "body": "16px"
                        },
                        "typographyRationale": "Clean, professional, readable"
                    }
                },
                "visualStyle": {
                    "designAesthetic": "Modern, trustworthy, professional",
                    "imageStyle": "Professional photography, authentic",
                    "iconStyle": "Line icons, minimal",
                    "visualHierarchy": "Clear, guided attention flow"
                },
                "componentSpecs": {
                    "buttonStyles": {
                        "primary": "Blue background, white text, 12px padding",
                        "secondary": "Transparent with blue border"
                    },
                    "formStyles": "Clean inputs, clear labels, helpful placeholders",
                    "cardStyles": "White background, subtle shadow, rounded corners",
                    "spacingSystem": "8px base unit, consistent rhythm"
                }
            },
            "psychologicalDesign": {
                "trustBuilding": {
                    "trustSignals": ["Client testimonials", "Years in business", "Certifications"],
                    "placementStrategy": "Throughout page, especially near CTAs",
                    "visualTrustElements": ["Professional design", "Client photos"]
                },
                "persuasionPrinciples": [
                    {
                        "principle": "Social Proof",
                        "implementation": "Testimonials and success stories"
                    },
                    {
                        "principle": "Authority",
                        "implementation": "Credentials and expertise shown"
                    },
                    {
                        "principle": "Reciprocity",
                        "implementation": "Free calculator provides value"
                    }
                ],
                "cognitiveLoadManagement": {
                    "informationChunking": "Clear sections, digestible content",
                    "progressiveDisclosure": "Calculator results after engagement",
                    "visualBreaks": "Whitespace and visuals separate sections"
                },
                "emotionalTriggers": {
                    "section1EmotionalGoal": "Curiosity and intrigue",
                    "section2EmotionalGoal": "Recognition and empathy",
                    "section3EmotionalGoal": "Engagement and value",
                    "finalSectionEmotionalGoal": "Confidence and action"
                }
            },
            "contentModules": [
                {
                    "moduleType": "Hero",
                    "purpose": "Grab attention and introduce value",
                    "requiredContent": ["Headline", "Subheadline", "Primary CTA"],
                    "optionalContent": ["Supporting image", "Trust badge"],
                    "tone": "Confident, benefit-focused",
                    "visualRequirements": ["Hero image or illustration"]
                },
                {
                    "moduleType": "Calculator",
                    "purpose": "Engage visitor and capture email",
                    "requiredContent": ["Calculator embed", "Instructions", "Email capture"],
                    "optionalContent": ["Preview of results", "Social proof"],
                    "tone": "Helpful, clear",
                    "visualRequirements": ["Calculator interface design"]
                }
            ],
            "technicalRequirements": {
                "technicalSpecs": {
                    "integrationRequirements": ["Calculator embed", "Email capture", "Analytics"],
                    "analyticsEvents": ["VIEW_HERO", "START_CALCULATOR", "COMPLETE_CALCULATOR", "SUBMIT_EMAIL", "CLICK_CTA"],
                    "performanceTargets": "LCP < 2.5s, CLS < 0.1"
                },
                "contentDelivery": {
                    "contentFormat": "JSON for white-paper-sites project",
                    "updateFrequency": "Static with quarterly updates",
                    "abTestingConsiderations": "Headlines, CTAs, calculator placement"
                }
            },
            "complianceLegal": {
                "requiredDisclaimers": [
                    {
                        "disclaimer": "This calculator is for educational purposes only and does not constitute financial advice.",
                        "placement": "Near calculator, footer"
                    }
                ],
                "regulatoryConsiderations": {
                    "industryRegulations": "SEC compliance for financial advice",
                    "privacyRequirements": "GDPR-compliant data collection",
                    "accessibilityStandards": "WCAG 2.1 AA compliance"
                }
            }
        }
        
        return site_brief
    
    def save_brief(self, brief: Dict[str, Any], output_file: Path):
        """Save site brief as JSON"""
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w') as f:
            json.dump(brief, f, indent=2)
        print(f"Site brief saved to {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Generate site brief for landing page")
    parser.add_argument("--topic", required=True, help="Content topic (e.g., tax_planning)")
    parser.add_argument("--tool", required=True, help="Tool/calculator ID")
    parser.add_argument("--persona", help="Target persona")
    parser.add_argument("--narratives", nargs="+", help="Narrative IDs to use")
    parser.add_argument("--output", help="Output file path")
    
    args = parser.parse_args()
    
    generator = SiteBriefGenerator()
    brief = generator.generate_site_brief(
        topic=args.topic,
        tool_id=args.tool,
        persona=args.persona,
        narrative_ids=args.narratives
    )
    
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = Path("site_briefs") / f"site_brief_{args.topic}_{args.tool}.json"
    
    generator.save_brief(brief, output_path)
    
    print(f"\nSite brief generated successfully!")
    print(f"Use this file with the white-paper-sites project:")
    print(f"  https://github.com/xoate0100/white-paper-sites")


if __name__ == "__main__":
    main()

