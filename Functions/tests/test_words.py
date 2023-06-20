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

def test_letters_from_one_word_to_dict_fixture(word_toulouse, letters_toulouse_cs):
    # given: cf args    
    # when
    letter_dict = words.letters_from_one_word_to_dict(word_toulouse)
    # then
    assert letters_toulouse_cs == letter_dict


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


@pytest.mark.parametrize(
    ["dict1", "dict2", "expected_dict"] ,
    [
          ({}, {}, {}),
          ({}, {"a":1, "b":2}, {"a":1, "b":2}),
          ({"a":1, "b":2}, {}, {"a":1, "b":2}),
          ({"a":1, "b":2}, {"c":4}, {"a":1, "b":2, "c":4}),
          ({"a":1, "b":2}, {"b":4}, {"a":1, "b":6}),
          ({"a":1, "b":2}, {"a": 5, "c":4}, {"a": 6, "b":2, "c":4}),
    ],
    ids=["empty dicts", "empty dict 1", "empty dict 2", 
         "new letter", "letter already present", "letters new and already present"]
)
def test_update_dict_letters(dict1, dict2, expected_dict):
    # when
    letters = words.update_dict_letters(dict1, dict2)
    # then
    assert expected_dict == letters
    assert letters is dict1