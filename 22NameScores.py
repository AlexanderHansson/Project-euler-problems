#coding:utf-8
#Author:Alexander Hansson
#Version 2015-12-25

"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?
"""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters={k:v+1 for k,v in zip(alphabet,range(len(alphabet)))} #used to map every letter to it's number


#Creates a sorted list of all the names
names = []
with open("p022_names.txt","r") as file:
	names = file.read().split(",")

names = map(lambda x: x.strip("\""), names)
names.sort()



def calculate_score(name):
	"""calculates the score for each name"""
	sum = 0
	for letter in name:
		sum+=letters[letter.upper()]
	return sum
	
def main():
	sum = 0
	for i in range(len(names)):
		sum+=calculate_score(names[i])*(i+1)
	return sum

print main()