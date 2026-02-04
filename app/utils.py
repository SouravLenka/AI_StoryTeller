import os
from fastapi import HTTPException, UploadFile

def validate_image_extension(filename: str):
    """
    Validates that the uploaded file has a permitted extension.
    """
    allowed_extensions = ["jpg", "jpeg", "png"]
    ext = filename.split(".")[-1].lower()
    if ext not in allowed_extensions:
        raise HTTPException(
            status_code=400, 
            detail=f"Invalid file type. Only {', '.join(allowed_extensions)} are allowed."
        )
    return ext

def ensure_directory(directory: str):
    """
    Ensures a directory exists.
    """
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
