#!/usr/bin/python3
def print_last_digit(number):
    number_to_str = repr(number)
    last_char = number_to_str[-1]
    last_digit = int(last_char)
    print(last_digit, end='')
    return last_digit
