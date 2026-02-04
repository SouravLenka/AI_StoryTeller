from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routes import router
from app.captioner import get_captioner
from app.storyteller import get_storyteller
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Image-to-Story Generator",
    description="An AI-powered application that generates creative stories from uploaded images using BLIP and Google Gemini.",
    version="1.0.0"
)

# Include API routes
app.include_router(router)

# Mount static files
APP_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(APP_DIR, "static")
if os.path.exists(STATIC_DIR):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.on_event("startup")
async def startup_event():
    """
    Load models once at startup to optimize performance.
    """
    logger.info(f"Starting up application. Static dir: {STATIC_DIR}")
    try:
        # Pre-load captioning model
        get_captioner()
        # Pre-load storyteller
        get_storyteller()
        logger.info("All models loaded and ready.")
    except Exception as e:
        logger.error(f"Failed to load models during startup: {e}")

@app.get("/")
async def serve_ui():
    """
    Serves the simple frontend UI.
    """
    index_path = os.path.join(STATIC_DIR, "index.html")
    logger.info(f"Attempting to serve UI from: {index_path}")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {"message": "UI not found. Head over to /docs for the API docs."}


if __name__ == "__main__":

    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
