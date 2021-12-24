#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div

    n = len(sys.argv)
    n = n - 1
    if n != 3:
        print('Usage: {} <a> <operator> <b>'.format(sys.argv[0]))
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operador = sys.argv[2]
    if operador == '+':
        print("{:d} + {:d} = {:d}" .format(a, b, add(a, b)))
    elif operador == '-':
        print("{:d} - {:d} = {:d}" .format(a, b, sub(a, b)))
    elif operador == '*':
        print("{:d} * {:d} = {:d}" .format(a, b, mul(a, b)))
    elif operador == '/':
        print("{:d} / {:d} = {:d}" .format(a, b, div(a, b)))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
