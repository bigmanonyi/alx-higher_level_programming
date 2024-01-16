#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    lenth = len(my_list) - 1
    if idx < 0:
        return my_list
    elif idx > lenth:
        return my_list
    else:
        element = my_list[idx]
        return my_list
