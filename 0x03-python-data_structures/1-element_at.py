#!/usr/bin/python3
def element_at(my_list, idx):
    if (idx < 0) + (idx + 1  > len(my_list)):
        return None
    else:
        return my_list[idx]
