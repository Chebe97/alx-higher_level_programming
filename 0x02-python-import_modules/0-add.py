#!/usr/bin/python3
#import the def add(a, b) function
#print function with string format

if __name__ == "__main__":
    
    from add_0 import add
    a = 1
    b = 2

    print("{:d} + {:d} = {:d}".format(a, b, add(a,b)))
