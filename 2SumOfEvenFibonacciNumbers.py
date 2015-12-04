#coding:utf-8
#Version 2015-12-04
#Author Alexander Hansson

def __fibonacci__(roof = 4000000):
	"""returns a list of all fibonnaci numbers up to roof"""
	a = [1,1,2]
	while(a[len(a)-1] + a[len(a)-2] < roof):
		a.append(a[len(a)-2]+a[len(a)-1])
	return a

def evensum(roof = 4000000):
	"""sums up all the even numbers in a list"""
	sum = 0
	list = __fibonacci__(roof)
	print list
	for num in list:
		if num%2 == 0:
			sum+=num
	return sum
	
#prints the answer
print evensum()