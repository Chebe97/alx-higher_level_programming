#!/usr/bin/python3
#A program that prints number 0 to 99
#Numbers must be followed by a , and a space
for number in range(0, 100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{0:02d}".format(number), end = ", ")
