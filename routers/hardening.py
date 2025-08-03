# routers/hardening.py
from fastapi import APIRouter, Depends, Request, Header
from pydantic import BaseModel
from slowapi import Limiter
from slowapi.util import get_remote_address
import pyotp
import itsdangerous

router = APIRouter(prefix="/hardening", tags=["2. API Hardening"])
limiter = Limiter(key_func=get_remote_address)

# Mock user database for 2FA secrets
MOCK_USER_2FA_SECRETS = {"user123": pyotp.random_base32()}

# Secret key for signing CAPTCHA tokens
CAPTCHA_SIGNER = itsdangerous.TimestampSigner("super-secret-key-for-captcha")

class TokenVerification(BaseModel):
    token: str

@router.get("/rate-limited-endpoint", summary="Demonstrates Rate Limiting")
@limiter.limit("5/minute")
async def get_rate_limited_data(request: Request):
    """This endpoint is rate-limited to 5 requests per minute per IP."""
    return {"message": "If you see this, your request was not rate-limited."}

@router.get("/2fa/setup", summary="Generates a 2FA secret for a mock user")
async def setup_2fa():
    """Generates a secret key and provisioning URI for a mock user."""
    user_id = "user123"
    secret = MOCK_USER_2FA_SECRETS[user_id]
    provisioning_uri = pyotp.totp.TOTP(secret).provisioning_uri(
        name="user@aiguard.com", issuer_name="AI Guard"
    )
    return {
        "user_id": user_id,
        "secret_key": secret,
        "provisioning_uri": provisioning_uri,
        "message": "Scan the URI with your authenticator app (e.g., Google Authenticator)."
    }

@router.post("/2fa/verify", summary="Verifies a 2FA TOTP token")
async def verify_2fa(payload: TokenVerification):
    """Verifies a Time-based One-Time Password (TOTP)."""
    user_id = "user123"
    secret = MOCK_USER_2FA_SECRETS[user_id]
    totp = pyotp.TOTP(secret)
    is_valid = totp.verify(payload.token)
    if is_valid:
        return {"status": "success", "message": "2FA token is valid."}
    return {"status": "failure", "message": "Invalid 2FA token."}

@router.post("/captcha/verify", summary="Simulates CAPTCHA verification")
async def verify_captcha(payload: TokenVerification):
    """Verifies a signed token from the frontend to simulate a CAPTCHA."""
    try:
        # Check if token is valid and not older than 2 minutes
        CAPTCHA_SIGNER.unsign(payload.token, max_age=120)
        return {"status": "success", "message": "CAPTCHA passed!"}
    except itsdangerous.SignatureExpired:
        return {"status": "failure", "message": "CAPTCHA token expired."}
    except itsdangerous.BadSignature:
        return {"status": "failure", "message": "Invalid CAPTCHA token."}