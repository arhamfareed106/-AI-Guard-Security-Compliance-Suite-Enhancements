# routers/reporting.py
import os
import json
from fastapi import APIRouter
from fastapi.responses import FileResponse, PlainTextResponse, JSONResponse

router = APIRouter(prefix="/reports", tags=["5. Finalization & Reporting"])

@router.get("/download/{report_id}/{format}")
async def download_report(report_id: str, format: str):
    """Allows downloading of generated audit reports."""
    file_path = f"reports_data/audit_report_{report_id}.{format}"
    if os.path.exists(file_path):
        return FileResponse(path=file_path, filename=os.path.basename(file_path))
    return {"error": "File not found."}

@router.get("/summary")
async def get_dashboard_summary():
    """Compiles a summary for the main dashboard."""
    # In a real app, this would query a database. Here we simulate by reading latest files.
    audit_files = [f for f in os.listdir("reports_data") if f.endswith(".json")]
    latest_audit = {}
    if audit_files:
        latest_file_path = os.path.join("reports_data", sorted(audit_files)[-1])
        with open(latest_file_path, 'r') as f:
            latest_audit = json.load(f).get("audit_summary", {})

    # Mock scores
    readiness_score = 75 if os.path.exists("reports_data/playbook_generated.flag") else 25
    security_test_result = "Passed (with recommendations)" if os.path.exists("reports_data/test_run.flag") else "Not yet run"

    return JSONResponse({
        "audit_summary": latest_audit,
        "response_readiness_score": readiness_score,
        "security_test_results": security_test_result
    })

@router.get("/export/owasp-checklist", response_class=PlainTextResponse)
async def export_owasp_checklist():
    """Provides a downloadable OWASP API Security Top 10 checklist."""
    # Flag that this has been generated for the summary
    open("reports_data/checklist_generated.flag", "w").close()
    return """
# OWASP API Security Checklist (Top 10 - 2023)

- [ ] **API1:2023 - Broken Object Level Authorization:** Have you checked that a user can't access objects belonging to other users?
- [ ] **API2:2023 - Broken Authentication:** Are your authentication endpoints protected against brute force? Are JWT tokens validated correctly?
- [ ] **API3:2023 - Broken Object Property Level Authorization:** Are you filtering responses to only return properties the user is allowed to see?
- [ ] **API4:2023 - Unrestricted Resource Consumption:** Have you implemented rate limiting and pagination?
- [ ] **API5:2023 - Broken Function Level Authorization:** Can users access admin-only functions?
- [ ] **API6:2023 - Unrestricted Access to Sensitive Business Flows:** Are sensitive operations (e.g., password reset) protected from automated attacks?
- [ ] **API7:2023 - Server Side Request Forgery (SSRF):** Do your endpoints fetch remote resources? Is the input validated?
- [ ] **API8:2023 - Security Misconfiguration:** Is CORS configured correctly? Are unnecessary HTTP headers removed?
- [ ] **API9:2023 - Improper Inventory Management:** Are old API versions deprecated and disabled? Is all documentation up to date?
- [ ] **API10:2023 - Unsafe Consumption of APIs:** Are you validating and sanitizing data received from third-party APIs?
"""