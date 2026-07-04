from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import orchestrator, finance, hr, legal, gtm

app = FastAPI(title="AutoCEO API", version="1.0.0")

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(orchestrator.router, prefix="/api/orchestrator", tags=["Orchestrator"])
app.include_router(finance.router, prefix="/api/finance", tags=["Finance"])
app.include_router(hr.router, prefix="/api/hr", tags=["HR"])
app.include_router(legal.router, prefix="/api/legal", tags=["Legal"])
app.include_router(gtm.router, prefix="/api/gtm", tags=["GTM"])

@app.get("/health")
def health_check():
    return {"status": "ok"}
