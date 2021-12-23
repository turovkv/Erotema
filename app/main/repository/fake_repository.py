from typing import Optional

from app.main.model.models import User
from app.main.repository.repository import Repository

fake_users_db = {
    "johndoe": {
        "id": 1,
        "username": "johndoe",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW" # 'secret'
    }
}


class FakeRepository(Repository):
    def get_user(self, username: str) -> Optional[User]:
        if username in fake_users_db:
            return User(**fake_users_db[username])
        return None


rep = None


def get_repo() -> Repository:
    global rep
    if rep is None:
        rep = FakeRepository()
    return rep
