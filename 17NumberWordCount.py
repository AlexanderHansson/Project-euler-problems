#coding:utf-8
#Author: Alexander Hansson
#Version 2015-12-15


"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
"""

words = {}
#some initial hardcoding
words[1] = "one"
words[2] = "two"
words[3] = "three"
words[4] = "four"
words[5] = "five"
words[6] = "six"
words[7] = "seven"
words[8] = "eight"
words[9] = "nine"
words[10] = "ten"
words[11] = "eleven"
words[12] = "twelve"
words[13] = "thirteen"
words[14] = "fourteen"
words[15] = "fifteen"
words[16] = "sixteen"
words[17] = "seventeen"
words[18] = "eighteen"
words[19] = "nineteen"
words[20] = "twenty"
words[30] = "thirty"
words[40] = "forty"
words[50] = "fifty"
words[60] = "sixty"
words[70] = "seventy"
words[80] = "eighty"
words[90] = "ninety"
words[100] = "onehundred"
words[200] = "twohundred"
words[300] = "threehundred"
words[400] = "fourhundred"
words[500] = "fivehundred"
words[600] = "sixhundred"
words[700] = "sevenhundred"
words[800] = "eighthundred"
words[900] = "ninehundred"
words[1000] = "onethousand"


def filltens(start):
	for i in range(start+1,start+10):
		words[i] = words[start] + words[i-start]
		#print str(i) + ": " + words[i]

def fillhundreds(start):
	for i in range(start+1,100+start):
		words[i] = words[start/100] + "hundredand" + words[i-start] 

def countletters(roof):
	sum = 0
	for i in range(1,roof+1):
		sum += len(words[i])
	return sum


def main():
	for i in range(20,100,10):
		filltens(i)	
	for i in range(100,1000,100):
		fillhundreds(i)
	print countletters(1000)

main()
