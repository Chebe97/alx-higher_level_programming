#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5

    #addition
    print("{:d} + {:d} = {:d}".format(a, b, add(a,b)))
    #subraction
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    #multiplication
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    #division
    print("{:d} / {:d} = {:d}".format(a,b, div(a,b)))


    
