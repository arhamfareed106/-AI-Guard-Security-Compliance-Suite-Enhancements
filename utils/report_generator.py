# utils/report_generator.py
import json
from typing import List, Dict, Any
import datetime
import uuid

def generate_reports(gaps: List[Dict[str, Any]], data_flow_text: str) -> Dict[str, str]:
    """Generates JSON and Markdown reports and returns them as strings."""
    timestamp = datetime.datetime.now().isoformat()
    report_id = str(uuid.uuid4())

    # --- JSON Report ---
    json_data = {
        "report_id": report_id,
        "timestamp": timestamp,
        "audit_summary": {
            "total_gaps_found": len(gaps) if gaps[0].get('risk_level') != 'Low' else 0,
            "highest_risk_level": max([g['risk_level'] for g in gaps], key=lambda r: ["Low", "Medium", "High", "Critical"].index(r), default="Low")
        },
        "original_data_flow": data_flow_text,
        "compliance_gaps": gaps
    }
    json_report = json.dumps(json_data, indent=2)

    # --- Markdown Report ---
    md_report = f"# Privacy Audit Report\n\n"
    md_report += f"**Report ID:** `{report_id}`\n"
    md_report += f"**Date:** {timestamp}\n\n"
    md_report += f"## 1. Audited Data Flow\n\n```\n{data_flow_text}\n```\n\n"
    md_report += f"## 2. Compliance Gaps Identified\n\n"
    md_report += "| Detected Term | Risk Level | Relevant Law / Principle | Recommendation |\n"
    md_report += "|---|---|---|---|\n"
    for gap in gaps:
        md_report += f"| {gap['detected_term']} | **{gap['risk_level']}** | {gap['relevant_law']} | {gap['recommendation']} |\n"
    
    return {"json": json_report, "markdown": md_report, "id": report_id}

def save_report(report_content: str, report_id: str, format: str):
    """Saves a report string to a file."""
    filepath = f"reports_data/audit_report_{report_id}.{format}"
    with open(filepath, "w") as f:
        f.write(report_content)
    return filepath