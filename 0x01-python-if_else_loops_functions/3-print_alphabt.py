#!/usr/bin/python3
#A program that prints the ASCII alphabet in lowercase
#Except q and e

for lowercasealphabets in range(97, 123):
    if lowercasealphabets in [101, 113]:
        continue
    print(chr(lowercasealphabets), end ="".format(lowercasealphabets))
