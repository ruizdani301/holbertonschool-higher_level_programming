#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            _up = chr(ord(c) - 32)
        else:
            _up = c
        print("{:s}".format(_up), end="")
    print('')
