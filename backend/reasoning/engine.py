from reasoning.evidence import collect_evidence
from reasoning.rules import apply_rules
from reasoning.storyteller import generate_story
from reasoning.prioritizer import build_dashboard
from reasoning.health import calculate_health


def analyze_reasoning(
    schema,
    missing_values,
    duplicates,
    outliers,
    correlation,
    feature_selection
):
    """
    Run the complete reasoning pipeline.

    Parameters
    ----------
    schema : list

    missing_values : dict

    duplicates : dict

    outliers : dict

    correlation : dict

    feature_selection : dict

    Returns
    -------
    dict
    """

    # -------------------------------------------------
    # Step 1
    # Collect Evidence
    # -------------------------------------------------

    evidence = collect_evidence(

        schema,

        missing_values,

        duplicates,

        outliers,

        correlation,

        feature_selection

    )

    # -------------------------------------------------
    # Step 2
    # Apply Rules
    # -------------------------------------------------

    decisions = apply_rules(
        evidence
    )

    # -------------------------------------------------
    # Step 3
    # Generate Stories
    # -------------------------------------------------

    stories = generate_story(
        decisions
    )

    # -------------------------------------------------
    # Step 4
    # Prioritize
    # -------------------------------------------------

    dashboard = build_dashboard(
        stories
    )

    # -------------------------------------------------
    # Step 5
    # Dataset Health
    # -------------------------------------------------

    health = calculate_health(
        stories
    )

    # -------------------------------------------------
    # Final Response
    # -------------------------------------------------

    return {

        "health": health,

        "dashboard": dashboard,

        "stories": stories,

        "decisions": decisions,

        "evidence": evidence

    }