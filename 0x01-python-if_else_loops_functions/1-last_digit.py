#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if last == 0:
    print("0")
elif last < 6 and last != 0:
    print("{} and is less than 6 and not 0".format(number))
else:
    print("{} and is greater than 5".format(number))
