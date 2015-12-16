#coding:utf-8
#Author:Alexander Hansson
#Version:2015-12-17


def factorial(n):
	"""Calculates the factorial of a number"""
	if (n<=1):
		return 1
	return n*factorial(n-1)


def summarize_numbers(n):
	"""Summarizes all the numbers in a number n"""
	sum = 0
	while n>0:
		sum+=n%10
		n/=10
	return sum
	
print summarize_numbers(factorial(100))


