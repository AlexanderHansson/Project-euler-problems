#coding:utf-8
#Author:Alexander Hansson
#Version 2015-12-27


def recip(num,digits=50):
    """returns the reciprocal of num with digits digits"""
    return str(10**digits/num)
    

def recLen(string,length):
    """Returns true if length is the length of the recurring cycle"""
    #print string[0:length] + " compared to: " + string[length:length*2] + " and " + string[0:length*2] + " compared to: " + string[length*2:length*4]
    if string[0:length] == string[length:length*2] and string[0:length*2] == string[length*2:length*4]:
        return True
    else:
        return False


def findLen(num):
    """Ugliest method ever #fulhack"""   
    digits = 20
    start=0
    i = 1
    rec = recip(num,digits)[start:]
    while(not recLen(rec,i)):
        i+=1
        if(len(rec)/4 < i):
            i=1
            start+=1
            rec = recip(num,digits)[start:]
        if rec == "":
            start=0
            i=1
            digits*=7
            rec = recip(num,digits)[start:]
    return i
       
       
def findLargest(cap):
    """finds the number<cap with the largest reciprocal sequence"""
    lengths = [findLen(x) for x in range(1,cap)]
    return lengths.index(max(lengths))+1
    
print findLargest(1000)
