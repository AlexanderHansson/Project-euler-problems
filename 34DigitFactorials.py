"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: as 1! = 1 and 2! = 2 are not sums they are not included
"""


factorials = {}
def fac(x):
    if x in factorials:
        return factorials[x]
    if x <=1:
        return 1
    return x*fac(x-1)

number = 10
while True:
    facsum = sum([fac(int(digit)) for digit in str(number)])
    if facsum == number:
        print number
    number+=1
    if number % 10**6==0:
        print "another million: {0}".format(number)
