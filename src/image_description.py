from typing import List, Optional, Literal
from ollama import chat
from pydantic import BaseModel, ValidationError
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ObjectDetected(BaseModel):
    """
    Represents an object detected in an image with its name, confidence level, and attributes.
    """
    name: str
    confidence: float
    attributes: str


class ImageDescription(BaseModel):
    """
    Represents the description of an image, including summary, detected objects, scene, colors, time of day, setting, and optional text content.
    """
    summary: str
    objects: List[ObjectDetected]
    scene: str
    colors: List[str]
    time_of_day: Literal['Morning', 'Afternoon', 'Evening', 'Night']
    setting: Literal['Indoor', 'Outdoor', 'Unknown']
    text_content: Optional[str] = None


def main():
    """
    Analyzes an image to describe its content using the Ollama chat service
    and validates the response using Pydantic.
    """
    try:
        image_path = './src/images/image-01.png'

        response = chat(
            model='llava',
            format=ImageDescription.model_json_schema(),
            messages=[
                {
                    'role': 'user',
                    'content': 'Analyze this image and describe what you see, including any objects, the scene, colors and any text you can detect.',
                    'images': [image_path],
                },
            ],
            options={'temperature': 0},
        )

        image_description = ImageDescription.model_validate_json(
            response.message.content)

        print("Image Description:")
        print(image_description)

    except ValidationError as ve:
        logger.error(f"Validation Error: {ve}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
