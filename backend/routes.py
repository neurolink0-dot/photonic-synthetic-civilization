from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class MultimodalRequest(BaseModel):
    text: str
    mode: str = "sovereign"


@router.get("/")
def home():
    return {
        "status": "ok",
        "message": "HRQ Dynasty API running"
    }


@router.get("/status")
def status():
    return {
        "status": "online",
        "engine": "HRQ Dynasty",
        "mode": "sovereign"
    }


@router.post("/engine/multimodal")
def multimodal(request: MultimodalRequest):
    return {
        "status": "ok",
        "input": request.text,
        "mode": request.mode,
        "persona": {
            "tone": "sovereign"
        },
        "response": f"HRQ Dynasty received: {request.text}"
    }
