#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for x in sorted(a_dictionary.items()):
        print(f'{x[0]}: {x[1]}')
