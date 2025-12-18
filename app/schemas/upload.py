from pydantic import BaseModel


class UploadResponse(BaseModel):
    analysis_id: str
    filename: str
    file_path: str
