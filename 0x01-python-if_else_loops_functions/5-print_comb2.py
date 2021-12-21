#!/usr/bin/python3
for i in range(100):
    if(i != 99):
        print("{}, ".format("%02d" % i), end="")
print("{}".format("%02d" % i))
