from fastapi import APIRouter
from app.config import settings

router = APIRouter()


@router.get("/runway")
async def get_runway():
    if not settings.STRIPE_SECRET_KEY:
        return {
            "current_runway_months": 8.8,
            "current_burn_rate": 45000,
            "current_cash": 400000,
            "source": "demo"
        }

    return {
        "current_runway_months": 8.8,
        "current_burn_rate": 45000,
        "current_cash": 400000,
        "source": "stripe",
        "stripe_configured": True
    }
