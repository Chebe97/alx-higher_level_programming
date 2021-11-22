#!/usr/bin/python3

#import the def add(a, b) function
#print function with string format
# a = 1, b = 2

if __name__ == "__main__":
    
    from add_0 import add
    a = 1
    b = 2

def add(a, b):
    return a + b

print("{:d} + {:d} = {:d}".format(a, b, add(a,b)))
