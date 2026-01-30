import math, itertools

a, n = map(int, input().split())
perms = []
nOfPrimes = 0

def permute(x):
    # x is the number
    xstr = str(x)
    p = list(itertools.permutations(xstr))
    for i in range(len(p)):
        j = ''.join(p[i])
        p[i] = j
    p = list(dict.fromkeys(p))
    for s in range(len(p)):
        p[s] = int(p[s])
    return p

def chkIfPrime(m):
    global prime
    prime = True
    if m % 2 == 0:
        prime = False
        pass
    else:
        count = 3
        while count <= (math.ceil(m/2)):
            if m % count == 0:
                prime = False
                break
            else:
                count += 2


perms = permute(n)
for z in range(len(perms)):
    chkIfPrime(perms[z])
    if prime == True:
        nOfPrimes += 1
if a == 0:
    print(nOfPrimes)
if a == 1:
    if nOfPrimes == len(perms):
        print('1')
    else:
        print('0')












