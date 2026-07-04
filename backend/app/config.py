import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


class Settings:
    STRIPE_SECRET_KEY: str = os.getenv("STRIPE_SECRET_KEY", "")
    HUBSPOT_API_KEY: str = os.getenv("HUBSPOT_API_KEY", "")
    BAMBOOHR_API_KEY: str = os.getenv("BAMBOOHR_API_KEY", "")
    BAMBOOHR_SUBDOMAIN: str = os.getenv("BAMBOOHR_SUBDOMAIN", "")
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    SIGNNOW_API_KEY: str = os.getenv("SIGNNOW_API_KEY", "")


settings = Settings()
