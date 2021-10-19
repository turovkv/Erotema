from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.UserServiceHTTP_Postgres.database import Base
from app.UserServiceHTTP_Postgres.user_service import get_db
from app.main import api

SQLALCHEMY_DATABASE_URL_test = "postgresql://123:123@localhost:5432/QuizOnline"

engine_test = create_engine(
    SQLALCHEMY_DATABASE_URL_test
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)
Base.metadata.create_all(bind=engine_test)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


api.dependency_overrides[get_db] = override_get_db
client = TestClient(api)


def test_create_user_1():
    response = client.post(
        "/users/",
        json={"email": "a", "name": "b", "password": "c"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "a"
    assert data["name"] == "b"
    assert "id" in data
    email = data["email"]
    response = client.get(f"/users/by_email/{email}")
    assert response.status_code == 200, response.text
    data = response.json()

    assert data["email"] == "a"
    assert data["name"] == "b"


def test_create_user_2():
    response = client.post(
        "/users/",
        json={"email": "aa1", "name": "bb", "password": "cc"},
    )
    assert response.status_code == 200, response.text

    response = client.get(f"/users")
    assert response.status_code == 200, response.text
    data = response.json()[1]

    assert data["email"] == "aa1"
    assert data["name"] == "bb"
