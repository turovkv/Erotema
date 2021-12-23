import fastapi
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.main.model.models import User, Token
from app.main.service.auth_service import get_current_user, generate_new_token

router = fastapi.APIRouter()


@router.get("/a/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    return generate_new_token(form_data.username, form_data.password)
