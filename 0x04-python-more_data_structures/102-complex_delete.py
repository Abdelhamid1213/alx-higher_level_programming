#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        tmp_dic = a_dictionary.copy()
        for key in tmp_dic.keys():
            if tmp_dic[key] == value:
                a_dictionary.pop(key)
    return a_dictionary


print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
new_dict = complex_delete(a_dictionary, 'C')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

print("--")
print("--")
new_dict = complex_delete(a_dictionary, 'c_is_fun')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)
