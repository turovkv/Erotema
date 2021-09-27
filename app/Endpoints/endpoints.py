import fastapi
from fastapi import HTTPException

from app.Entities.entities import Question
from app.Services.question_service import get_question, add_question

router = fastapi.APIRouter()


@router.get('/question', response_model=Question)
def get_question_ep(id_token: str):
    try:
        return get_question(id_token)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e.value))


@router.post('/question')
def add_question_ep(question: Question):
    try:
        return add_question(question)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
