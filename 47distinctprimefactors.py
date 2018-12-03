#!/usr/bin/python
#coding:utf-8

"""


The first two consecutive numbers to have two distinct prime factors are:

    14 = 2 × 7
    15 = 3 × 5

    The first three consecutive numbers to have three distinct prime factors are:

    644 = 2² × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19.

    Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""

consecutive = 0
primes = set()
primefacts = dict()
primefacts[1] = set()
NUM_PRIMEFACS=4
c = 2
while True:
    i = c
    factors = set()
    changed=False
    for p in primes:
        while i%p==0:
            factors.add(p)
            i/=p
            changed=True
        if changed:
            factors = factors | primefacts[i]
            break
    l  = len(factors)
    if l: 
        primefacts[c] = factors
        if l == NUM_PRIMEFACS:
            consecutive+=1
        else: consecutive = 0
        if consecutive == NUM_PRIMEFACS:
            print c-NUM_PRIMEFACS+1
            break
    else:
        primes.add(c)
        primefacts[c] = set([c])
        consecutive = 0
    
    
    c+=1
