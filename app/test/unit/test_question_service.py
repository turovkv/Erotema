import pytest

from app.deprecated.QuizServiceHTTP.Entities.entities import Question
from app.deprecated.QuizServiceHTTP.Services.question_service import validate_id_token, validate_text, validate_question


class TestQuestionServiceValidation:
    def test_validate_id_token_len(self):
        assert not validate_id_token("a")
        assert not validate_id_token("ab")
        assert not validate_id_token("abc")
        assert validate_id_token("abcd")
        assert validate_id_token("abcde")

    def test_validate_id_token_symbols(self):
        assert not validate_id_token("!!!!")
        assert not validate_id_token("????")
        assert not validate_id_token("ab?d")
        assert validate_id_token("abcd")

    def test_validate_id_token_symbols_and_len(self):
        assert not validate_id_token("!!")
        assert not validate_id_token("??")
        assert not validate_id_token("ab")
        assert validate_id_token("1234567890alskdlaksjd")

    def test_validate_text_symbols(self):
        assert not validate_text("")
        assert not validate_text("][")
        assert not validate_text("-")
        assert validate_text("abcd")
        assert validate_text("abcde")

    def test_validate_text_symbols_2(self):
        assert not validate_text("@@@")
        assert not validate_text("  $")
        assert not validate_text("-=+")
        assert validate_text("abc d")
        assert validate_text("abc  33de")

    def test_validate_text_symbols_3(self):
        assert not validate_text("@-@")
        assert not validate_text("- $")
        assert not validate_text("-=-")
        assert validate_text("ab12c d")
        assert validate_text("abc ???!!!,,.,..,()()( 33de")

    def test_validate_question_invalid_token(self):
        with pytest.raises(Exception) as ex:
            validate_question(Question(id_token="?ques11", text="ques11", answer_ids=["ans11", "ans22"]))
        assert str(ex.value) == "Invalid id token"

    def test_validate_question_2(self):
        with pytest.raises(Exception) as ex:
            validate_question(Question(id_token="ques11", text="ques][11", answer_ids=["ans11", "ans22"]))
        assert str(ex.value) == "Invalid text"

    def test_validate_question_3(self):
        with pytest.raises(Exception) as ex:
            validate_question(Question(id_token="ques11", text="ques11", answer_ids=["ans11"]))
        assert str(ex.value) == "Invalid number of answers (1 not in [2, 6])"

    def test_validate_question_4(self):
        with pytest.raises(Exception) as ex:
            validate_question(Question(id_token="ques11", text="ques11", answer_ids=["ans11", "ans11?"]))
        assert str(ex.value) == "Invalid id token for answer (ans11?)"

    def test_validate_question_5(self):
        validate_question(Question(id_token="ques11", text="ques11", answer_ids=["ans11", "ans11"]))
