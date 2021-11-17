#!/usr/bin/python3
def print_last_digit(number):

    if number > 0:
        ldigt = number % 10
    else:
        ldigit = -number % 10
        print("last_digit:{}".format(ldigit))
        return ldigit


