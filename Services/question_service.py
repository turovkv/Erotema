import re
from typing import Optional, Match

from Entities.entities import Question
from Repositories.repositories import fake_db


def validate_id_token(id_token: str) -> Optional[Match[str]]:
    return re.match(r"^[a-zA-Z0-9]{4,}$", id_token)


def get_question(id_token: str) -> Question:
    if not validate_id_token(id_token):
        raise Exception("Invalid token")
    return fake_db["question"](id_token)



# def add_question_with_float(question: Question):
#     if not isinstance(question.answer, float):
#
#     else:
#         return
