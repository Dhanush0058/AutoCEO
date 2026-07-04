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
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    DOCUSIGN_INTEGRATOR_KEY: str = os.getenv("DOCUSIGN_INTEGRATOR_KEY", "")
    DOCUSIGN_CLIENT_ID: str = os.getenv("DOCUSIGN_CLIENT_ID", "")
    DOCUSIGN_USER_ID: str = os.getenv("DOCUSIGN_USER_ID", "")
    DOCUSIGN_ACCOUNT_ID: str = os.getenv("DOCUSIGN_ACCOUNT_ID", "")


settings = Settings()
