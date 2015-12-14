#coding:utf-8
#Author: Alexander Hansson, Lasse Heemann
#Verison: 2015-12-14

from math import sqrt

"""A triangular number is on the form 1+2+3+4+.....+n-1+n
    1 = 1
    3 = 1+2
    6 = 1+2+3
    10 = 1+2+3+4
    15 = 1+2+3+4+5
    21 = 1+2+3+4+5+6
    etc.
    We can see that 28 is the first triangle number to have over five divisors
    (1,2,4,7,14,28),
    What is the value of the first triangle number to have over fibe hundred
    divisors?
    """

def get_divisors(number):
    """returns divisors of numbers"""
    divisors=[]
    oldnumber=number
    i = 1
    while(i<=sqrt(number)):
        if oldnumber%i==0:
            divisors.append(i)
            if i!=sqrt(number):
                divisors.append(number/i)
        i+=1
    return divisors



def triangular(divisors):
    """Calculates triangular numbers"""
    i = 1
    num = 0
    derp = len(get_divisors(num))
    while derp < divisors:
        num +=i
        i+=1
        derp = len(get_divisors(num))
    return num





def main():
    print triangular(500)

main()
