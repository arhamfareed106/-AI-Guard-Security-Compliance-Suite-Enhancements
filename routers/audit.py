# routers/audit.py
from fastapi import APIRouter, Request, Body
from fastapi.responses import JSONResponse
from utils.compliance import analyze_data_flow
from utils.report_generator import generate_reports, save_report

router = APIRouter(prefix="/audit", tags=["1. Privacy Audit"])

@router.post("/analyze")
async def analyze_and_get_report(request: Request, data_flow: str = Body(..., embed=True)):
    """
    Receives data flow text, analyzes for compliance gaps, and returns results.
    """
    gaps = analyze_data_flow(data_flow)
    reports = generate_reports(gaps, data_flow)
    
    # Save reports to the server
    json_path = save_report(reports["json"], reports["id"], "json")
    md_path = save_report(reports["markdown"], reports["id"], "md")

    return JSONResponse(content={
        "message": "Analysis complete.",
        "results": json.loads(reports["json"]),
        "download_links": {
            "json": f"/reports/download/{reports['id']}/json",
            "markdown": f"/reports/download/{reports['id']}/md"
        }
    })