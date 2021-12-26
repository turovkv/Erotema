from app.deprecated.QuizServiceHTTP.Entities.entities import Question, Answer, Quiz, Game

fake_db = {
    "answer": {},
    "question": {},
    "quiz": {},
    "game": {}
}


def init_db():
    fake_db["answer"] = dict({
        "ans1": Answer(id_token="ans1", text="ans1", points=0),
        "ans2": Answer(id_token="ans2", text="ans2", points=1),
        "ans3": Answer(id_token="ans3", text="ans3", points=1),
        "ans4": Answer(id_token="ans4", text="ans4", points=0),
        "ans5": Answer(id_token="ans5", text="ans5", points=2)
    })
    fake_db["question"] = dict({
        "ques1": Question(
            id_token="ques1",
            text="ques1",
            answer_ids=["ans1", "ans2"]
        ),
        "ques2": Question(
            id_token="ques2",
            text="ques2?",
            answer_ids=["ans3", "ans4", "ans5"]
        ),
    })
    fake_db["quiz"] = dict({
        "quiz1": Quiz(
            id_token="ques1",
            text="ques1",
            question_ids=["ques1", "ques2"]
        )
    })
    fake_db["game"] = dict({
        "game1": Game(
            user_id_token="u1",
            quiz_id_token="quiz1",
            status="unseen",
            points=0
        )
    })


def get_question(id_token: str) -> Question:
    return fake_db["question"][id_token]


def add_question(question: Question):
    fake_db["question"][question.id_token] = question


def check_exists_question(id_token: str):
    if id_token in fake_db["question"]:
        return True
    else:
        return False
