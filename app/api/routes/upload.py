from fastapi import APIRouter, UploadFile, File, HTTPException
from uuid import uuid4
import os

from app.services.file_service import save_uploaded_file

router = APIRouter()

UPLOAD_DIR = "uploads"

ALLOWED_EXTENSIONS = [".pdf", ".docx"]


@router.post("/upload-cv", summary="Upload de currículo (PDF ou DOCX)")
async def upload_cv(file: UploadFile = File(...)):
    filename_lower = file.filename.lower()

    if not any(filename_lower.endswith(ext) for ext in ALLOWED_EXTENSIONS):
        raise HTTPException(
            status_code=400,
            detail="Formato de arquivo não suportado. Use PDF ou DOCX."
        )

    analysis_id = str(uuid4())
    filename = f"{analysis_id}_{file.filename}"

    file_path = await save_uploaded_file(file, UPLOAD_DIR, filename)

    return {
        "analysis_id": analysis_id,
        "file_path": file_path
    }
