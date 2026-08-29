from fastapi import APIRouter

router = APIRouter(prefix="/karma")

@router.get("/")
def get_karma():
    return {"status": "ok", "karma": 0}
