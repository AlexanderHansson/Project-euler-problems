#!/usr/bin/python
primes = [2]
twosquares = set([])
def is_prime(i):
    for p in primes:
        if i%p == 0:
            return False
    return True
i = 3
found = False
nextsquare = 4
squareindex = 1 
while True:
    found = False
    if i >= nextsquare:
        twosquares.add(nextsquare)
        squareindex+=1
        nextsquare = 2*squareindex**2
    if is_prime(i):
        primes.append(i)
        i+=2
    else:
        for p in primes:
            if i-p in twosquares:
                found = True
                break
        if not found:
            break
        else:
            i+=2
print i
    
        
