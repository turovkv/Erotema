import fastapi
from fastapi import HTTPException

from Entities.entities import Question
from Services.question_service import get_question

router = fastapi.APIRouter()


@router.get('/Endpoints/question', response_model=Question)
def get_question_ep(id_token: str):
    try:
        return get_question(id_token)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post('/Endpoints/question')
def add_question_with_float_ep(question: Question):
    if not isinstance(question.answer, float):
        raise HTTPException(status_code=500, detail="The answer should be float!")
    else:
        return
