#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i% 3 == 0:
            print("{}".format("FIZZ"), end = " ")
        elif i % 5 == 0:
            print("{}".format("BUZZ"), end = " ")
        elif i % 3 == 0 and i % 5 == 0:
            print("{}".format("FIZZBUZZ"), end =" ")
        else:
            print("{}".format(i), end = " ")
