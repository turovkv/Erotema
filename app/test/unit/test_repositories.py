from app.QuizServiceHTTP.Entities.entities import Question
from app.QuizServiceHTTP.Repositories.repositories import add_question, get_question, check_exists_question


class TestQuestionDao:
    def test_get_and_add_1(self):
        added = Question(id_token="ques11", text="ques11", answer_ids=["ans11", "ans22"])
        correct = Question(id_token="ques11", text="ques11", answer_ids=["ans11", "ans22"])
        add_question(added)
        extracted = get_question(added.id_token)
        assert extracted.id_token == correct.id_token
        assert extracted.text == correct.text
        assert extracted.answer_ids == correct.answer_ids

    def test_get_and_add_2(self):
        added = Question(id_token="ques22", text="ques22", answer_ids=["ans33", "ans44"])
        correct = Question(id_token="ques22", text="ques22", answer_ids=["ans33", "ans44"])
        add_question(added)
        extracted = get_question(added.id_token)
        assert extracted.id_token == correct.id_token
        assert extracted.text == correct.text
        assert extracted.answer_ids == correct.answer_ids

    def test_get_and_add_3(self):
        added = Question(id_token="ques33", text="ques33", answer_ids=["ans11", "ans22", "ans33"])
        correct = Question(id_token="ques33", text="ques33", answer_ids=["ans11", "ans22", "ans33"])
        add_question(added)
        extracted = get_question(added.id_token)
        assert extracted.id_token == correct.id_token
        assert extracted.text == correct.text
        assert extracted.answer_ids == correct.answer_ids

    def test_add_and_exists_1(self):
        add_question(Question(id_token="ques31", text="ques33", answer_ids=["ans11", "ans22", "ans33"]))
        add_question(Question(id_token="ques32", text="ques33", answer_ids=["ans11", "ans22", "ans33"]))
        add_question(Question(id_token="ques33", text="ques33", answer_ids=["ans11", "ans22", "ans33"]))
        assert check_exists_question("ques31")
        assert check_exists_question("ques32")
        assert check_exists_question("ques33")

    def test_add_and_exists_2(self):
        add_question(Question(id_token="ques31", text="ques33", answer_ids=["ans11", "ans22", "ans33"]))
        add_question(Question(id_token="ques32", text="ques33", answer_ids=["ans11", "ans22", "ans33"]))
        add_question(Question(id_token="ques33", text="ques33", answer_ids=["ans11", "ans22", "ans33"]))
        assert check_exists_question("ques31")
        assert not check_exists_question("ques322")
        assert check_exists_question("ques33")

    def test_add_and_exists_3(self):
        add_question(Question(id_token="ques31", text="ques33", answer_ids=["ans11", "ans22", "ans33"]))
        add_question(Question(id_token="ques32", text="ques33", answer_ids=["ans11", "ans22", "ans33"]))
        add_question(Question(id_token="ques33", text="ques33", answer_ids=["ans11", "ans22", "ans33"]))
        assert check_exists_question("ques31")
        assert check_exists_question("ques32")
        assert not check_exists_question("ques333")
