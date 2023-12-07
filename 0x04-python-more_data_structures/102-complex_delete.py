#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete_key = [key for key, v in a_dictionary.items() if v == value]
    for key in delete_key:
        del a_dictionary[key]
    return (a_dictionary)
