from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from app.main.model.models import User, Token
from app.main.repository.fake_impl.fake_repository import FakeRepository
from app.main.repository.repository import Repository

SECRET_KEY = "2c647be7ab01f90aa14e78fc85b7307978676272d1e7d882812a92e8a01f2c0e"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 3
TOKEN_URL = "token"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=TOKEN_URL)


class AuthException(Exception):
    pass


class AuthService:
    def __init__(self, repo: Repository = Depends(FakeRepository)):
        self.repo = repo

    def verify_password(self, plain_password, hashed_password) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password) -> str:
        return pwd_context.hash(password)

    def authenticate_user(self, username: str, password: str) -> bool:
        user = self.repo.get_user(username)
        if not user:
            return False
        if not self.verify_password(password, user.hashed_password):
            return False
        return True

    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None) -> str:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def generate_new_token(self, username: str, password: str) -> Token:
        user = self.authenticate_user(username, password)

        if not user:
            raise AuthException("Incorrect username or password")

        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = self.create_access_token(
            data={"sub": username}, expires_delta=access_token_expires
        )
        return Token(access_token=access_token, token_type="bearer")

    def get_current_user(self, token) -> User:
        credentials_exception = AuthException("Could not validate credentials")
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception
        user = self.repo.get_user(username)
        if user is None:
            raise credentials_exception
        return user

    def create_user(self, username: str, password: str) -> None:
        self.repo.create_user(username, self.get_password_hash(password))


def get_authorised_user(
        token: str = Depends(oauth2_scheme),
        auth_service: AuthService = Depends()
) -> User:
    return auth_service.get_current_user(token)
