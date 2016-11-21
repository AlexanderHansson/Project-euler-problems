#coding:utf-8
#Author: Alexander Hansson
#Version: 2016-01-24

#This is a very shitty brute-force solution, but it solves the problem

"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""


def sum_of_powers(number):
    sum = 0
    while number>0:
        sum+=(number%10)**5
        number/=10
    return sum
    
def main():
    number = 2
    sum = 0
    numbers = []
    while True:
        if sum_of_powers(number) == number:
            numbers.append(number)
            sum+=number
        if number%1000000==0:
            print "Iteration: " + str(number)
            print "numbers:"
            for n in numbers:
                print n
            print "Sum:"
            print sum
        number+=1        
main()
