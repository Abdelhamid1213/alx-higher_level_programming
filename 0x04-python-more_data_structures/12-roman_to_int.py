#!/usr/bin/python3
def roman_to_int(roman_string):
    r_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i_val = 0
    for i in range(len(roman_string)):
        if i > 0 and r_val[roman_string[i]] > r_val[roman_string[i - 1]]:
            i_val += r_val[roman_string[i]] - 2 * r_val[roman_string[i - 1]]
        else:
            i_val += r_val[roman_string[i]]
    return i_val
