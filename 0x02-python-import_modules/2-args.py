#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    len = len(sys.argv)
    if len ==1:
        print("{}argument:".format(len - 1))
    elif len == 2:
        print("{}argument:".format(len - 1))
    else:
        print("{}argument:".format(len - 1))
    for i in range(1, len):
        print("{}: {}".format(i, sys.argv[i]))

