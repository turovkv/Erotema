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

    def create_user(self, username: str, hashed_password: str) -> None:
        user = self.get_user(username)
        if user is not None:
            raise Exception("This user already exists")

        fake_users_db[username] = {
            "id": len(fake_users_db),
            "username": username,
            "hashed_password": hashed_password
        }