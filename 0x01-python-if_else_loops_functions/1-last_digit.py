#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_digit = int(repr(number)[-1])

if number < 0:
    l_digit = -l_digit
print("Last digit of {} is {} and is ".format(number, l_digit), end="")

if l_digit > 5:
    print(f"greater than 5")
elif l_digit == 0:
    print(f"0")
else:
    print(f"less than 6 and not 0")
