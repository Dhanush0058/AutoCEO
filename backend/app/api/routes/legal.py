from fastapi import APIRouter
from app.config import settings

router = APIRouter()

@router.post("/contract-template")
async def generate_contract(type: str):
    if not settings.SIGNNOW_API_KEY:
        return {
            "type": type,
            "status": "ready_for_signing",
            "message": "SignNow key not configured"
        }

    return {
        "type": type,
        "status": "ready_for_signing",
        "message": "SignNow integration ready",
        "signnow_configured": True
    }