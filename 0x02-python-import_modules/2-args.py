#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    lenth = len(argv) - 1
    if lenth < 1:
        print("{} arguments.".format(lenth))
    elif lenth == 1:
        print ("{} argumnet:".format(lenth))
    else:
        print("{} arguments:".format(lenth))
        for i in range(1, lenth):
            print("{}: {}".format(i, argv[i + 1]))
