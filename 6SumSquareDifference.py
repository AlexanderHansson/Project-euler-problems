#coding:utf-8
#Author: Alexander Hansson
#Version 2015-12-05

"""
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sum(roof):
	squaresum = 0
	for i in range(1,roof+1):
		squaresum+=i**2
	sumsquare=0
	for i in range(1,roof+1):
		sumsquare+=i
	sumsquare=sumsquare**2
	return sumsquare - squaresum
print sum(100)   