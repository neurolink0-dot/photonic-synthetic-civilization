from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from .routes import router
from .api_karma import router as karma_router
from .api_dashboard import router as dashboard_router
import os

app = FastAPI(title="HRQ Dynasty", version="1.0.0")

app.include_router(router)
app.include_router(karma_router)
app.include_router(dashboard_router)

# Mount static files for frontend
try:
    app.mount("/static", StaticFiles(directory="static"), name="static")
except Exception:
    pass  # static directory optional

# Serve dashboard at root
@app.get("/")
async def root():
    """Redirect to dashboard"""
    static_path = os.path.join(os.path.dirname(__file__), "../static/dashboard.html")
    if os.path.exists(static_path):
        return FileResponse(static_path)
    return {
        "status": "ok",
        "message": "HRQ Dynasty API running",
        "dashboard": "/static/dashboard.html"
    }
