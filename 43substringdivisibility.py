#!/usr/bin/python
from copy import copy
primes = [0,0,2,3,5,7,11,13,17]
numbers = []

class Pandigital(object):
    def __init__(self, digits):
        self.digits = digits
    def substring(self,i1,i2):
        value = 0
        exponent = 0
        for i in range(i2,i1-1,-1):
            value+=(self.digits[i-1]*10**(exponent))
            exponent+=1
        return value
    def property(self):
        for i in range(2,9):
            if self.substring(i,i+2) % primes[i] != 0:
                    return False
        return True


def generate_pandigi(digits, depth):
    if depth == 11:
        p = Pandigital(copy(digits))
        if p.property():
            #print p.substring(1,10)
            numbers.append(p.substring(1,10))
        return digits
    for i in [x for x in range(10) if x not in digits]:
        digits.append(i)
        digits = generate_pandigi(digits, depth+1)
        digits = digits[:-1]
    return digits

generate_pandigi([],1)
print sum(numbers)
