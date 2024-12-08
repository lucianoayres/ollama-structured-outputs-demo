from typing import List
from ollama import chat
from pydantic import BaseModel, ValidationError
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Book(BaseModel):
    """
    Represents the structure of a Book with title, author, genres, and published year.
    """
    title: str
    author: str
    genres: List[str]
    published_year: int


def main():
    """
    Fetches details about the book "1984" by George Orwell using the Ollama chat service
    and validates the response using Pydantic.
    """
    try:
        response = chat(
            messages=[
                {
                    'role': 'user',
                    'content': 'Can you provide details about "1984" by George Orwell?'
                }
            ],
            model='llama3.2',
            format=Book.model_json_schema(),
        )

        book = Book.model_validate_json(response.message.content)

        print("Book Information:")
        print(book)

    except ValidationError as ve:
        logger.error(f"Validation Error: {ve}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
