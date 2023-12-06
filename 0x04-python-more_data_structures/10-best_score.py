#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict):
        return (None)
    init_key = None
    big_value = float('-inf')
    for key, value in a_dictionary.items():
        if value > big_value:
            big_value = value
            init_key = key
    return (init_key)
