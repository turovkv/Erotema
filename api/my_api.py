import fastapi
from fastapi import HTTPException

from models.entities import Question

router = fastapi.APIRouter()


@router.get('/api/question', response_model=Question)
def get_question(id_token: str):
    print(id_token)
    if id_token == "abc":
        return Question(id_token="a", text="b", answer="c")
    else:
        raise HTTPException(status_code=404, detail="Item not found")


@router.post('/api/question')
def add_question_with_float(question: Question):
    if not isinstance(question.answer, float):
        raise HTTPException(status_code=500, detail="The answer should be float!")
    else:
        return
