#!/usrt/bin/python3
"""Write a function that
       write a file
"""
def write_file(filename="", text=""):
    """Write a function that
       write a file
    """
    with open(filename, 'w') as f:
        w_file = f.write(text)
        f.close
        return w_file
