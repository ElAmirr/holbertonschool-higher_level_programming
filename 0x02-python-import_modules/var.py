#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    length = len(sys.argv)
    a = sys.argv[1]
    b = sys.arg[3]
    op = sys.arg[2]
    '''if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    '''
    else:
        if sys.argv[2] not in ('+', '-', '*', '/'):
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            if sys.argv[2] == "+":
                print("{} + {} = {}".format(int(a), int(
                    b), add(int(a), int(b))))
            elif sys.argv[2] == "-":
                print("{} - {} = {}".format(int(a), int(
                    b), sub(int(a), int(b))))
            elif sys.argv[2] == "*":
                print("{} * {} = {}".format(int(a), int(
                    b), mul(int(a), int(b))))
            else:
                print("{} / {} = {}".format(int(a), int(
                    b), div(int(a), int(b))))
