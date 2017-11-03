#!/usr/bin/python

"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def doublepalindrome(string):
    for loops in range(2):
        for i in range(len(string)/2):
            if string[i] != string[-(i+1)]:
                return False
        string = int(string)
        binstring = bin(string)[2:]
        if "1" in binstring:
            binstring[binstring.index("1"):]
        string = binstring
    #now we know it is a palindrome in both bases


    return True


palins = [(number,bin(number)[2:]) for number in range(10**6) if doublepalindrome(str(number))]
for pal in palins:
    print pal
print sum([x[0] for x in palins])

