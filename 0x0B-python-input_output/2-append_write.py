#!/usr/bin/python3
def append_write(filename="", text=""):
    with open (filename, 'a') as f:
        w_file = f.write(text)
        f.close
        return w_file
