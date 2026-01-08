# Microservices Architecture for Content Generation

## Overview

This microservices architecture enables **iterative, agentic content improvement** where quality checks and prompt services work together to incrementally refine content based on quantifiable outcome goals.

## Architecture Principles

1. **Stateful**: Each service maintains state and tracks improvements
2. **Quantifiable**: All operations produce measurable metrics (0.0-1.0)
3. **Atomic**: Each service performs a single, well-defined operation
4. **Iterative**: Services call each other to incrementally improve content
5. **Agentic**: Services communicate via agentic chat for intelligent decision-making
6. **Human-Centered**: Preserves emotional elements while optimizing for conversion

## Services

### 1. Content Orchestrator (`orchestrator.py`)
- Manages workflow, state, and iterative improvement loop
- Coordinates all services
- Tracks metrics and improvements

### 2. Quality Service (`quality_service.py`)
- Validates content against all quality dimensions
- Quantifies quality scores (0.0-1.0)
- Identifies issues and generates suggestions

### 3. Prompt Service (`prompt_service.py`) - TODO
- Generates and refines prompts
- Applies sales copy principles
- Integrates emotional elements

### 4. Emotional Service (`emotional_service.py`) - TODO
- Validates emotional elements
- Enhances emotional depth
- Ensures connectedness

### 5. Conversion Service (`conversion_service.py`) - TODO
- Validates conversion elements
- Enhances conversion optimization
- Ensures engagement tactics

### 6. Authority Service (`authority_service.py`) - TODO
- Validates authority elements
- Enhances credibility
- Ensures expertise signals

### 7. Trust Service (`trust_service.py`) - TODO
- Validates trust elements
- Enhances transparency
- Ensures honesty

## Usage Example

```python
from services.orchestrator import ContentOrchestrator
from services.quality_service import QualityService

# Initialize services
orchestrator = ContentOrchestrator()
orchestrator.quality_service = QualityService()

# Generate content with iterative improvement
result = orchestrator.generate_content(
    topic="Retirement Reality Check",
    metadata={
        "format_type": "chapter",
        "persona": "engineer_retiree",
        "funnel_stage": "top_of_funnel",
        "length": "3000-4000 words"
    },
    target_metrics={
        "structural": 0.95,
        "sales_copy": 0.90,
        "emotional": 0.85,
        "conversion": 0.90,
        "authority": 0.85,
        "trust": 0.90
    },
    max_iterations=5,
    ai_generator=your_ai_generator_function
)

print(f"Final Score: {result['overall_score']:.2f}")
print(f"Iterations: {result['iterations']}")
print(f"Improvement: {result['improvement_delta']:.2f}")
```

## Quality Dimensions

### Structural (Weight: 20%)
- Length compliance
- Structure completeness
- Compliance validation

### Sales Copy (Weight: 25%)
- Curiosity gaps
- Emotional tone
- Conceptual clarity
- Future pacing
- Actionable tidbits
- Delight/discovery

### Emotional (Weight: 20%)
- Tone consistency
- Emotional depth
- Connectedness
- Respect for intelligence

### Conversion (Weight: 15%)
- CTA effectiveness
- Engagement tactics
- "Wanting more" elements

### Authority (Weight: 10%)
- Citations
- Expertise signals
- Credibility

### Trust (Weight: 10%)
- Transparency
- Honesty
- No manipulation

## State Management

All generation state is saved to `state/generation/{request_id}.yaml` with:
- Iteration history
- Quality metrics per iteration
- Improvement deltas
- Service call logs
- Final content and metrics

## Next Steps

1. Implement remaining services (Prompt, Emotional, Conversion, Authority, Trust)
2. Add agentic chat integration
3. Implement iterative improvement loop
4. Add comprehensive quality checks
5. Create service-to-service communication patterns

