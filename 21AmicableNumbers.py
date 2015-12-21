#coding:utf-8
#Author: Alexander Hansson
#Version: 2015-12-21

"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""

from math import sqrt


divisors = {}
amicable = []

def find_divisors(n):
	"""returns a list of all divisors of n"""
	if divisors.get(n)==None:
		div=[]
		for i in range(1,int(sqrt(n))+1):
			if n%i == 0:
				div.append(i)
				if(i!=sqrt(n) and i!=1):
					div.append(n/i)
		divisors[n] = div
	else:
		div = divisors[n]
	return div
	
	

def d(n):
	"""if n is amicable, it will be added to amicable along with its amicable number"""
	othernr = 0
	for i in find_divisors(n):
		othernr+=i
	sum = 0
	for i in find_divisors(othernr):
		sum+=i
	if sum==n and n!=othernr:
		amicable.append(n)
		amicable.append(othernr)
	
def main():
	"""Calculates the sum of all amicable numbers under 10000"""
	for i in range(1,10000):
		if i not in amicable:
			d(i)
	sum = 0
	for am in amicable:
		sum+=am
	print sum
	print amicable
	
main()