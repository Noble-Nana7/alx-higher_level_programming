#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

if __name__ == "__main__":

    a = 10
    b = 5

    r_add = add(a, b)
    r_minus = sub(a, b)
    r_mul = mul(a, b)
    r_div = div(a, b)

    print("{} + {} = {}".format(a, b, r_add))
    print("{} - {} = {}".format(a, b, r_minus))
    print("{} * {} = {}".format(a, b, r_mul))
    print("{} / {} = {}".format(a, b, r_div))
