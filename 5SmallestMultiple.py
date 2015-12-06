#coding:utf-8
#Author: Alexander Hansson
#Version: 2015-12-05

from math import sqrt,log

"""
Problem:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def smallestNumber(roof):
	"""
	All numbers below roof can be described by, or by multiples of the prime numbers n. n<roof.
	Hence we only need to look for the set of prime numbers and check how many times every prime number n 
	can be multiplyed by itself in order not to surpass the value roof:
	n*n*n*n....*n*n = n**k. where k is the largest integer such that n**k<roof
	If we find these k's for each respective prime n, we have solved the problem.
	Our answer will be the product of all factors n**k 
	"""
	ans = 1
	primes = getPrimesToRoof(roof)
	for prime in primes:
		print "Prime: " + str(prime)+ "**" + str(int(log(roof,prime)))
		ans*=(prime**int(log(roof,prime)))
	return ans


def getPrimesToRoof(roof):
	"""
	returns all prime numbers n: n<roof
	"""
	primes = []
	for number in range(2,roof+1):
		for divisor in range(2,number+1):
			if (number%divisor)==0 and (number!=divisor):
				break #wasn't a prime
			if number == divisor:
				primes.append(number)
	return primes
	
	
def __main():
	while True:
		ans = int(raw_input("Skriv in ett tal: "))
		print smallestNumber(ans)
		
__main()
					