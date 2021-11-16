#!/usr/bin/python3
#A program that prints all numbers 0 yo 98
#In decimal and hexadecimal

for number in range(0, 99):
    print(number, "=", hex(number).format(number))
