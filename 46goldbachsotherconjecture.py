#!/usr/bin/python
#coding:utf-8
"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

"""



primes = [2]
twosquares = set([])
def is_prime(i):
    for p in primes:
        if i%p == 0:
            return False
    return True
i = 3
found = False
nextsquare = 4
squareindex = 1 
while True:
    found = False
    if i >= nextsquare:
        twosquares.add(nextsquare)
        squareindex+=1
        nextsquare = 2*squareindex**2
    if is_prime(i):
        primes.append(i)
        i+=2
    else:
        for p in primes:
            if i-p in twosquares:
                found = True
                break
        if not found:
            break
        else:
            i+=2
print i
    
        
