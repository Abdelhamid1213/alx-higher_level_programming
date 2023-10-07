#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        i = 0
        for elem in list:
            print('{:d}'.format(elem), end='')
            if i < len(list) - 1:
                print(end=' ')
                i += 1
        print('')
