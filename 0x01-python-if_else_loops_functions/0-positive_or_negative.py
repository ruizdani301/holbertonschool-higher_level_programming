#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(str(number) + " " + "is" + " " + "positive")
elif number < 0:
    print(str(number) + " " + "is" + " " + "negative")
else:
    print(str(0) + "is" + "zero")
