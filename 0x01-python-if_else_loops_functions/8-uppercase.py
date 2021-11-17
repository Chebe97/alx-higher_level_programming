#!/usr/bin/python3
def islower(c):
    if ord(c) in range(97, 123):
        return True
    else:
        return False


def uppercase(str):
    str0 = ""
    for c in str:
        if islower(c):
            str0 = str0 +chr(ord(c) - 32)
        else:
            str0 = str0 + c
            print("{}".format(str0))
