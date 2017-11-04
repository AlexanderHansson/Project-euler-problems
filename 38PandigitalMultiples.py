#coding:utf-8
"""
Take the number 192 and multiply it by each of 1, 2, and 3:
        192 × 1 = 192
            192 × 2 = 384
                192 × 3 = 576
                By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
                The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
                What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""




maxpandigi=123456789

def ispandigi(num):
    num = str(num)
    if not len(num)==9:
        return False
    for i in range(1,10):
        if str(i) not in num:
            return False
    return True

i = 1
while i < 10**5:
    prod = str(i)
    j = 2
    while len(prod)<10:
        prod+=str(i*j)
        if len(prod) == 9:
            if ispandigi(prod):
                print "{0}*1 + -- + {0}*{1} = {2}".format(i,j,prod)
                if int(prod) > maxpandigi:
                    maxpandigi = int(prod)
        j+=1
    i+=1

print maxpandigi
