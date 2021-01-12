import math
n = int(input())
a = [0*i for i in range(n)]
stair = []
for _ in range(n):
    stair.append(int(input()))
check = 0
i = 0
index = 0
while i <=n-1:
    if i == 0:
        a[index] = stair[i]
        index += 1
    if i+2 <= n-1:
        if check == 0:
            if a[index-1] + stair[i+1] > a[index-1] + stair[i+2]:
                a[index] = a[index-1] + stair[i+1]
                i += 1
                check = 1
            else:
                a[index] = a[index-1] + stair[i+2]
                i += 2
        elif check == 1:
            a[index] = a[index-1] + stair[i+2]
            check = 0
            i += 2
    else:
        i += 1
        a[index] = a[index-1]
    if i == n-1:
        a[index] = a[index-1] + stair[i]
        break
    index += 1
print(a[index])
