#!/usr/bin/python
#coding:utf-8

#Not the nicest code I've written, but also not the ugliest

"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""



fractions = []
for number in [str(x) for x in range(10,100)]:
    numerator = number
    for index,digit in enumerate(number):
        for otherdigit in [str(x) for x in range(10) if x!= digit]:
            denominators = [digit+otherdigit, otherdigit+digit]
            for denominator in denominators:
                if denominator==numerator or int(denominator)<int(numerator) or "0" in denominator:
                    continue #ignore trivial cases and cases like denominator=0
                if float(numerator)/float(denominator) == float(numerator.replace(digit,"",1))/float(otherdigit):
                    fractions.append((numerator,denominator))
#now we have all fractions, time to find the lowest common denominator of their product

denominator = 1
numerator = 1 
for frac in fractions:
    numerator*=int(frac[0])
    denominator*=int(frac[1])
#we should actually prime factorise here and find GCD, but apparently the answer is very 
#simple as the denominator is exactly a factor 100 larger than the numerator
print float(numerator)/denominator

