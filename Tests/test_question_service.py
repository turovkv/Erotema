from Services.question_service import validate_id_token


def test_get_question():
    assert True


def test_validate_id_token_len():
    assert validate_id_token("a") is None
    assert validate_id_token("ab") is None
    assert validate_id_token("abc") is None
    assert validate_id_token("abcd") is not None
    assert validate_id_token("abcde") is not None


def test_validate_id_token_symbols():
    assert validate_id_token("!!!!") is None
    assert validate_id_token("????") is None
    assert validate_id_token("ab?d") is None
    assert validate_id_token("abcd") is not None
