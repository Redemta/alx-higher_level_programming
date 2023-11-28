#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10
if number < 0:
    lastDigit = -lastDigit
thestr = "Last digit of {} is {}" .format(number, lastDigit)
if lastDigit > 5:
    print(f"{thestr} and is greater than 5")
elif lastDigit == 0:
    print(f"{thestr} and is 0")
else:
    print(f"{thestr} and is less than 6 and not 0")
