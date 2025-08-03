# routers/response.py
from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

router = APIRouter(prefix="/response", tags=["4. Incident Response"])

def get_playbook_content():
    """Returns the static content of the AI Incident Response Playbook."""
    return """
# AI Incident Response Playbook

## 1. Introduction
This document outlines the procedures for responding to security incidents involving our AI systems. The goal is to detect, contain, eradicate, and recover from incidents efficiently while minimizing impact to users and maintaining compliance with relevant regulations.

## 2. Roles and Responsibilities

### 2.1 Incident Response Team
- **Incident Commander:** Overall lead of the response effort. Coordinates all activities and makes critical decisions.
- **Security Analyst:** Investigates the technical aspects of the incident and implements containment measures.
- **AI/ML Specialist:** Provides expertise on AI model behavior, training data, and potential vulnerabilities.
- **Communications Lead:** Manages internal and external communication, including user notifications.
- **Legal Counsel:** Advises on legal and regulatory obligations, including GDPR and PIPEDA compliance.
- **Privacy Officer:** Ensures all response actions comply with privacy regulations and policies.

### 2.2 Contact Information
**Mock Contact Tree:**
- **Security On-Call:** +1-555-123-4567 (security-oncall@example.com)
- **AI/ML Team Lead:** +1-555-234-5678 (ai-team@example.com)
- **Legal Department:** +1-555-345-6789 (legal@example.com)
- **PR Department:** +1-555-456-7890 (press@example.com)
- **Privacy Officer:** +1-555-567-8901 (privacy@example.com)

## 3. Incident Classification

| Severity | Description | Response Time | Notification |
|----------|-------------|---------------|-------------|
| **Critical** | Significant data breach, system compromise, or AI behavior causing harm | Immediate (< 1 hour) | C-Suite, Legal, affected users |
| **High** | Limited data exposure, significant AI misbehavior | < 4 hours | Department heads, potentially affected users |
| **Medium** | Minor data issues, AI performance degradation | < 24 hours | Team leads |
| **Low** | Isolated incidents with minimal impact | < 72 hours | Relevant team members |

---

## 4. Incident Response Playbooks

### 4.1 Playbook: Prompt Injection Attack
- **Detection:** 
  - Monitoring for unusual model outputs or behavior
  - User reports of unexpected or harmful responses
  - Security monitoring alerts for known injection patterns

- **Containment:** 
  - Temporarily disable affected AI service or endpoint
  - Implement emergency input filtering rules
  - Rate-limit or block source IPs of suspicious requests

- **Eradication:** 
  - Analyze the injection patterns and update input validation
  - Implement or improve prompt sanitization
  - Update model guardrails and safety measures

- **Recovery:** 
  - Deploy updated input validation and sanitization
  - Gradually restore service with enhanced monitoring
  - Document lessons learned and update security controls

- **Communication:**
  - Notify affected users if harmful content was delivered
  - Provide transparency report on the incident and remediation
  - Update documentation with new safety measures

### 4.2 Playbook: Model Evasion / Adversarial Input
- **Detection:** 
  - Monitoring for unusual output patterns or low-confidence scores
  - Pattern recognition for known evasion techniques
  - Anomaly detection in model usage patterns

- **Containment:** 
  - Rate-limit or block the source IP
  - Deploy emergency input validation rules
  - Enable enhanced logging for suspicious requests

- **Eradication:** 
  - Analyze the adversarial inputs and update detection systems
  - Patch the model or pre-processing logic
  - Implement additional security layers

- **Recovery:** 
  - Retrain or fine-tune the model with adversarial examples
  - Deploy updated model with improved robustness
  - Implement ongoing adversarial testing

- **Communication:**
  - Document the attack vector and mitigation measures
  - Share anonymized findings with security community if novel technique

### 4.3 Playbook: Data Poisoning
- **Detection:** 
  - Sudden drop in model accuracy or performance metrics
  - Drastic changes in model behavior for specific inputs
  - Anomalies in training data or unexpected model outputs

- **Containment:** 
  - Halt continuous training pipelines immediately
  - Revert to last known-good model version
  - Isolate suspicious training data

- **Eradication:** 
  - Identify the source and method of poisoned data introduction
  - Purge the malicious data from the training set
  - Review and enhance data validation processes

- **Recovery:** 
  - Retrain the model with sanitized dataset
  - Implement improved data provenance tracking
  - Enhance monitoring for future poisoning attempts

- **Communication:**
  - Notify stakeholders of performance impact and recovery timeline
  - Document incident for compliance purposes

### 4.4 Playbook: AI Impersonation / Voice Cloning
- **Detection:** 
  - Reports from users of unauthorized access
  - Multiple failed login attempts followed by a success using biometric auth
  - Unusual patterns in voice authentication requests

- **Containment:** 
  - Immediately suspend the affected accounts
  - Invalidate all active sessions
  - Enable additional authentication factors for all users

- **Eradication:** 
  - Investigate access logs to determine the scope of the breach
  - Identify the method used for voice cloning
  - Implement additional voice liveness detection

- **Recovery:** 
  - Notify affected users with clear instructions
  - Require password reset and re-enrollment of biometric data
  - Deploy enhanced liveness checks and anti-spoofing measures

- **Communication:**
  - Provide clear guidance to affected users
  - Offer identity protection services if appropriate
  - Report to relevant authorities if required by regulations

### 4.5 Playbook: Model Extraction Attack
- **Detection:** 
  - Unusual query patterns or high volume of systematic requests
  - Requests that probe decision boundaries or model parameters
  - Multiple accounts making similar structured queries

- **Containment:** 
  - Implement stricter rate limiting based on query patterns
  - Temporarily restrict API access for suspicious accounts
  - Enable additional monitoring for model extraction patterns

- **Eradication:** 
  - Analyze the extraction technique and update detection rules
  - Implement query pattern analysis to detect future attempts
  - Review and enhance API access controls

- **Recovery:** 
  - Deploy output randomization techniques
  - Implement query monitoring and anomaly detection
  - Consider model watermarking or fingerprinting

- **Communication:**
  - Update terms of service to explicitly prohibit model extraction
  - Document the incident for internal security review

## 5. Regulatory Compliance

### 5.1 GDPR Considerations
- Determine if the incident constitutes a data breach under GDPR
- Assess if personal data was compromised or exposed
- Notify relevant supervisory authority within 72 hours if required
- Prepare user notifications if high risk to rights and freedoms
- Document the breach and response actions for compliance

### 5.2 PIPEDA Considerations
- Assess if the incident involves breach of security safeguards
- Determine if there is real risk of significant harm (RROSH)
- Notify affected individuals and the Privacy Commissioner if RROSH exists
- Maintain records of all privacy breaches for compliance

## 6. Post-Incident Activities

### 6.1 Lessons Learned
- Conduct a post-incident review meeting
- Document what worked well and areas for improvement
- Update playbooks based on lessons learned
- Identify preventative measures to implement

### 6.2 Documentation
- Maintain detailed incident records for regulatory compliance
- Document technical details for future reference
- Update security controls and procedures

---
"""

