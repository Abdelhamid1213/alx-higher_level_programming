#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def square_list(list):
        return [x * x for x in list]
    squared_matrix = map(square_list, matrix)
    return list(squared_matrix)
