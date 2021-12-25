import fastapi
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.main.model.models import Token
from app.main.service.auth_service import TOKEN_URL, AuthService

router = fastapi.APIRouter()


@router.post(f"/{TOKEN_URL}", response_model=Token)
def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        auth_service: AuthService = Depends(AuthService)
) -> Token:
    return auth_service.generate_new_token(form_data.username, form_data.password)


@router.post(f"/signup")
def signup(username: str, password: str, auth_service: AuthService = Depends()) -> None:
    auth_service.create_user(username, password)
