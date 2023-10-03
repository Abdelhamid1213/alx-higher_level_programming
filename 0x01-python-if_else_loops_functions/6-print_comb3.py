#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i, 9):
        print('{}{}'.format(i, j+1), end='')
        if (i < 8):
            print(end=', ')
print('')
