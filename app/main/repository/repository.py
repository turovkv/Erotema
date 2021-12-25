from typing import List, Optional

from app.main.model.models import Quiz, User


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Repository(metaclass=SingletonMeta):
    def get_user(self, username: str) -> Optional[User]:
        pass

    def get_quiz(self, user_session_id: int) -> Quiz:
        pass

    def get_saved_quizzes(self, user_id: int) -> List[Quiz]:
        pass

    def get_public_quizzes(self) -> List[Quiz]:
        pass

    def update_points(self, user_session_id: int, point_sum: int) -> None:
        pass

    def update_quiz_publicity(self, user_id: int, quiz_id: int):
        pass

    def create_user(self, username: str, hashed_password: str) -> None:
        pass

    def create_quiz(self, user_id: int, quiz: Quiz) -> int:
        pass

    def create_quiz_session(self, user_id: int, quiz_id: int) -> int:
        pass

    def create_user_session(self, user_id: int, session_id: int) -> int:
        pass
