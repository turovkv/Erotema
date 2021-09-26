from Entities.entities import Question, Answer, Quiz, Game

fake_db = {
    "answer": {
      "ans1": Answer(id_token="ans1", text="ans1", points=0),
      "ans2": Answer(id_token="ans2", text="ans2", points=1),
      "ans3": Answer(id_token="ans3", text="ans3", points=1),
      "ans4": Answer(id_token="ans4", text="ans4", points=0),
    },
    "question": {
        "ques1": Question(
            id_token="ques1",
            text="ques1",
            answer_ids=["ans1", "ans2"]
        ),
        "ques2": Question(
            id_token="ques2",
            text="ques2",
            answer_ids=["ans3", "ans4"]
        ),
    },
    "quiz": {
        "quiz1": Quiz(
            id_token="ques1",
            text="ques1",
            question_ids=["ques1", "ques2"]
        )
    },
    "game": {
        "game1": Game(
            user_id_token="u1",
            quiz_id_token="quiz1",
            status="unseen",
            points=0,
        )
    }
}
