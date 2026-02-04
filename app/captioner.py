import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ImageCaptioner:
    def __init__(self, model_id="Salesforce/blip-image-captioning-base"):
        """
        Initializes the BLIP captioning model and processor.
        Loads the model onto GPU if available, otherwise CPU.
        """
        logger.info(f"Loading image captioning model: {model_id}...")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.processor = BlipProcessor.from_pretrained(model_id)
        self.model = BlipForConditionalGeneration.from_pretrained(model_id).to(self.device)
        logger.info(f"Model loaded successfully on {self.device}.")

    def generate_caption(self, image_path: str) -> str:
        """
        Generates a textual description of the image at the given path.
        """
        try:
            raw_image = Image.open(image_path).convert('RGB')
            # unconditional image captioning
            inputs = self.processor(raw_image, return_tensors="pt").to(self.device)

            out = self.model.generate(**inputs)
            caption = self.processor.decode(out[0], skip_special_tokens=True)
            
            logger.info(f"Generated caption: {caption}")
            return caption
        except Exception as e:
            logger.error(f"Error generating caption: {e}")
            raise e

# Global instance to be loaded once at startup
captioner = None

def get_captioner():
    global captioner
    if captioner is None:
        captioner = ImageCaptioner()
    return captioner
