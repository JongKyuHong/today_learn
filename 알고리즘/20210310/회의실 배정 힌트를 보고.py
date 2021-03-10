n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))

a.sort(key = lambda x : (x[1],x[0]))
cnt = 1
k = a[0][1]
for i in range(1,n):
    if a[i][0] >= k:
        cnt += 1
        k = a[i][1]
print(cnt)