@router.get("/playbook/generate", response_class=PlainTextResponse)
async def generate_playbook():
    """Generates and returns the AI Incident Response Playbook in Markdown format."""
    return get_playbook_content()

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime, timedelta
import uuid

class IncidentRequest(BaseModel):
    incident_type: str = Field(..., description="Type of incident to simulate", 
                              example="prompt_injection")
    severity: str = Field("medium", description="Incident severity level", 
                         example="high")
    description: Optional[str] = Field(None, description="Additional details about the incident",
                                    example="Unusual model behavior detected in production")

@router.post("/test/trigger-incident")
async def trigger_mock_incident(request: IncidentRequest):
    """Triggers a mock incident to test the response workflow."""
    incident_id = f"INC-MOCK-{int(1000 * __import__('time').time()) % 100000}"
    
    # Define response templates for different incident types
    incident_responses = {
        "prompt_injection": {
            "type": "prompt_injection",
            "next_steps": [
                "Analyze injection patterns in recent requests",
                "Update input validation and sanitization rules",
                "Review and enhance model guardrails",
                "Notify affected users if harmful content was delivered"
            ]
        },
        "model_evasion": {
            "type": "model_evasion",
            "next_steps": [
                "Investigate source of the attack",
                "Analyze model inputs and outputs",
                "Update detection systems for adversarial inputs",
                "Consider model retraining with adversarial examples"
            ]
        },
        "data_poisoning": {
            "type": "data_poisoning",
            "next_steps": [
                "Halt continuous training pipelines",
                "Identify source of poisoned data",
                "Purge malicious data from training sets",
                "Roll back to known-good model version"
            ]
        },
        "voice_cloning": {
            "type": "voice_cloning",
            "next_steps": [
                "Suspend affected accounts",
                "Investigate access logs for unauthorized activity",
                "Enhance voice liveness detection mechanisms",
                "Notify affected users with clear instructions"
            ]
        },
        "model_extraction": {
            "type": "model_extraction",
            "next_steps": [
                "Analyze query patterns to identify extraction technique",
                "Implement stricter rate limiting and access controls",
                "Consider output randomization or model watermarking",
                "Update terms of service to explicitly prohibit extraction"
            ]
        }
    }
    
    # Get the appropriate response template or use a default one
    incident_type = request.incident_type.lower()
    response_template = incident_responses.get(incident_type, {
        "type": incident_type,
        "next_steps": [
            "Investigate the incident",
            "Apply appropriate containment measures",
            "Document findings and update security controls",
            "Prepare incident report"
        ]
    })
    
    # Generate a timeline based on severity
    timeline = [
        {"time": "T+0m", "action": f"Alert fired: 'Potential {incident_type.replace('_', ' ').title()} Detected'"}
    ]
    
    # Adjust timeline based on severity
    if request.severity.lower() == "critical":
        timeline.extend([
            {"time": "T+5m", "action": "Auto-escalation to Incident Commander."},
            {"time": "T+10m", "action": "Security team engaged."},
            {"time": "T+15m", "action": "C-Suite notified."},
            {"time": "T+30m", "action": "Initial assessment completed."}
        ])
    elif request.severity.lower() == "high":
        timeline.extend([
            {"time": "T+5m", "action": "Auto-escalation to Incident Commander."},
            {"time": "T+15m", "action": f"Containment protocol initiated for {incident_type.replace('_', ' ')}."},
            {"time": "T+60m", "action": "Initial assessment completed."}
        ])
    else:  # medium or low
        timeline.extend([
            {"time": "T+5m", "action": "Auto-escalation to Incident Commander."},
            {"time": "T+15m", "action": f"Containment protocol initiated for {incident_type.replace('_', ' ')}."}
        ])
    
    return {
        "incident_id": incident_id,
        "status": "Mock incident triggered.",
        "severity": request.severity,
        "type": response_template["type"],
        "description": request.description,
        "timeline": timeline,
        "next_steps": response_template["next_steps"]
    }