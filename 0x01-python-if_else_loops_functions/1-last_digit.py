#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = number * -1
digit = number % 10
if digit > 5:
    print("Last digif of {:d} is {:d} and is\
 greater than 5".format(number, digit))
elif digit < 6 and digit != 0:
    print("Last digif of {:d} is {:d} and is\
 less than 6 and not 0".format(number, digit))
else:
    print("Last digif of {:d} is {:d} and is 0".format(number, digit))
