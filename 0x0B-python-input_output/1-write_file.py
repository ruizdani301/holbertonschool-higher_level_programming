#!/usrt/bin/python3
def write_file(filename="", text=""):
    with open (filename, 'w') as f:
        w_file = f.write(text)
        f.close
        return w_file
