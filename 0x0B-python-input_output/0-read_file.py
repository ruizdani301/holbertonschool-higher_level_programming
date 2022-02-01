#!/usr/bin/python3
def read_file(filename=""):
    with open(filename) as f:
        file = f.read()
        print(file)
        f.close
