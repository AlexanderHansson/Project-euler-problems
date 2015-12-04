#coding:utf-8
#Version 2015-12-04
#Author Alexander Hansson

def Mul35(max=1000):
	"""
	If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9, The sum of these multiples is 23.
	Find the sum of all the multiples of 3 or 5 below 1000
	"""
	listofnums = []
	#stores all nums
	for i in range(max):
		if(i%3==0 or i%5==0):
			listofnums.append(i)
	#calculates the sum
	sum = 0
	for i in listofnums:
		sum+=i
	return sum
	
#should print 23
print Mul35(10)
	
#should print answer to problem
print Mul35()

	
