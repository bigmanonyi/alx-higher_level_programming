#!/usr/bin/env python3
def remove_char_at(str, n):
    new = ""
    b = 0
    for char in str:
        if b != n:
            new += str[b]
        b += 1
    return (new)
