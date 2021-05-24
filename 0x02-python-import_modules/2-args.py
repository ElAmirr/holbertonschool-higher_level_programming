#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    print("{} argument".format(length) +
          ((":", "s:")[length > 1], "s.")[length == 0])
    for i in range(1, length + 1):
        print("{:d}: {:s}".format(i, sys.argv[i]))
