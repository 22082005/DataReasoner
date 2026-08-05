from typing import Optional


def create_evidence(
    module: str,
    evidence_type: str,
    severity: str,
    description: str,
    evidence: dict,
    recommendation: Optional[str] = None
):
    """
    Create a standardized evidence object.

    Parameters
    ----------
    module : str
        Module that generated the evidence.

    evidence_type : str
        Type of evidence.

    severity : str
        Critical, High, Medium, Low, Informational.

    description : str
        Human-readable description.

    evidence : dict
        Supporting values.

    recommendation : str, optional
        Suggested action.

    Returns
    -------
    dict
    """

    return {

        "module": module,

        "type": evidence_type,

        "severity": severity,

        "description": description,

        "evidence": evidence,

        "recommendation": recommendation

    }