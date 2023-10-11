#!/usr/bin/python3
def best_score(a_dictionary):
    best_val = 0
    best_key = None
    if a_dictionary:
        for key in a_dictionary.keys():
            if a_dictionary[key] > best_val:
                best_val = a_dictionary[key]
                best_key = key
    return best_key
