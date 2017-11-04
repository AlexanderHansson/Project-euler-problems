#!/usr/bin/python

"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

"""


import math
primes = list()
circularprimes = set()

def isprime(x):    
    return x in primes

def truncprime(prime):
    global circularprimes 
    prime = str(prime)
    for i in range(1,len(prime)):
        pb = prime[:-i]
        pf = prime[i:]
        if not (isprime(int(pb)) and isprime(int(pf))):
            return False
    if int(prime)>9:
        circularprimes.add(int(prime))
        print circularprimes
        return True
    else:
        return False




number = 2
while len(circularprimes) < 11:
    root = math.sqrt(number)
    for p in primes:
        if p > root:
            primes.append(number)
            truncprime(number)
            #print primes
            break
        if number % p==0:
            break
    else:
        primes.append(number)
        truncprime(number)
    number += 1

print sum(circularprimes)
