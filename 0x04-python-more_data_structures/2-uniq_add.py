#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(my_list)
    count = 0
    for i in new:
        count += i
    return count
