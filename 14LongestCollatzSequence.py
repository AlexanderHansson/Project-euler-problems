#coding:utf-8
#Author:Alexander Hansson
#Version 2015-12-14


"""
A collats sequence follow the following rules:
n->n/2 (n is even)
n->3n+1 (n is odd)
Using the starting number 13 we get the following sequence:
13->40->20->10->5->16->8->4->2->1
Find the largest collatz sequence under one million
""""

sequence = {}#static so we dont have to do things twice

def collatz(number):
    """If the collatz sequence for the given number doesn't already exists, it
    will be added, all other sequences that this sequence depend on will also be
    added"""
    if sequence.get(number) == None:
        lista = []
        if (number%2== 0):
            lista = collatz(number/2)
        elif number != 1:
            lista = collatz(3*number+1)
        sequence[number] = []
        for num in lista:
            sequence[number].append(num)
        sequence[number].append(number)
    return sequence[number]


def find_biggest_collatz_sequence(roof = 1000000):
    """Finds the biggest Collatz sequence with a starting number under param roof"""
    biggest = []
    for i in range(1,roof):
        collatz(i)
        if len(sequence[i])>len(biggest):
            biggest = sequence[i]
    return biggest


def main():
    print find_biggest_collatz_sequence()
main()

