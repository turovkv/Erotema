from typing import List, Any, Tuple

from pydantic import BaseModel


class Answer(BaseModel):
    id_token: str
    text: str
    points: int


class Question(BaseModel):
    id_token: str
    text: str
    answer_ids: List[str]


class Quiz(BaseModel):
    id_token: str
    text: str
    question_ids: List[str]


class Game(BaseModel):
    user_id_token: str
    quiz_id_token: str
    status: str
    points: int
