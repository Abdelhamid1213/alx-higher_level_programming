#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number[-1] < 6:
    print(f'Last digit of {number} is {number[-1]} and is less than 6 and not 0')
elif number[-1] > 6:
    print(f'Last digit of {number} is {number[-1]} and is greater than 6 and not 0')
else:
    print(f'Last digit of {number} is {number[-1]} and is 0')
