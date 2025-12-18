import os
from fastapi import UploadFile


async def save_uploaded_file(
    file: UploadFile,
    upload_dir: str,
    filename: str
) -> str:
    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, filename)

    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)

    return file_path
