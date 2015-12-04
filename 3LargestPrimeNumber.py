#coding:utf-8
#Version 2015-12-04
#Author Alexander Hansson
from math import sqrt

def largestPrimeFac(number):
	"""
	The prime factors of 13195 are 5, 7, 13 and 29.
	What is the largest prime factor of the number 600851475143 ?
	"""
	return __getLargestPrime(number)	


def __getLargestPrime(number,start = 2,a=[]):
		"""private recursive method to calculate the largest prime number of a number"""
		b = [] #list to contain all primes <= sqrt(number)
		if len(a) == 0: #if we are on the first recursive step
			for num in range(start,int(round(sqrt(number)))+1):
				for i in range(1,int(round(sqrt(num)))+1):
					if num%i==0 and i != 1:#if any number num: start<=num<=sqrt(number) is dividable by any number i: 1<i<sqrt(num), it is not prime
						break
					if i+1 == int(round(sqrt(num)))+1:#else, it is prime and we add it to b
						b.append(num)
		else: #if we are in any of the recursive steps
			for num in a: 
				if num <= round(sqrt(number)) and num >= start:
					b.append(num) #we only look at the previous list a of primes and add them to the b if they are relevant start<=prime<=sqrt(number)
		for num in b:
			if number%num==0: #test if number is dividable by any of the primes
				return __getLargestPrime(number/num,num,b)
		return number #when we reach this, we have reached our biggest prime factor.
			

print largestPrimeFac(600851475143)
		

			

