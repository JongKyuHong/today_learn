n,m = list(map(int,input().split()))

array = []
for _ in range(n):
    array.append(int(input()))
d = (m+1) * 10001
d[0] = 0

for i in range(n):
    for j in range(2,m+1):
        d[j] = min(d[j],d[j-array[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])



