from fastapi import APIRouter
from app.config import settings

router = APIRouter()


@router.get("/competitors")
async def get_competitors():
    if not settings.HUBSPOT_API_KEY:
        return {
            "competitors": ["CorpA", "CorpB", "CorpC"],
            "source": "demo"
        }

    return {
        "competitors": ["CorpA", "CorpB", "CorpC"],
        "source": "hubspot",
        "hubspot_configured": True
    }
