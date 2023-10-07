#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for elem in list:
            print('{:d}'.format(elem), end=' ')
        print('')
