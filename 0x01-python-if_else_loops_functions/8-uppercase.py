#!/usr/bin/python3

def uppercase(str):
    result = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        print("{:s}".format(i), end="")
    print()
