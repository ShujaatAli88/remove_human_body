from pathlib import Path
from ..config import settings
from tempfile import NamedTemporaryFile
import aiofiles
from fastapi import UploadFile

async def save_upload_file_tmp(upload_file: UploadFile) -> Path:
    try:
        suffix = Path(upload_file.filename).suffix
        with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp_path = Path(tmp.name)
        async with aiofiles.open(tmp_path, 'wb') as out_file:
            content = await upload_file.read()
            await out_file.write(content)
        return tmp_path
    finally:
        await upload_file.close()
