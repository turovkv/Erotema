from typing import List

from app.UserServiceHTTP_Postgres.model.models import Quiz


class Repository:
    def get_quiz(self, user_session_id: int) -> Quiz:
        pass

    def update_points(self, user_session_id: int, point_sum: int) -> None:
        pass

    def get_saved_quizzes(self, user_id: int) -> List[Quiz]:
        pass

    def get_public_quizzes(self) -> List[Quiz]:
        pass

    def create_quiz(self, user_id: int, quiz: Quiz) -> int:
        pass

    def update_quiz_publicity(self, user_id: int, quiz_id: int):
        pass

    def create_quiz_session(self, user_id: int, quiz_id: int) -> int:
        pass

    def create_user_session(self, user_id: int, session_id: int) -> int:
        pass
