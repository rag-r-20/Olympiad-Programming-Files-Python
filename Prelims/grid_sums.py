n, m = map(int, input().split())
totals = []
for i in range(n):
    numbers = list(map(int, input().split()))
    nth_sum = 0
    for j in range(m):
        nth_sum += numbers[j]
    totals.append(nth_sum)

for x in range(n):
    print(totals[x])
    
