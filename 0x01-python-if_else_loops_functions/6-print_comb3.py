#!/usr/bin/python3
#A program that prints all possible different combinations of two digits
#Two digits must be different
#Print only the smallest combination of two digits
for digit in range(0, 10):
    for digit1 in range(digit + 1, 10):
        if digit == 8 and digit1 == 9:
            print("{}{}".format(digit, digit1))
        else:
            print("{}{}".format(digit, digit1), end = ", ")

