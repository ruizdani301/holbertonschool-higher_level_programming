#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        new = number * (-1)
        last = new % 10
    else:
        last = number % 10
    print(last, end="")
    return last
