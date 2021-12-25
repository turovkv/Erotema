from typing import List

import fastapi
from fastapi import Depends

from app.main.model.models import User, Quiz
from app.main.service.auth_service import get_authorised_user
from app.main.service.quiz_service import QuizService

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
def read_users_me(user: User = Depends(get_authorised_user)):
    return user


@router.get("/quiz/join", response_model=Quiz)
def join_quiz(usid: int, user: User = Depends(get_authorised_user), quiz_service: QuizService = Depends()):
    return quiz_service.get_quiz(usid)


@router.get("/quiz/saved", response_model=List[Quiz])
def get_saved(user: User = Depends(get_authorised_user), quiz_service: QuizService = Depends()):
    return quiz_service.get_saved_quizzes(user)


@router.get("/quiz/public", response_model=List[Quiz])
def get_public_quizzes(user: User = Depends(get_authorised_user), quiz_service: QuizService = Depends()):
    return quiz_service.get_public_quizzes()
