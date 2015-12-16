#coding:utf-8
#Author:Alexander Hansson
#Version: 2015-12-16

"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""



def weekDay(num):
	"""Used to handle weekdays easier"""
	return {
	0:"Monday",
	1:"Tuesday",
	2:"Wednesday",
	3:"Thursday",
	4:"Friday",
	5:"Saturday",
	6:"Sunday"
	}[num%7]

def days_in_month(month, year):
	"""Maps month index to number of days"""
	months = {
	0:31,
	1:28,
	2:31,
	3:30,
	4:31,
	5:30,
	6:31,
	7:31,
	8:30,
	9:31,
	10:30,
	11:31
	}
	if ((year%4 == 0) and (year%100 != 0) or (year%400 == 0)):
		months[1] = 29
	return months[month]


def count_mondays():
	"""Counts the mondays in the beginning of the month from year 1901 to year 2000"""
	#some initial settings
	year = 1900
	weekday = 0 #Monday
	mondaysonfirst = 0
	while year<2001:
		for month in range(12): 
			print "month: " + str(month) + " weekday: " + str(weekDay(weekday))
			if weekDay(weekday) == "Sunday" and year != 1900:	
				mondaysonfirst+=1	
			weekday+=(days_in_month(month,year))%7
		year+=1
	return mondaysonfirst


print count_mondays()	



