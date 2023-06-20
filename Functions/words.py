from typing import Dict, Set, Union, Optional, cast

def letters_from_one_word_to_dict(word: str) -> Dict[str,int]:
    res: Dict[str,int] = {}
    for l in word:
        if l in res:
            res[l] += 1
        else:
            res[l] = 1
    return res
            
def update_dict_letters(
        letter_dict1: Dict[str,int], 
        letter_dict2: Dict[str,int]
) -> Dict[str,int]:
    # update letter counts of letter_dict1 with letter_dict2
    for l,c in letter_dict2.items():
        if l in letter_dict1:
            letter_dict1[l] += c
        else:
            letter_dict1[l] = c
    return letter_dict1

def letters_from_word(
        a, 
        *word: str, 
        b, 
        # previous_res: Optional[Union[Set[str], Dict[str,int]]] = None, 
        previous_res: set[str] | dict[str,int] | None = None, 
        **kwargs):
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
    if count:
        if previous_res is None:
            previous_res_dict: dict[str,int] = {}
        else:
            # dynamic typing
            assert isinstance(previous_res, dict)
            # static typing
            previous_res_dict = cast(dict[str,int], previous_res)
        for w in word:
            # TODO: case insensitive
            new_letters_dict = letters_from_one_word_to_dict(w)
            update_dict_letters(previous_res_dict, new_letters_dict)
        return previous_res_dict
    else:
        if previous_res is None:
            previous_res_set: set[str] = set()
        else:
            # dynamic typing
            assert isinstance(previous_res, set)
            # static typing
            previous_res_set = cast(set[str], previous_res)
        for w in word:
            # TODO: case insensitive
            new_letters_set = set(w)
            previous_res_set.update(new_letters_set)
        return previous_res_set
   
if __name__ == '__main__':
    # good call
    a = letters_from_one_word_to_dict("toulouse")
   
    # wrong call: mypy can detect that
    # error: Argument 1 to "letters_from_one_word_to_dict" has incompatible type "int"; expected "str"
    # b = letters_from_one_word_to_dict(123)

    c = update_dict_letters({"a": 2, "b": 3}, {"b": 4, "c": 1})
    update_dict_letters(c, {"c": 5, "d": 1})

    # wrong call detected by mypy
    # update_dict_letters(c, 
    #         {
    #             "a": "lundi", # dynamic error
    #             3: 5          # weird result
    #         })
    print(c)

    e = letters_from_word(1, "Toulouse", "Lyon", "Paris", b=2)
    f = letters_from_word(1, "Toulouse", "Lyon", "Paris", b=2, 
                      previous_res={"a": 1}, count=True)
    g = letters_from_word(1, "Toulouse", "Lyon", "Paris", b=2, 
                      previous_res={"a"})
    
    # wrong call: how to detect it ?
    #    - with Hints: not possible, indeterminsm with "if count"
    #    - duck typing: discover error dynamically
    #    - dynamic typing: assert or test type of parameters
    # h = letters_from_word(1, "Toulouse", "Lyon", "Paris", b=2, 
    #                   previous_res={"a"}, count=True)
    i = letters_from_word(1, "Toulouse", "Lyon", "Paris", b=2, 
                      previous_res={"a": 1}, count=False)
