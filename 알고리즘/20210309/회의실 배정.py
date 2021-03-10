n = int(input())

a = []
for _ in range(n):
    a.append(list(map(int,input().split())))
result = 0
maxr = 0
k = 0
a.sort(key= lambda x : x[0])
for i in range(n):
    print(a[i])
    for j in range(i,n):
        if j == i:
            k = a[i][1]
            result += 1
        if k <= a[j][0] and n !=1:
            k = a[j][1]
            result += 1
    if maxr < result:
        maxr = result
    result = 0
print(maxr)



