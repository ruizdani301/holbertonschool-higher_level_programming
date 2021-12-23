#!/usr/bin/python3
import sys
n = len(sys.argv)
n -= 1
if n == 0:
    print("{} arguments.".format(n))
else:
    print("{} arguments:".format(n))
    for i in range(1, (n+1)):
        print("{}: {}".format(i, sys.argv[i]))
