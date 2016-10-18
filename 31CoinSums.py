#coding:utf-8
#Author: Alexander Hansson
#Version: 12/2-2016


"""
In england the currency is made up of pound and pence, and there are eigh coins
in general circulation:
1p, 2p, 5p, 20p, 50p, onepound(100p) and 2pound(200p)
It is possible to make 2pounds in the following way:

1*1pound + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p
How many different ways can 2pounds be made using any number of coins?
"""



class twopound(object):
    def __init__(self):
        self.value = 200
    def __del__(self):
        pass
    def get_value(self):
        return self.value
    def split(self):
        return (onepound(), onepound())
    def __str__(self):
        return str(self.value)

class onepound(object):
    def __init__(self):
        self.value = 100
    def __del__(self):
        pass
    def get_value(self):
        return self.value
    def split(self):
        return (fiftypence(), fiftypence())
    def __str__(self):
        return str(self.value)    
           

class fiftypence (object):
    def __init__(self):
        self.value = 50
    def __del__(self):
        pass
    def get_value(self):
        return self.value 
    def split(self):
        return (twentypence(), twentypence(), tenpence())
    def __str__(self):
        return str(self.value)

class twentypence (object):
    def __init__(self):
        self.value = 50
    def __del__(self):
        pass
    def get_value(self):
        return self.value
    def split(self):
        return (tenpence(), tenpence())
    def __str__(self):
        return str(self.value)



class tenpence (object):
    def __init__(self):
        self.value = 50
    def __del__(self):
        pass
    def get_value(self):
        return self.value
    def split(self):
        return (fivepence(), fivepence())
    def __str__(self):
        return str(self.value)



class fivepence (object):
    def __init__(self):
        self.value = 50
    def __del__(self):
        pass
    def get_value(self):
        return self.value
    def split(self):
        return (twopence(), twopence(),onepence())
    def __str__(self):
        return str(self.value)


class twopence (object):
    def __init__(self):
        self.value = 50
    def __del__(self):
        pass
    def get_value(self):
        return self.value
    def split(self):
        return (onepence(), onepence())
    def __str__(self):
        return str(self.value)




class onepence (object):
    def __init__(self):
        self.value = 50
    def __del__(self):
        pass
    def get_value(self):
        return self.value
    def split(self):
        return ()
    def __str__(self):
        return str(self.value)
        
        


"""
This is not working properly, find a way to recursively break down the
coins to smaller coins, in a tree-structure
every break-down should count as a new combination.
However you cant just break down all at once, fix the algorithm

"""
def split(x, sum):
    if len(x.split())>0:
        sum = sum+1
    for kid in x.split():
        sum = split(kid,sum)
    return sum




coin = twopound()


print split(coin,1)