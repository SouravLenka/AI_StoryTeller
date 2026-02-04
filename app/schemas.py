from pydantic import BaseModel
from typing import Optional

class StoryResponse(BaseModel):
    image_caption: str
    generated_story: str


class StoryRequest(BaseModel):
    genre: Optional[str] = None
    mood: Optional[str] = None
