import fastapi
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.main.model.models import Token
from app.main.service.auth_service import generate_new_token, create_user, TOKEN_URL

router = fastapi.APIRouter()


@router.post(f"/{TOKEN_URL}", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()) -> Token:
    return generate_new_token(form_data.username, form_data.password)


@router.post(f"/signup")
async def signup(username: str, password: str) -> None:
    await create_user(username, password)
