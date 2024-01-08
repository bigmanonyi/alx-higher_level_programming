#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    new = 0
    for i in range(1, len(argv)):
        new += int(argv[i])
    print("{}".format(new))
