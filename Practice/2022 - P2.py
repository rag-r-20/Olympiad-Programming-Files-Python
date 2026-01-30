import math

a, n = map(int, input().split())
nList = list(map(int, input().split()))
numNebors = 0  # Neighbors shortened to Nebors
nebors = []

if a == 1:
    for i in range(len(nList) - 1):
        if nList[i] == (nList[i+1] - 1) and nList[i] != 0:
            numNebors += 1
            currentNebor = []
            currentNebor.append(nList[i])
            currentNebor.append(nList[i+1])
            nebors.append(currentNebor)
    print(numNebors)
    print(nebors)
elif a == 2:
    for j in range(math.ceil(len(nList)/2), 0, -1):
        number = []
        for k in range(j):
            number.append(nList[k])
        print(number)