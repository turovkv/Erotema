from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse

from app.main.service.auth_service import AuthException
from app.main.service.quiz_service import QuizException
from app.main.service.session_service import SessionException


def auth_exception_handler(request: Request, exc: AuthException):
    return JSONResponse(status_code=401, content={"message": f"Auth Error: {str(exc)}"}, )


def quiz_exception_handler(request: Request, exc: QuizException):
    return JSONResponse(status_code=400, content={"message": f"Quiz Error: {str(exc)}"}, )


def session_exception_handler(request: Request, exc: SessionException):
    return JSONResponse(status_code=400, content={"message": f"Session Error: {str(exc)}"}, )


def add_handlers(app: FastAPI):
    app.add_exception_handler(AuthException, auth_exception_handler)
    app.add_exception_handler(QuizException, quiz_exception_handler)
    app.add_exception_handler(SessionException, session_exception_handler)
