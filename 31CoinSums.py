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





value = 200
ways = 0

for twopo in [x*200 for x in range(value/200+1)]:
    value = 200 - twopo
    for onepo in [x*100 for x in range(value/100+1)]:
        value = 200-twopo-onepo
        for fiftypence in [x*50 for x in range(value/50+1)]:
            value = 200-twopo-fiftypence
            for twentypence in [x*20 for x in range(value/20+1)]:
                value = 200-twopo-onepo-fiftypence-twentypence
                for tenpence in [x*10 for x in range(value/10+1)]:
                    value = 200-twopo-onepo-fiftypence-twentypence-tenpence
                    for fivepence in [x*5 for x in range(value/5+1)]:
                        value=200-twopo-onepo-fiftypence-twentypence-tenpence-fivepence
                        for twopence in [x*2 for x in range(value/2+1)]:
                            value=200-twopo-onepo-fiftypence-twentypence-tenpence-fivepence-twopence
                            while(value>0):
                                value-=1
                            else:
                                ways+=1

print ways


