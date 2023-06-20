import pytest

@pytest.fixture
def word_toulouse():
    return "Toulouse"

@pytest.fixture
def letters_toulouse_cs():
    return {"T":1, "o":2, "u":2, "l":1, "s":1, "e":1}