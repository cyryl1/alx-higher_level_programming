#!/usr/bin/python3

for i in range(ord('a'), ord('z') + 1):
    if i == 'q' and i == 'e':
        break
    print("{}".format(chr(i)), end="")
