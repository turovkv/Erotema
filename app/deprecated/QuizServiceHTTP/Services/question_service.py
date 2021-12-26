import re

from app.deprecated.QuizServiceHTTP.Entities.entities import Question
from app.deprecated.QuizServiceHTTP.Repositories import repositories


def validate_id_token(id_token: str) -> bool:
    return bool(re.match(r"^[a-zA-Z0-9]{4,}$", id_token))


def validate_text(text: str) -> bool:
    return bool(re.match(r"^[a-zA-Z0-9.,!?() ]+$", text))


def validate_question(question: Question):
    if not validate_id_token(question.id_token):
        raise Exception("Invalid id token")
    if not validate_text(question.text):
        raise Exception("Invalid text")
    if not (1 < len(question.answer_ids) < 7):
        raise Exception(f"Invalid number of answers ({len(question.answer_ids)} not in [2, 6])")
    for ans_id in question.answer_ids:
        if not validate_id_token(ans_id):
            raise Exception(f"Invalid id token for answer ({ans_id})")


def get_question(id_token: str) -> Question:
    if not validate_id_token(id_token):
        raise Exception("Invalid token")
    return repositories.get_question(id_token)


def add_question(question: Question):
    validate_question(question)
    if repositories.check_exists_question(question.id_token):
        raise Exception(f"Question with id {question.id_token} already exists")
    repositories.add_question(question)
