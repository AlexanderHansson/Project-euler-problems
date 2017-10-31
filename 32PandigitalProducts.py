#!/usr/bin/Python
#coding:utf-8
"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
"""

from itertools import permutations as permute
res=set()
numbers = "123456789"
for p in [str().join(p) for p in permute(numbers)]:
    for i in range(4,0,-1): #move * sign
        for j in range(4,i,-1): #move = sign
            if int(p[:j])*int(p[j:i+j]) == int(p[i+j:]): #check if pandigi
                res.add(int(p[i+j:])) 
print sum(res)
