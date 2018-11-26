#!/usr/bin/python


import sys
lines = sys.stdin.read().replace("\"", "").split(",")
lettervalues = {}
words = []
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
tnums = set()
for i,letter in enumerate(alphabet):
    lettervalues[letter] = i+1



def triangle_num(n):
    return n*(n+1)/2

def wordvalue(word):
    value = 0
    for i in range(len(word)):
        value += lettervalues[word[i]]
    return value


for word in lines:
    words.append((word, wordvalue(word)))

maxvalue = max(words, key=lambda x: x[1])[1]


i = 1
tnum = triangle_num(i)
while tnum<maxvalue:
    tnums.add(tnum)
    i+=1
    tnum = triangle_num(i)


no_triangle_words = 0

for word, value in words:
    if int(value) in tnums:
        no_triangle_words+=1
        #print "word: {}, value:{}".format(word,value)
        #print tnums
print no_triangle_words
