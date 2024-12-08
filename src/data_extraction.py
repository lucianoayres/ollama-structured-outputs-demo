from typing import List
from ollama import chat
from pydantic import BaseModel, ValidationError
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Ingredient(BaseModel):
    """
    Represents an ingredient with a name, quantity, and an optional flag.
    """
    name: str
    quantity: str
    optional: bool = False


class Recipe(BaseModel):
    """
    Represents a Recipe with a name, list of ingredients, steps, and preparation/cooking times.
    """
    name: str
    ingredients: List[Ingredient]
    steps: List[str]
    prep_time_minutes: int
    cook_time_minutes: int


def main():
    """
    Generates a detailed spaghetti carbonara recipe using the Ollama chat service
    and validates the response using Pydantic.
    """
    try:
        recipe_instructions = '''
            I want to make spaghetti carbonara.
            Ingredients:
            - 200g spaghetti
            - 100g pancetta
            - 2 large eggs
            - 50g Pecorino cheese
            - 50g Parmesan
            - Freshly ground black pepper
            - Salt
            Instructions:
            1. Cook the spaghetti.
            2. Fry the pancetta.
            3. Beat the eggs and mix with cheese.
            4. Combine everything together with spaghetti.
        '''

        response = chat(
            messages=[
                {
                    'role': 'user',
                    'content': recipe_instructions,
                }
            ],
            model='llama3.2',
            format=Recipe.model_json_schema()
        )

        recipe = Recipe.model_validate_json(response.message.content)

        print("Recipe Details:")
        print(recipe)

    except ValidationError as ve:
        logger.error(f"Validation Error: {ve}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
