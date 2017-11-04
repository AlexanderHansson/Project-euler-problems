
import math
solutions = [0]
for p in range(1,1001):
    solutions.append(0)
    for b in range(1,p):
        for a in range(1,b):
            c = p-a-b
            if c**2 == a**2 + b**2:
                #print "{0} {1} {2}".format(a,b,c)
                solutions[p]+=1
    print "{0}: solutions: {1}".format(p,solutions[p])
ans= solutions.index(max(solutions))
print ans
print solutions[ans]


