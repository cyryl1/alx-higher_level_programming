#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = len(sys.argv) - 1

    if argv == 0:
        print("0 arguments")
    elif argv == 1:
        print("1 argument")
    else:
        print("{} arguments".format(argv))
    for i in range(1, argv + 1):
        print("{} : {}".format(i, sys.argv[i]))
