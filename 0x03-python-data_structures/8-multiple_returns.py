#!/usr/bin/python3
def multiple_returns(sentence):
    char = sentence[0] if sentence else None
    length = len(sentence)
    return (length, char)
