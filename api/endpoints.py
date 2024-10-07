from fastapi import APIRouter, Form, HTTPException, UploadFile, File
from fastapi.responses import FileResponse
from ..utils.file_operations import save_upload_file_tmp
from ..core.image_processing import process_image, process_image_url, process_image_batch
import uuid


router = APIRouter()


@router.post("/segment_single_image/")
async def segment_single_image(file: UploadFile = File(...)):
    tmp_path = await save_upload_file_tmp(file)
    print(tmp_path)
    output_path = await process_image(tmp_path, file.filename)
    return FileResponse(output_path, media_type="image/png", filename=f"processed_{file.filename}")

@router.post("/segment_ia_url/")
async def segment_image_url(image_url: str= Form(...)):
    output_path = await process_image_url(image_url)
    return FileResponse(output_path, media_type="image/png", filename="processed_url_image.png")



@router.post("/segment_batch_images/")
async def segment_batch_images(files: list[UploadFile] = File(...)):
    batch_id = uuid.uuid4()
    zip_path = await process_image_batch(files, batch_id)
    return FileResponse(zip_path, media_type="application/zip", filename=f"processed_images_{batch_id}.zip")