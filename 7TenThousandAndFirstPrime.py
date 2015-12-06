#coding:utf-8
#Author: Alexander Hansson
#Version 2015-12-06


from math import sqrt
def getPrimesToRoof(numberofprime):
	"""
	By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
	What is the 10 001st prime number?
	"""
	#har optimerats som faaaan
	primes = [2]
	i = 3
	while(numberofprime>1):
		for prime in primes:
			if prime>sqrt(i):
				primes.append(i)
				numberofprime-=1
				i+=1
				break
			if (i%prime==0):
				i+=1
				break
	return primes[len(primes)-1]
	
	
print getPrimesToRoof(10001)