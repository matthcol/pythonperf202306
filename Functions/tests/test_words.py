import words
import pytest

def test_letters_from_one_word_to_dict():
    # given
    word = "Toulouse"
    expected_letter_dict =  {"T":1, "o":2, "u":2, "l":1, "s":1, "e":1}
    # when
    letter_dict = words.letters_from_one_word_to_dict(word)
    # then
    assert expected_letter_dict == letter_dict


@pytest.mark.parametrize(
        # nom des parametres à injecter
        ["word", "expected_letter_dict"],
        # valeurs à injecter
        [
            ("", {}),
            ("a", {"a": 1}),
            ("aA", {"a": 1, "A": 1}),
            ("ab", {"a": 1, "b": 1}),
            ("aa", {"a": 2}),
            ("aba", {"a": 2, "b": 1}),
            ("abaabc", {"a": 3, "b": 2, "c": 1}),
        ],
        # nommer les cas
        ids=[
            "empty word",
            "word with one letter",
            "word case sensitive",
            "word with 2 letters",
            "word with letter repeated twice",
            "word aba",
            "word abaabc"
        ]
)
def test_letters_from_one_word_to_dict_all_case(word, expected_letter_dict):
    # # given
    # word = "Toulouse"
    # expected_letter_dict =  {"T":1, "o":2, "u":2, "l":1, "s":1, "e":1}
    # when
    letter_dict = words.letters_from_one_word_to_dict(word)
    # then
    assert expected_letter_dict == letter_dict