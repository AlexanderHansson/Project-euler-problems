#!/usr/bin/python

def num_digits(num):
    num = int(num)
    i = 1
    while num >= (10**i):
        i = i + 1
        
    return i

def constant(x):
    x = int(x)
    i = 1
    num = 1
    n = num_digits(num)
    while i+n <= x:
        i+=n
        num +=1
        n = num_digits(num)
    index = x-i
    num/=(10**(num_digits(num)-index-1))
    while num>=10:
        num%=10
    return num


product = 1
i = 1
while i<=1000000:
    product*=(constant(i))
    i*=10
print product
