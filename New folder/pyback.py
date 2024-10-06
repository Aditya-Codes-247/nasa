from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

# Pool of questions
quiz_data = [
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Mars"},
    {"question": "How many moons does Earth have?", "options": ["1", "2", "3", "4"], "answer": "1"},
    {"question": "Which planet is the largest in our solar system?", "options": ["Earth", "Jupiter", "Saturn", "Neptune"], "answer": "Jupiter"},
    {"question": "What is the name of Earth's satellite?", "options": ["Moon", "Io", "Titan", "Europa"], "answer": "Moon"},
    {"question": "Which planet is closest to the Sun?", "options": ["Venus", "Mercury", "Mars", "Earth"], "answer": "Mercury"},
    {"question": "What is the largest volcano in the solar system?", "options": ["Mauna Kea", "Olympus Mons", "Mount Everest", "Vesuvius"], "answer": "Olympus Mons"},
    {"question": "What planet has the most rings?", "options": ["Earth", "Jupiter", "Saturn", "Neptune"], "answer": "Saturn"},
    {"question": "Which planet is known as the Morning Star?", "options": ["Mars", "Venus", "Jupiter", "Saturn"], "answer": "Venus"},
    {"question": "How long is one year on Mercury?", "options": ["88 Earth days", "365 Earth days", "225 Earth days", "687 Earth days"], "answer": "88 Earth days"},
    {"question": "What is the smallest planet in the solar system?", "options": ["Mars", "Venus", "Mercury", "Earth"], "answer": "Mercury"},
]

class Question(BaseModel):
    question: str
    options: list
    answer: str

@app.get("/questions", response_model=list[Question])
def get_questions():
    return random.sample(quiz_data, 5)  # Get 5 random questions
