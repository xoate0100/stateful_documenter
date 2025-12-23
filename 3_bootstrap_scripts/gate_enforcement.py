#!/usr/bin/env python3
"""
Gate enforcement module.
Implements gate checks from feature_flags.yml (warn_on_performance_regression, warn_on_mutation_drop)
"""
import sys
import pathlib

try:
    import yaml
except ImportError:
    print("[gate] Warning: PyYAML not installed. Install with: pip install PyYAML")
    sys.exit(0)


def load_feature_flags():
    """Load feature flags configuration"""
    flags_path = pathlib.Path("0_phase0_bootstrap/feature_flags.yml")
    if not flags_path.exists():
        return {}
    return yaml.safe_load(open(flags_path))


def detect_project_type() -> str:
    """Detect project type from MVP_SPECIFICATION or ACTIVE_PLAN"""
    # Try MVP_SPECIFICATION first
    mvp_path = pathlib.Path("0_phase0_bootstrap/MVP_SPECIFICATION.yaml")
    if mvp_path.exists():
        try:
            mvp = yaml.safe_load(open(mvp_path))
            project_type = mvp.get("Project_Type") or mvp.get("project_type")
            if project_type:
                return project_type.lower()
        except:
            pass
    
    # Fall back to ACTIVE_PLAN
    plan_path = pathlib.Path("6_ai_runtime_context/ACTIVE_PLAN.yaml")
    if plan_path.exists():
        try:
            plan = yaml.safe_load(open(plan_path))
            project_type = plan.get("project_type")
            if project_type:
                return project_type.lower()
        except:
            pass
    
    return "programming"


def warn_on_performance_regression(gates: dict, thresholds: dict):
    """
    Gate: warn_on_performance_regression
    Integrate with CI perf benchmark; log warnings only.
    """
    if not gates.get("warn_on_performance_regression", False):
        return True  # Not enabled
    
    threshold = thresholds.get("perf_regression_pct", 10)
    
    # Stub: Placeholder for performance testing
    # TODO: Integrate with actual performance benchmarking
    perf_report = pathlib.Path("ai_reports/performance_report.json")
    
    if not perf_report.exists():
        print("[gate] warn_on_performance_regression: No performance report found")
        print("  Tip: Run performance benchmarks to enable regression detection")
        return True  # Warning only
    
    # TODO: Parse performance report and check for regressions
    # For now, just log that the gate is active
    print(f"[gate] warn_on_performance_regression: Active (threshold: {threshold}%)")
    print("  Status: Performance regression detection not yet implemented")
    print("  Action: This is a stub - implement performance benchmarking")
    
    return True


def warn_on_mutation_drop(gates: dict, thresholds: dict):
    """
    Gate: warn_on_mutation_drop
    Stub mutation-testing job; mark TODO until engine implemented.
    """
    if not gates.get("warn_on_mutation_drop", False):
        return True  # Not enabled
    
    threshold = thresholds.get("mutation_kill", 75)
    
    # Stub: Placeholder for mutation testing
    mutation_report = pathlib.Path("ai_reports/mutation_report.json")
    
    if not mutation_report.exists():
        print("[gate] warn_on_mutation_drop: No mutation test report found")
        print("  Tip: Run mutation tests to enable mutation score tracking")
        return True  # Warning only
    
    # TODO: Parse mutation report and check for drops
    print(f"[gate] warn_on_mutation_drop: Active (threshold: {threshold}%)")
    print("  Status: Mutation testing not yet implemented")
    print("  Action: This is a stub - implement mutation testing (e.g., mutmut, stryker)")
    
    return True


def main():
    """Main gate enforcement"""
    flags = load_feature_flags()
    gates = flags.get("gates", {})
    thresholds = flags.get("thresholds", {})
    project_type = detect_project_type()
    
    if not gates:
        print("[gate] No gates configured")
        sys.exit(0)
    
    # Skip coverage/mutation gates for documentation projects
    if project_type == "documentation":
        print("[gate] Project type is 'documentation' - skipping code-related gates (coverage, mutation)")
        print("[gate] Documentation projects don't have code to test")
        sys.exit(0)
    
    results = []
    
    # Run gate checks (warnings only, non-blocking)
    results.append(warn_on_performance_regression(gates, thresholds))
    results.append(warn_on_mutation_drop(gates, thresholds))
    
    # Gates are warnings, so always exit 0
    print("[gate] Gate checks complete (warnings only)")
    sys.exit(0)


if __name__ == "__main__":
    main()

