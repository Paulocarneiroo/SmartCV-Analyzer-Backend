from fastapi import APIRouter, BackgroundTasks, Body, HTTPException
from typing import List
from app.services.analysis_service import process_cv, ANALYSIS_STORE

router = APIRouter()


@router.post("/analyze/{analysis_id}", summary="Analisar currículo com base na vaga")
async def analyze_cv(
    analysis_id: str,
    file_path: str,
    job_skills: List[str] = Body(...),
    background_tasks: BackgroundTasks = None
):
    background_tasks.add_task(
        process_cv,
        analysis_id,
        file_path,
        set(job_skills)
    )

    ANALYSIS_STORE[analysis_id] = {"status": "PENDING"}

    return {
        "analysis_id": analysis_id,
        "status": "PENDING"
    }

@router.get("/analysis/{analysis_id}", summary="Consultar resultado da análise")
async def get_analysis(analysis_id: str):
    analysis = ANALYSIS_STORE.get(analysis_id)

    if not analysis:
        raise HTTPException(status_code=404, detail="Análise não encontrada")

    return {
        "analysis_id": analysis_id,
        **analysis
    }
