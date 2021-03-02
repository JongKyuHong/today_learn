n = int(input())
mapn = []
for _ in range(n):
    mapn.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            mapn[i][j] = mapn[i-1][j] + mapn[i][j]
        elif j == i:
            mapn[i][j] = mapn[i-1][j-1] + mapn[i][j]
        else:
            mapn[i][j] = max(mapn[i-1][j-1],mapn[i-1][j]) + mapn[i][j]
print(max(mapn[n-1]))
