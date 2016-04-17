import math
import sys

def generate(max):
    p = 2
    list = [i for i in range(max + 1)]
    primes = []
    while p <= math.sqrt(max):
        primes.append(p)
        for i in range(math.ceil((max + 1) / p)): # cross out composites
            list[i*p] = False
        p += 1
        while list[p] == False: # find next prime
            p += 1
    for i in range(p, max + 1): # enter remaining primes
        if list[i] != False:
            primes.append(list[i])
    
    print(primes)
    return primes
    
if __name__ == '__main__':
    if len(sys.argv) == 2:
        generate(int(sys.argv[1]))
    else:
        print("Usage: generate.py max")