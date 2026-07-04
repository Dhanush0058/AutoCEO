from fastapi import APIRouter
from app.config import settings

router = APIRouter()


@router.post("/job-description")
async def generate_jd(title: str):
    if not settings.BAMBOOHR_API_KEY or not settings.BAMBOOHR_SUBDOMAIN:
        return {
            "title": title,
            "status": "draft_created",
            "jd": f"We are looking for a {title}...",
            "source": "demo"
        }

    return {
        "title": title,
        "status": "draft_created",
        "jd": f"We are looking for a {title}...",
        "source": "bamboohr",
        "bamboohr_configured": True
    }
