#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

ld = str(abs(number))[-1]
ld = int(ld)

if number < 0:
    ld = -ld


if ld > 5:
    print(f"Last digit of {number} is {ld} and is greater than 5")
elif ld < 6 and ld != 0:
    print(f"Last digit of {number} is {ld} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {ld} and is 0")