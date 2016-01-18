#coding:utf-8
#Author:Alexander Hansson
#Version: 2015-12-28

#TODO: convert to python2

"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

"""




def expand(matrix):
    """expands the matrix with placeholder items"""
    startx = 1
    starty = len(matrix[0])
    for rows in matrix:
        rows.insert(0,"foo")
        rows.append("foo")
    size = len(matrix[0])
    newtoprow = []
    newbotrow = []
    for i in range(size):
        newbotrow.append("foo")
        newtoprow.append("foo")
    matrix.insert(0,newtoprow)
    matrix.append(newbotrow)
    fill_matrix(matrix,startx,starty)
    
    
    
def fill_matrix(matrix,x,y):
    """replaces all placeholder items with the correct values"""
    number = matrix[x][y]
    y+=1
    number+=1
    
    #right
    matrix[x][y] = number
    
    #down
    while x<len(matrix)-1:
        number+=1
        x+=1
        matrix[x][y] = number
    
    #left
    while y>0:
        number+=1
        y-=1
        matrix[x][y] = number
    
    #up
    while x>0:
        number+=1
        x-=1
        matrix[x][y] = number
    
    #right
    while y<len(matrix)-1:
        number+=1
        y+=1
        matrix[x][y] = number
        
        
    
def print_matrix(matrix):
    """nice print for a matrix"""
    for row in matrix:
            rep=str(row)
            print(rep)
    

def summarize_diagonals(mat):
    """summarizes the diagonals in a matrix"""
    sum=0
    i=0
    for row in mat:
        sum+=row[i]
        sum+=row[len(row)-1-i] 
        i+=1
    return sum-1 #-1 because we count the middle twice



def main():
        
    #ans = int(raw_input("dimensions? axa, enter a: "))
    ans=1001
    ans=int((ans-1)/2)
    mat = [[1]]
    
    #builds the matrix
    for i in range(0,ans):
        expand(mat)
        
    #prints the answah    
    print(summarize_diagonals(mat))
    
main()
