from typing import List

from app.main.model.models import Quiz, User
from app.main.repository.fake_impl.fake_repository import FakeRepository


def get_quiz(user: User, usid: int) -> Quiz:
    return FakeRepository().get_quiz(usid)


def get_saved_quizzes(user: User) -> List[Quiz]:
    return FakeRepository().get_saved_quizzes(user.id)


def get_public_quizzes(self) -> List[Quiz]:
    return FakeRepository().get_public_quizzes()


def update_points(user_session_id: int, point_sum: int) -> None:
    return FakeRepository().update_points(user_session_id, point_sum)


def update_quiz_publicity(user_id: int, quiz_id: int):
    return FakeRepository().update_quiz_publicity(user_id, quiz_id)


def create_quiz(user_id: int, quiz: Quiz) -> int:
    return FakeRepository().create_quiz(user_id, quiz)


def create_quiz_session(user_id: int, quiz_id: int) -> int:
    return FakeRepository().create_quiz_session(user_id, quiz_id)


def create_user_session(user_id: int, session_id: int) -> int:
    return FakeRepository().create_user_session(user_id, session_id)
