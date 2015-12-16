#coding:utf-8
#Author:Alexander Hansson
#Version:2015-12-16

"""
By starting at the top of the triangle below and moving to adjacent numbers (straight south or diagonally south east) on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""
#This code could be optimized with caches to handle bigger triangles
#We could also skip the hardcoding of the triangle
#All this will be done in the bigger problem 67
#Where the same algoritm is used on a much bigger triangle


pyramid = []
height = 15
def build_pyramid():
	for i in range(height):
		pyramid.append([])
	#derp hardcoding
	pyramid[0] = [75]
	pyramid[1] = [95, 64]
	pyramid[2] = [17, 47, 82]
	pyramid[3] = [18, 35, 87, 10]
	pyramid[4] = [20, 4, 82, 47, 65]
	pyramid[5] = [19, 1, 23, 75, 3, 34]
	pyramid[6] = [88, 2, 77, 73, 7, 63, 67]
	pyramid[7] = [99, 65, 4, 28, 6, 16, 70, 92]	
	pyramid[8] = [41, 41, 26, 56, 83, 40, 80, 70, 33]
	pyramid[9] = [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
	pyramid[10] = [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
	pyramid[11] = [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
	pyramid[12] = [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
	pyramid[13] = [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
	pyramid[14] = [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]

#prints the pyramid, used for debug
def __print_pyramid():
	for i in range(len(pyramid)):
		print pyramid[i]


def find_highest_path(down=0, right=0):
	"""recursively finds the longest path through the triangle"""
	#print "height: " + str(height)
	#print "down: " + str(down)
	#print "right: " + str(right)
	if (down >= height-1):
		return pyramid[down][right]
	leftc = find_highest_path(down+1, right)
	rightc = find_highest_path(down+1, right+1)
	if leftc>rightc:
		return leftc+pyramid[down][right]
	else:
		return rightc+pyramid[down][right]	
	
build_pyramid()
print find_highest_path()