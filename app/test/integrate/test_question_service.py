import pytest

from app.deprecated.QuizServiceHTTP.Entities.entities import Question
from app.deprecated.QuizServiceHTTP.Services.question_service import add_question, get_question


class TestQuestionService:
    def test_get_and_add_1(self):
        added = Question(id_token="ques11", text="ques1", answer_ids=["ans1", "ans2"])
        correct = Question(id_token="ques11", text="ques1", answer_ids=["ans1", "ans2"])
        add_question(added)
        extracted = get_question(added.id_token)
        assert extracted.id_token == correct.id_token
        assert extracted.text == correct.text
        assert extracted.answer_ids == correct.answer_ids

    def test_get_and_add_2(self):
        added = Question(id_token="ques22", text="ques2", answer_ids=["ans3", "ans4"])
        correct = Question(id_token="ques22", text="ques2", answer_ids=["ans3", "ans4"])
        add_question(added)
        extracted = get_question(added.id_token)
        assert extracted.id_token == correct.id_token
        assert extracted.text == correct.text
        assert extracted.answer_ids == correct.answer_ids

    def test_get_and_add_3(self):
        with pytest.raises(Exception) as ex:
            add_question(Question(id_token="ques11?", text="ques11", answer_ids=["ans11", "ans11?"]))
        assert str(ex.value) == "Invalid id token"

    def test_get_and_add_4(self):
        with pytest.raises(Exception) as ex:
            add_question(Question(id_token="ques2", text="ques11", answer_ids=["ans11", "ans11"]))
        assert str(ex.value) == "Question with id ques2 already exists"
