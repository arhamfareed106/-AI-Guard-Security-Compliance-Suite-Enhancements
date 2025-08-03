# utils/compliance.py
import re
from typing import List, Dict, Any

# Keywords to detect potential PII (Personal Identifiable Information)
GDPR_PII_KEYWORDS = {
    "name": {"risk": "High", "law": "GDPR Art. 4(1)", "mitigation": "Anonymize or pseudonymize if not essential. Ensure lawful basis for processing."},
    "email": {"risk": "High", "law": "GDPR Art. 4(1)", "mitigation": "Encrypt at rest and in transit. Obtain explicit consent for marketing communications."},
    "phone": {"risk": "High", "law": "GDPR Art. 4(1)", "mitigation": "Mask parts of the number where possible. Justify collection purpose."},
    "address": {"risk": "High", "law": "GDPR Art. 4(1)", "mitigation": "Collect only necessary components (e.g., country, not full street address)."},
    "ip address": {"risk": "Medium", "law": "GDPR Recital 30", "mitigation": "Store for minimal duration. Consider storing anonymized versions."},
    "ssn": {"risk": "Critical", "law": "GDPR Art. 9", "mitigation": "Avoid collecting unless legally required. Requires highest level of security."},
    "social security number": {"risk": "Critical", "law": "GDPR Art. 9", "mitigation": "Avoid collecting unless legally required. Requires highest level of security."},
    "health data": {"risk": "Critical", "law": "GDPR Art. 9 (Special Category)", "mitigation": "Requires explicit consent and enhanced security measures (e.g., encryption, access controls)."},
    "biometric": {"risk": "Critical", "law": "GDPR Art. 9 (Special Category)", "mitigation": "Requires explicit consent and a Data Protection Impact Assessment (DPIA)."},
}

PIPEDA_PII_KEYWORDS = {
    "age": {"risk": "Medium", "law": "PIPEDA Principle 4.3", "mitigation": "Ensure meaningful consent, especially for minors."},
    "gender": {"risk": "Medium", "law": "PIPEDA Principle 4.4", "mitigation": "Justify the need for collection (Limiting Collection)."},
    "financial information": {"risk": "High", "law": "PIPEDA Principle 4.7", "mitigation": "Implement strong safeguards (encryption, access control)."},
    "credit card": {"risk": "High", "law": "PIPEDA Principle 4.7", "mitigation": "Comply with PCI-DSS. Do not store CVV."},
}

def analyze_data_flow(text: str) -> List[Dict[str, Any]]:
    """
    Parses input text to find PII keywords and returns compliance gaps.
    """
    gaps = []
    text_lower = text.lower()
    
    combined_keywords = {**GDPR_PII_KEYWORDS, **PIPEDA_PII_KEYWORDS}

    for keyword, details in combined_keywords.items():
        if re.search(r'\b' + keyword + r'\b', text_lower):
            gaps.append({
                "detected_term": keyword,
                "risk_level": details["risk"],
                "relevant_law": details["law"],
                "recommendation": details["mitigation"],
            })
            
    if not gaps:
        gaps.append({
            "detected_term": "N/A",
            "risk_level": "Low",
            "relevant_law": "N/A",
            "recommendation": "No obvious PII keywords detected. However, a manual review is always recommended.",
        })
        
    return gaps