#!/usr/bin/env bash
set -euo pipefail
STATUS=0

# Detect project type
detect_project_type() {
  # Try MVP_SPECIFICATION first
  if [ -f "0_phase0_bootstrap/MVP_SPECIFICATION.yaml" ]; then
    PROJECT_TYPE=$(python3 <<EOF
import yaml
try:
    with open("0_phase0_bootstrap/MVP_SPECIFICATION.yaml") as f:
        mvp = yaml.safe_load(f)
    project_type = mvp.get("Project_Type") or mvp.get("project_type")
    if project_type:
        print(project_type.lower())
    else:
        print("programming")
except:
    print("programming")
EOF
    )
  else
    # Fall back to ACTIVE_PLAN
    if [ -f "6_ai_runtime_context/ACTIVE_PLAN.yaml" ]; then
      PROJECT_TYPE=$(python3 <<EOF
import yaml
try:
    with open("6_ai_runtime_context/ACTIVE_PLAN.yaml") as f:
        plan = yaml.safe_load(f)
    project_type = plan.get("project_type", "programming")
    print(project_type.lower())
except:
    print("programming")
EOF
      )
    else
      PROJECT_TYPE="programming"
    fi
  fi
  echo "$PROJECT_TYPE"
}

PROJECT_TYPE=$(detect_project_type)

# Skip test coverage for documentation projects
if [ "$PROJECT_TYPE" = "documentation" ]; then
  echo "[coverage] Project type is 'documentation' - skipping test coverage checks (no code to test)"
  exit 0
fi

# Load feature flags to get component-specific thresholds
load_thresholds() {
  if [ -f "0_phase0_bootstrap/feature_flags.yml" ]; then
    # Use Python to parse YAML and extract thresholds
    python3 <<EOF
import yaml, sys
try:
    with open("0_phase0_bootstrap/feature_flags.yml") as f:
        flags = yaml.safe_load(f)
    components = flags.get("components", {})
    gates = flags.get("gates", {})
    
    # Backend threshold
    backend_threshold = components.get("backend", {}).get("coverage_threshold", 100)
    print(f"BACKEND_THRESHOLD={backend_threshold}")
    
    # Frontend threshold
    frontend_threshold = components.get("frontend", {}).get("coverage_threshold", 95)
    print(f"FRONTEND_THRESHOLD={frontend_threshold}")
    
    # Shared threshold
    shared_threshold = components.get("shared", {}).get("coverage_threshold", 90)
    print(f"SHARED_THRESHOLD={shared_threshold}")
    
    # Block on coverage drop
    BLOCK_ON_COVERAGE = gates.get("block_on_coverage_drop", true)
    print(f"BLOCK_ON_COVERAGE={str(BLOCK_ON_COVERAGE).lower()}")
except Exception as e:
    print("# Error loading thresholds, using defaults", file=sys.stderr)
    print("BACKEND_THRESHOLD=100")
    print("FRONTEND_THRESHOLD=95")
    print("SHARED_THRESHOLD=90")
    print("BLOCK_ON_COVERAGE=true")
EOF
  else
    echo "BACKEND_THRESHOLD=100"
    echo "FRONTEND_THRESHOLD=95"
    echo "SHARED_THRESHOLD=90"
    echo "BLOCK_ON_COVERAGE=true"
  fi
}

eval $(load_thresholds)

# Backend (pytest + coverage)
if [ -d "backend" ]; then
  python3 -m pip install --quiet pytest pytest-cov || true
  if pytest -q --cov=backend --cov-report=term-missing --cov-report=json:coverage-backend.json; then
    # Check coverage threshold
    COVERAGE=$(python3 -c "import json; print(json.load(open('coverage-backend.json'))['totals']['percent_covered'])")
    if (( $(echo "$COVERAGE < $BACKEND_THRESHOLD" | bc -l) )); then
      echo "[coverage] Backend coverage $COVERAGE% below threshold $BACKEND_THRESHOLD%"
      if [ "$BLOCK_ON_COVERAGE" = "true" ]; then
        STATUS=1
      fi
    fi
  else
    STATUS=1
  fi
fi

# Frontend (jest/vitest suggested)
if [ -f "frontend/package.json" ]; then
  if (cd frontend && npm ci --silent && npm test --silent -- --coverage); then
    # Frontend coverage check would go here if coverage output is available
    echo "[coverage] Frontend tests passed (threshold: ${FRONTEND_THRESHOLD}%)"
  else
    STATUS=1
  fi
fi

exit $STATUS

