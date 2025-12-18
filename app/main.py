from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import upload

app = FastAPI(
    title="SmartCV Analyzer API",
    description="API para análise inteligente de currículos com NLP",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router, tags=["Upload"])


@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok"}
