#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        tmp_dic = a_dictionary.copy()
        for key in tmp_dic.keys():
            if tmp_dic[key] == value:
                a_dictionary.pop(key)
    return a_dictionary
