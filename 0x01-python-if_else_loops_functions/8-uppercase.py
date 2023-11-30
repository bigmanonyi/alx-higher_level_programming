#!/usr/bin/python3
def uppercase(str):
    new = ""
    for i in str:
        if 'a' <= i <= 'z':
            upper_char = chr(ord(i) - 32)
        else:
            upper_char = i
        new = new + upper_char
    print("{}".format(new))
