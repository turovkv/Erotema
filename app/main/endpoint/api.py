import fastapi
from fastapi import HTTPException, Depends

from app.main.model.models import Question, User
from app.main.service.auth_service import get_current_user

router = fastapi.APIRouter(prefix="/api")


# @router.get('/question', response_model=Question)
# def get_question_ep(id_token: str):
#     try:
#         return get_question(id_token)
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e.value))
#
#
# @router.post('/question')
# def add_question_ep(question: Question):
#     try:
#         return add_question(question)
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))


@router.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
