# main.py
import time
import json
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from routers import audit, hardening, testing, response, reporting

# --- Rate Limiting Setup ---
# All endpoints will be limited to 20 requests per minute per IP.
limiter = Limiter(key_func=get_remote_address)

# --- App Initialization ---
app = FastAPI(
    title="AI Guard - Security & Compliance Suite",
    description="A full-stack application for API security, compliance, and AI threat simulation.",
    version="1.0.0"
)

# --- Middleware Configuration ---
app.state.limiter = limiter

# Define a custom exception handler function
def custom_rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded):
    """Custom handler for rate limit exceeded errors. This can be customized to return a specific response."""
    return _rate_limit_exceeded_handler(request, exc)

app.add_exception_handler(RateLimitExceeded, custom_rate_limit_exceeded_handler)

# CORS (Cross-Origin Resource Sharing)
# This allows our frontend (served on a different origin during development) to talk to our backend.
origins = ["*"]  # In production, restrict this to your frontend's domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Dummy Authentication Middleware (Example) ---
@app.middleware("http")
async def dummy_auth_middleware(request: Request, call_next):
    # This is a placeholder for real authentication logic (e.g., validating a JWT Bearer token).
    # For this demo, we'll check for a simple, non-production-safe static token.
    if "Authorization" in request.headers:
        token = request.headers["Authorization"]
        # In a real app, you would decode and validate a JWT here.
        if token != "Bearer dummy-secure-token-for-demo":
            # You could return a 401 Unauthorized response here
            pass # For now, we let it pass but the logic is demonstrated.
    
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

# --- Static Files and Templates ---
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# --- Routers ---
# Include the logic from our modularized router files.
app.include_router(audit.router)
app.include_router(hardening.router)
app.include_router(testing.router)
app.include_router(response.router)
app.include_router(reporting.router)

# --- Root Endpoint ---
# This serves our main HTML page.
@app.get("/", include_in_schema=False)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})