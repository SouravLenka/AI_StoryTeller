from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.captioner import get_captioner
from app.storyteller import get_storyteller
from app.schemas import StoryResponse
from app.utils import validate_image_extension, ensure_directory
from typing import Optional
import shutil
import os
import uuid
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

# Ensure uploads directory exists
UPLOAD_DIR = "uploads"
ensure_directory(UPLOAD_DIR)

@router.post("/generate-story", response_model=StoryResponse)
async def generate_story_endpoint(
    image: UploadFile = File(...),
    genre: Optional[str] = Form(None),
    mood: Optional[str] = Form(None)
):
    """
    Endpoint to upload an image and receive a generated story.
    """
    # 1. Validate file extension
    ext = validate_image_extension(image.filename)

    # 2. Save file temporarily
    file_id = str(uuid.uuid4())
    temp_file_path = os.path.join(UPLOAD_DIR, f"{file_id}.{ext}")
    
    try:
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        
        # 3. Generate caption
        captioner = get_captioner()
        caption = captioner.generate_caption(temp_file_path)

        # 4. Generate story
        storyteller = get_storyteller()
        story = storyteller.generate_story(caption, genre, mood)

        return StoryResponse(image_caption=caption, generated_story=story)

    except Exception as e:
        logger.error(f"Error in story generation pipeline: {e}")
        # Expose the error for debugging
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

    
    finally:
        # Clean up temporary file
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

