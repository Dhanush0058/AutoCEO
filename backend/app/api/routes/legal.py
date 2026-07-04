from fastapi import APIRouter
from app.config import settings

router = APIRouter()


@router.post("/contract-template")
async def generate_contract(type: str):
    if not settings.DOCUSIGN_INTEGRATOR_KEY:
        return {
            "type": type,
            "status": "template_ready",
            "content": f"STANDARD {type.upper()} AGREEMENT...",
            "source": "demo"
        }

    return {
        "type": type,
        "status": "template_ready",
        "content": f"STANDARD {type.upper()} AGREEMENT...",
        "source": "docusign",
        "docusign_configured": True
    }
