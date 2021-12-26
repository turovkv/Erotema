from fastapi import Depends

from app.main.repository.fake_impl.fake_repository import FakeRepository
from app.main.repository.repository import Repository


class SessionService:
    def __init__(self, repo: Repository = Depends(FakeRepository)):
        self.repo = repo

    def get_quiz_id(self, user_session_id: int) -> int:
        return self.repo.get_quiz_id_by_session(user_session_id)

    def update_points(self, user_session_id: int, point_sum: int) -> None:
        return self.repo.update_points(user_session_id, point_sum)

    def create_quiz_session(self, user_id: int, quiz_id: int) -> int:
        return self.repo.create_quiz_session(user_id, quiz_id)

    def create_user_session(self, user_id: int, quiz_session_id: int) -> int:
        return self.repo.create_user_session(user_id, quiz_session_id)

    def start_quiz_in_single_mode(self, user_id: int, quiz_id: int):
        return self.create_user_session(user_id, self.create_quiz_session(user_id, quiz_id))
