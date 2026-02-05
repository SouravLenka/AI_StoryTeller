import os
import google.generativeai as genai
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class StoryTeller:
    def __init__(self):
        """
        Initializes the Gemini model using the API key from environment variables.
        """
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            logger.error("GEMINI_API_KEY not found in environment variables.")
            raise ValueError("GEMINI_API_KEY not found.")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        logger.info("Gemini AI StoryTeller initialized with gemini-2.0-flash.")


    def generate_story(self, caption: str, genre: str = None, mood: str = None) -> str:
        """
        Generates a creative story based on the image caption.
        """
        # Extra context based on optional fields
        genre_str = f"Genre: {genre}\n" if genre else ""
        mood_str = f"Mood: {mood}\n" if mood else ""

        prompt = f"""You are a creative storyteller.
Using ONLY the information from the image description below, write a vivid and engaging short story.
Do not introduce objects, characters, or events that are not implied by the image.
Focus on atmosphere, emotions, and subtle actions.

Image description:
"{caption}"

Story requirements:
- Length: 120–180 words
- Tone: cinematic and immersive
- Writing style: descriptive, natural, and human-like
- Perspective: third person
- Ending: meaningful but open-ended

Now write the story."""


        try:
            logger.info("Generating story with Gemini...")
            response = self.model.generate_content(prompt)
            
            # Check if response has candidates
            if not response.candidates:
                logger.error("Gemini returned no candidates. Safety filters might have blocked the content.")
                return "The stars were silent today. (Story generation was blocked or failed to produce a result.)"

            story = response.text.strip()
            logger.info(f"Story generated successfully: {story[:50]}...")
            return story
        except Exception as e:
            logger.error(f"Error generating story: {e}")
            raise e


# Global instance to be loaded once
storyteller = None

def get_storyteller():
    global storyteller
    if storyteller is None:
        storyteller = StoryTeller()
    return storyteller
