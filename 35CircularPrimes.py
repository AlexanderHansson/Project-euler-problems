#!/usr/bin/python

"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?

"""


import math


def isprime(x):
    #this stupid function is needed for numbers between one million and ten million
    #could probably be made faster with the same algorithm as below
    root = math.sqrt(x)
    for i in range(2,int(root)+1):
        if x%i==0:
            return False
    return True
        



#generate all primes below a million
primes = set()
for number in range(2,1000000):
    root = math.sqrt(number)
    for prime in primes:
        if prime>root:
            primes.add(str(number))
            break
        if number%prime==0:
            break
    else:
        primes.add(str(number))


circularprimes=set()
while len(primes)>0:
    prime = primes.pop()
    subset=set()
    for i in range(len(prime)):
        prime = prime[1:] + prime[0]
        subset.add(prime)
        if not isprime(int(prime)):
            break
    else:
        circularprimes |= subset
    for s in subset:
        try:
            primes.remove(s)
        except:
            pass

print len([x for x in circularprimes if int(x)<1000000])

