# Image-to-Story Generator

A complete Python-only AI project using FastAPI and Google Gemini API to generate creative short stories based on image content.

## Features

- **FastAPI**: Modern, fast (high-performance) web framework.
- **Image Captioning**: Uses `Salesforce/blip-image-captioning-base` to describe images.
- **Story Generation**: Google Gemini AI (`gemini-1.5-flash`) writes stories based on captions.
- **Multipart Uploads**: Handles image uploads seamlessly.
- **Metadata**: Optional `genre` and `mood` fields for customized storytelling.

## Prerequisites

- Python 3.10+
- Google Gemini API Key

## Setup

1. **Clone the repository** (if applicable) or enter the project directory.

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**:
   Ensure you have a `.env` file in the root directory with your API key:
   ```env
   GEMINI_API_KEY=your_actual_api_key_here
   ```

## Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The server will be available at `http://127.0.0.1:8000`.

## API Documentation

- **Interactive Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Alternative ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Endpoint: `POST /generate-story`

**Request**:

- Type: `multipart/form-data`
- Fields:
  - `image`: The image file (jpg, jpeg, png)
  - `genre` (optional): The story genre (e.g., "Scifi", "Fantasy")
  - `mood` (optional): The story mood (e.g., "Mysterious", "Happy")

**Response**:

```json
{
  "image_caption": "a cat sitting on a table next to a computer",
  "generated_story": "The neon glow of the monitor reflected in Whiskers' eyes..."
}
```

## Project Structure

```
image_to_story_fastapi/
│
├── app/
│   ├── main.py              # FastAPI app entry
│   ├── routes.py            # API routes
│   ├── captioner.py         # Image → text logic
│   ├── storyteller.py       # Gemini story generation logic
│   ├── schemas.py           # Pydantic response models
│   ├── utils.py             # Helpers
│   └── __init__.py          # Package marker
│
├── .env                     # API keys (ignored by git)
├── .gitignore               # Git rules
├── requirements.txt         # Dependencies
└── README.md                # This file
```

## License

MIT
