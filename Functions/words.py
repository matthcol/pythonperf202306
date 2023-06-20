from typing import Dict

def letters_from_one_word_to_dict(word):
    res = {}
    for l in word:
        if l in res:
            res[l] += 1
        else:
            res[l] =1
    return res
            
def update_dict_letters(letter_dict1, letter_dict2):
    # update letter counts of letter_dict1 with letter_dict2
    for l,c in letter_dict2.items():
        if l in letter_dict1:
            letter_dict1[l] += c
        else:
            letter_dict1[l] = c
    return letter_dict1

def letters_from_word(a, *word, b, previous_res=None, **kwargs):
    """returns letters form a series of word as a set by default 
    or a dict with the number of letters
    
    Parameters:
    -----------
    - a: dummy positional argument
    - word: word1, word2, ... wordn: words to decompose
    - b: dummy keyword argument
    - previous_res: previous set or dict to accumulate with this execution
        default value: empt set or empty dict
    - kwargs: other options (cf Other Options chapter)
    
    Other Options:
    --------------
    - case: deal with letters with case sensitive or insensitive (default)
        default value: False
    - count: count letters (result is a dict) or not (result is a set)
        default value: False
    """
    #handle options options
    case_sensitive = False
    count = False
    for option_name, option_value in kwargs.items():
        match option_name:
            case "case": 
                case_sensitive = option_value
            case "count":
                count = option_value
    if previous_res is None:
        previous_res = set()
    for w in word:
        # TODO: case insensitive
        if count:
            new_letters = letters_from_one_word_to_dict(w)
            update_dict_letters(previous_res, new_letters)
        else:
            new_letters = set(w)
            previous_res.update(new_letters)
    return previous_res