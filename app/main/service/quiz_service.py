from typing import List

from fastapi import Depends

from app.main.model.models import Quiz, User
from app.main.repository.fake_impl.fake_repository import FakeRepository
from app.main.repository.repository import Repository


class QuizService:
    def __init__(self, repo: Repository = Depends(FakeRepository)):
        self.repo = repo
        
    def get_quiz(self, usid: int) -> Quiz:
        return self.repo.get_quiz(usid)

    def get_saved_quizzes(self, user: User) -> List[Quiz]:
        return self.repo.get_saved_quizzes(user.id)

    def get_public_quizzes(self) -> List[Quiz]:
        return self.repo.get_public_quizzes()

    def update_points(self, user_session_id: int, point_sum: int) -> None:
        return self.repo.update_points(user_session_id, point_sum)

    def update_quiz_publicity(self, user_id: int, quiz_id: int) -> None:
        return self.repo.update_quiz_publicity(user_id, quiz_id)

    def create_quiz(self, user_id: int, quiz: Quiz) -> int:
        return self.repo.create_quiz(user_id, quiz)

    def create_quiz_session(self, user_id: int, quiz_id: int) -> int:
        return self.repo.create_quiz_session(user_id, quiz_id)

    def create_user_session(self, user_id: int, session_id: int) -> int:
        return self.repo.create_user_session(user_id, session_id)
