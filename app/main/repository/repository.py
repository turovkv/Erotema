from typing import List, Optional

from app.main.model.models import Quiz, User


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Repository:
    def get_user(self, username: str) -> Optional[User]:
        raise NotImplementedError()

    def get_quiz_id_by_session(self, user_session_id: int) -> int:
        raise NotImplementedError()

    def get_quiz(self, quiz_id: int) -> Quiz:
        raise NotImplementedError()

    def get_saved_quizzes(self, user_id: int) -> List[Quiz]:
        raise NotImplementedError()

    def get_public_quizzes(self) -> List[Quiz]:
        raise NotImplementedError()

    def update_points(self, user_session_id: int, point_sum: int) -> None:
        raise NotImplementedError()

    def update_quiz_publicity(self, user_id: int, quiz_id: int):
        raise NotImplementedError()

    def create_user(self, username: str, hashed_password: str) -> None:
        raise NotImplementedError()

    def create_quiz(self, user_id: int, quiz: Quiz) -> int:
        raise NotImplementedError()

    def create_quiz_session(self, user_id: int, quiz_id: int) -> int:
        raise NotImplementedError()

    def create_user_session(self, user_id: int, session_id: int) -> int:
        raise NotImplementedError()
