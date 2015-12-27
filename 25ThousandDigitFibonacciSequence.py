#coding:utf-8
#Author: Alexander Hansson
#Version 2015-12-27

"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""


from itertools import takewhile

#generator
def fibonacci():
    lst, sndlst = 1,1
    yield 1
    yield 1
    while True:
        cur = lst + sndlst
        sndlst=lst
        lst = cur
        yield cur #jumps back here on next call

print len(list(takewhile(lambda x: x <= 10**999, fibonacci())))+1 #wtfhax