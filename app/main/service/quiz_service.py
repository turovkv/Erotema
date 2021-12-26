from typing import List

from fastapi import Depends

from app.main.model.models import Quiz, User
from app.main.repository.fake_impl.fake_repository import FakeRepository
from app.main.repository.repository import Repository


class QuizException(Exception):
    pass


class QuizService:
    def __init__(self, repo: Repository = Depends(FakeRepository)):
        self.repo = repo

    def get_quiz(self, id: int) -> Quiz:
        return self.repo.get_quiz(id)

    def get_saved_quizzes(self, user: User) -> List[Quiz]:
        return self.repo.get_saved_quizzes(user.id)

    def get_public_quizzes(self) -> List[Quiz]:
        return self.repo.get_public_quizzes()

    def update_quiz_publicity(self, user_id: int, quiz_id: int) -> None:
        return self.repo.update_quiz_publicity(user_id, quiz_id)

    def create_quiz(self, user_id: int, quiz: Quiz) -> int:
        return self.repo.create_quiz(user_id, quiz)
