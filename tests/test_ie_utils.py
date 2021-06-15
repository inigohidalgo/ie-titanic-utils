import pytest
from ie_utils import tokenize

@pytest.mark.parametrize("sentence, expected_tokens", [
    ("This is a sentence", ["This", "is", "a", "sentence"]),
    ("Another sentence.", ["Another", "sentence."])
])
def test_tokenize_returns_expected_tokens(sentence, expected_tokens):
    tokens = tokenize(sentence)
    assert tokens == expected_tokens

@pytest.mark.parametrize("sentence, expected_tokens, lower", [
    ("This is a sentence", ["This", "is", "a", "sentence"], False),
    ("This is a sentence", ["this", "is", "a", "sentence"], True)
])
def test_tokenize_returns_expected_tokens_lower(sentence, expected_tokens, lower):
    tokens = tokenize(sentence, lower=lower)
    assert tokens == expected_tokens