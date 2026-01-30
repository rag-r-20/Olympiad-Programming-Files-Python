NoOfThoughts = int(input())
safe = True
thoughts = []
a = []
b = []

for x in range(NoOfThoughts):
    string1 = input()
    thoughts.append(string1)
    numa, numb = map(int, string1.split(','))
    a.append(numa)
    b.append(numb)        

for i in range(NoOfThoughts):
    if a[i] == b[i]:
        safe = False
    if i == 0:
        continue
    elif i > 0:
        for j in range(i):
            if b[i] == a[j]:
                safe = False

if safe == True:
    print("SAFE")
else:
    print("UNSAFE")