from typing import List, Optional, Literal
from typing import List
from ollama import chat
from pydantic import BaseModel


class Book(BaseModel):
    title: str
    author: str
    genres: List[str]
    published_year: int


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


class Ingredient(BaseModel):
    name: str
    quantity: str
    optional: bool = False


class Recipe(BaseModel):
    name: str
    ingredients: List[Ingredient]
    steps: List[str]
    prep_time_minutes: int
    cook_time_minutes: int


response = chat(
    messages=[
        {
            'role': 'user',
            'content': '''
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
            ''',
        }
    ],
    model='llama3.2',
    format=Recipe.model_json_schema()
)

recipe = Recipe.model_validate_json(response.message.content)

print("Recipe Details:")
print(recipe)


class ObjectDetected(BaseModel):
    name: str
    confidence: float
    attributes: str


class ImageDescription(BaseModel):
    summary: str
    objects: List[ObjectDetected]
    scene: str
    colors: List[str]
    time_of_day: Literal['Morning', 'Afternoon', 'Evening', 'Night']
    setting: Literal['Indoor', 'Outdoor', 'Unknown']
    text_content: Optional[str] = None


path = './images/image-01.png'

response = chat(
    model='llava',
    format=ImageDescription.model_json_schema(),
    messages=[
        {
            'role': 'user',
            'content': 'Analyze this image and describe what you see, including any objects, the scene, colors and any text you can detect.',
            'images': [path],
        },
    ],
    options={'temperature': 0},
)

image_description = ImageDescription.model_validate_json(
    response.message.content)

print("Image Description:")
print(image_description)
