from typing import List

import fastapi
from fastapi import Depends

from app.main.model.models import User, Quiz
from app.main.service.auth_service import get_authorised_user
from app.main.service.quiz_service import QuizService
from app.main.service.session_service import SessionService

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
def join_quiz(
        usid: int,
        user: User = Depends(get_authorised_user),
        quiz_service: QuizService = Depends(),
        session_service: SessionService = Depends()
) -> Quiz:
    return quiz_service.get_quiz(session_service.get_quiz_id(usid))


@router.get("/quiz/saved", response_model=List[Quiz])
def get_saved(user: User = Depends(get_authorised_user), quiz_service: QuizService = Depends()):
    return quiz_service.get_saved_quizzes(user)


@router.get("/quiz/public", response_model=List[Quiz])
def get_public_quizzes(user: User = Depends(get_authorised_user), quiz_service: QuizService = Depends()):
    return quiz_service.get_public_quizzes()


@router.put("/quiz/user_session/points")
def update_points(
        user_session_id: int, point_sum: int,
        user: User = Depends(get_authorised_user),
        session_service: SessionService = Depends()
) -> None:
    return session_service.update_points(user_session_id, point_sum)


@router.put("/quiz/publicity")
def update_quiz_publicity(
        quiz_id: int,
        user: User = Depends(get_authorised_user),
        quiz_service: QuizService = Depends()
) -> None:
    return quiz_service.update_quiz_publicity(user.id, quiz_id)


@router.post("/quiz")
def create_quiz(
        quiz: Quiz,
        user: User = Depends(get_authorised_user),
        quiz_service: QuizService = Depends()
) -> int:
    return quiz_service.create_quiz(user.id, quiz)


@router.post("/quiz_session")
def create_quiz_session(
        quiz_id: int,
        user: User = Depends(get_authorised_user),
        session_service: SessionService = Depends()
) -> int:
    return session_service.create_quiz_session(user.id, quiz_id)


@router.post("/user_session")
def create_user_session(
        session_id: int,
        user: User = Depends(get_authorised_user),
        session_service: SessionService = Depends()
) -> int:
    return session_service.create_user_session(user.id, session_id)


@router.post("/quiz_in_single_mode")
def join_quiz_in_single_mode(
        quiz_id: int,
        user: User = Depends(get_authorised_user),
        session_service: SessionService = Depends()
) -> int:
    return session_service.start_quiz_in_single_mode(user.id, quiz_id)
