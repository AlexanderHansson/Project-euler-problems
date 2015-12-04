#coding:utf-8
#Author Alexander Hansson
#Version 2015-12-04


def main():
	"""main method"""
	while(True):
		num = int(raw_input("enter a number"))
		print find_largest_palindrome(num)


def find_largest_palindrome(num):
	"""
	A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
	Find the largest palindrome made from the product of two 3-digit numbers.
	"""
	roof = 0
	for i in range(num):
		roof+=9*(10**i)
	all_palindromes = []
	for outer in range(roof,10**(num-1)-1,-1):
		for inner in range(roof,10**(num-1)-1,-1):
			if(is_palindrome(outer*inner)):
				all_palindromes.append(outer*inner)	
	#Now we have a list of all palindromes, time to find the biggest in the list
	biggest = 0
	for number in all_palindromes:
		if number > biggest:
			biggest = number
	return biggest

def is_palindrome(number):
	"""checks if a number is a palindrome"""
	parts = __divide_number(number)
	firsthalf = parts[0]
	secondhalf = __flip_number(parts[1])
	if (firsthalf == secondhalf):
		return True
	else:
		return False

def int_length(number):
	"""calculates number of digits in a number"""
	len = 0
	while(number!=0):
		len+=1
		number/=10
	return len
				
def __flip_number(number):
	"""flips a number, 123 = 321"""
	newnumber = 0
	i = 0
	length = int_length(number)
	while(number!=0):
		newnumber+=(10**(length-i-1))*(number%10)
		number/=10
		i+=1
	return newnumber

def __divide_number(number):
	"""divides a number in two parts, 123456 returns (123,456)"""
	firsthalf = number
	secondhalf = 0
	length = int_length(number)
	if length%2 == 0:#length is even
		looprange = length/2
	else:
		looprange = length/2+1
	for i in range(0,looprange):
		secondhalf+=(10**i)*(firsthalf%10)
		firsthalf/=10
	firsthalf=number/(10**(length/2))
	while(firsthalf%10==0):
		firsthalf/=10
	return (firsthalf,secondhalf)
	
main()