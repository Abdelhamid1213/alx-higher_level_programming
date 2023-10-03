#!/usr/bin/python3
i = 122
while i >= 97:
    print('{:c}'.format(i if i % 2 == 0 else i-32), end='')
    i -= 1
