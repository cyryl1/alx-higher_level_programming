#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = len(sys.argv) - 1

if argv == 1:
    print("{} argument".format(argv))
else:
    print("{} arguments".format(argv))

for i in range(1, argv + 1):
    print("{} : {}".format(i, sys.argv[i]))
