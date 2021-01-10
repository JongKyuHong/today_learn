import math
n = int(input())
a = [[] for i in range(n)]
stair = []
for _ in range(n):
    stair.append(int(input()))
for i in range(math.ceil(n/2)):
    if i == 0:
        a[0].append(stair)
    elif i == math.ceil(n/2)-1:
        pass
    else:
        a[i].append()

print(max(a[n-1]))
