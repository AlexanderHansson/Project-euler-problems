#coding:utf-8
#Author: Alexander Hansson
#Version 2015-12-06
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from math import sqrt
def sum_of_primes(roof):
	"""Finds the sum of all primes below roof"""
	#first make a list of primes
	primes = [2]
	for number in range(2,roof+1):
		for prime in primes:
			if number%prime == 0:
				break #wasn't a prime
			if prime>sqrt(number):
				primes.append(number)
				break #was a prime
		else: #if loop ends without a break
			primes.append(number)
	#now we add up all primes in the list
	sum = 0
	for prime in primes:
		sum+=prime
	return sum

print sum_of_primes(2000000)