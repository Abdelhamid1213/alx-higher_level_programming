#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = set()
    sum_val = 0
    for x in my_list:
        if x not in uniq:
            uniq.add(x)
    for x in uniq:
        sum_val += x
    return sum_val
