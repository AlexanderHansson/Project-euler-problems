#coding:utf-8
#Author:Alexander Hansson
#Version 2015-12-16 03:00

from memoized import memoized
from math import ceil,sqrt
from itertools import product


"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

limit=list(range(1,28190))
@memoized
def find_div(number):
    """finds all the divisors of a number"""
    div = [1]
    for i in range(2,int(sqrt(number)+1)):
        if number % i == 0:
            div.append(i)
            if (i<sqrt(number)):
                div.append(number/i)
    return div

#stores all abundant numbers in abn
abn=[n for n in limit if n < sum(find_div(n))]


#creates a list of all sums of two abundant numbers
sums=map(lambda (x,y): x+y, product(abn, abn))
sums=list(set(sums))
sums = filter(lambda n: n<(max(limit)+1), sums)

#prints the sum of all numbers that are not sums of abuntant numbers
print sum([n for n in limit if n not in sums])

