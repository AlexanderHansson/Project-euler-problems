#coding:utf-8


def isPanDigi(num,num2):
    print ""+str(num)+"*"+str(num2)+"="+str(num*num2) 
    num = str(num) + str(num2) + str(num*num2)
    num = int(num)
    onetonine = [1,2,3,4,5,6,7,8,9]
    ret = True;
    while num>0:
        if num%10 not in onetonine:
            return False
        else:
            onetonine.remove(num%10)
            num/=10
    return len(onetonine)==0


#totalOrdering
class prod(Object):
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
        self.prod = n1*n2
    def __eq__(self,other):
        return n1==other.n1 || n2==other.n2



#TODO:loopa genom alla tal och kolla om de är pandigiprodukter, hitta ett smart roof. använd dict 



    
       