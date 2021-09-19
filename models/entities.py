from typing import List, Any

from pydantic import BaseModel


class Question(BaseModel):
    id_token: str
    text: str
    answer: Any


class Quiz(BaseModel):
    id: str
    title: str
    questions: List[Question]
