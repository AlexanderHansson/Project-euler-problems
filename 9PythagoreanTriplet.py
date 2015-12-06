#coding:utf-8
#Author: Alexander Hansson
#Version: 2015-12-06

from math import sqrt

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def pythagorean_triplet(sum):
	for i in range (1,sum):
		for j in range(1,sum):
			ksquare = (i**2)+(j**2)
			k = sqrt(ksquare)
			if((k-int(k)) == 0):
				ijksum = i+j+int(k) 
				print str(i) + " + " + str(j) + " + " + str(int(k)) + " sum: " + str(ijksum)
				if ijksum == sum:
					return (i,j,int(k))
				elif ijksum > sum:
					break
				
triplet = pythagorean_triplet(1000)
print triplet[0]*triplet[1]*triplet[2]
				
  