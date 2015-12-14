#codeing:utf-8
#Author: Alexander Hansson
#Version 2015-12-14



"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the
right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?

All paths are 40 jumps, 20 down and 20 right.
All we need to do is to calculate 40 over 20, since it will describe how many
ways we can pick 20 ways out of 40
"""

def faculty(num):
    if num <=1:
        return 1
    else:
        return num*faculty(num-1)


print faculty(40)/(faculty(20)**2)
