#coding:utf-8
#Author:Alexander Hansson
#Version:2015-12-28

#TODO: Refactor to python2

from math import sqrt
from itertools import product
from functools import reduce

def is_prime(num):
    """returns true if a number is a prime"""
    if num <= 1:
        return False
    for i in range(2,int(sqrt(num))+1):
        if num%i==0:
            return False
    return True
        



def countPrimes(a,b):
    """counts how many primes the function n^2 + an + b generates"""
    i=0
    while is_prime(i**2 + a*i + b):
        i+=1
    return i
    
#makes a list ab of all combinations of (-999)to(999) and (-999)to(999)
ab = list(product(range(-999,1000),range(-999,1000)))

#calculates the length for each specific combination
lengths = [countPrimes(*(a,b)) for (a,b) in ab]

#prints the a and b that corresponds to the longest number of primes    
print(reduce(lambda x,y: x*y,ab[lengths.index(max(lengths))]))

