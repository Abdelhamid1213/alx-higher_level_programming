#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """Create a pascal triangle list"""
    if n <= 0:
        return []
    list = []
    for a in range(n):
        sub_list = []
        while a > 0:
            sub_list.append(a)
            a -= 1
        list.append(sub_list)
    return list
