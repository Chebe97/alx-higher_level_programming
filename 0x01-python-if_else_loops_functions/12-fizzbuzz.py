#!/usr/bin/python3
#A function that prints numbers 1 to 100
#For multiples of three print Fizz
#For multiples of five print Buzz
#For multiples of three and five print FizzBuzz

def fizzbuzz():
    for fizzbuzz in range(1, 101):
        
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print("FizzBuzz ", end="")
            continue
        
        elif fizzbuzz % 3 == 0:
            print("Fizz ", end="")
            continue
        
        elif fizzbuzz % 5 == 0:
            print("Buzz ", end="")
            continue
        
        else:
            print("{} ".format(fizzbuzz), end="")

