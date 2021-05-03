#!/usr/bin/python3
if __name___ == "__main__":
    from sys import argv
    l = len(argv) - 1
    if l == 0:
        print("{:d} arguments.".format(l))
    elif l == 1:
        print("{:d} argument:".format(l))
        print("{:d}: {:s}".format(l, argv(l)))
    else:
        print("{:d} arguments :".format(l))
        for i in range(1, l+1):
            print("{:d}: {:s}".format(l, argv[i]))
