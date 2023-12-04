#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    length = len(sentence)
    char_one = sentence[0]
    return (length, char_one)
