#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    n = 0
    sum = 0
    for pair in my_list:
        n += pair[0] * pair[1]
        sum += pair[1]
    return (n / sum)
