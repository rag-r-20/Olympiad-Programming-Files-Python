import math

n = int(input())
gridSize = n**2
accFibNums = [1]
outFibNums = [1]

for i in range(1, gridSize):
    if i == 1:
        x = 1
        accFibNums.append(x)
    else:
        x = accFibNums[i - 1] + accFibNums[i - 2]
        accFibNums.append(x)
    
    xstr = str(x)  
    if len(xstr) > 6:
        xstr = xstr[-6::]
        x = int(xstr)
        outFibNums.append(x)
    else:
        outFibNums.append(x)

'''
for r in range(n):
    for c in range(n):
        a = outFibNums[((n-1)**2)-c+r]
        if c == r and c <= (math.ceil(n/2)-1):
            a = outFibNums[((n-1-(2*r))**2)]
        elif c == r:
            a = outFibNums[((n-(2*(n-r)))**2)]
        if c == (n-1):
            print(a)
        else:
            print(a, end=",")
'''
