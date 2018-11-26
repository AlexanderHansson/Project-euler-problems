#!/usr/bin/python

import math

def num_digits(num):
    num = int(num)
    i = 1
    while num >= (10**i):
        i = i + 1
    return i

def is_pandigital(x):
    n = num_digits(x)
    x = int(x)
    num = []
    while x:
        digit = x%10
        if digit == 0 or digit>n:
            return False
        if digit in num:
            return False
        num.append(x%10)
        x = x/10

    return True

def is_prime(x):
    x = int(x)
    s = math.ceil(math.sqrt(x))
    i = 1
    while i < s:
        i = i + 1
        if x%i == 0:
            return False
    return True

i = 1
while i < 999999999:
    if is_pandigital(i) and is_prime(i):
        print i
    i+=1
print i
