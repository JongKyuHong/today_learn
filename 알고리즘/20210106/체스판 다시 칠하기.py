n,m = map(int,input().split())
map = []
result = []
for _ in range(n):
    map.append(input())

for a in range(n-7):
    for b in range(m-7):
        idx1=0
        idx2=0
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i+j)%2 == 0:
                    if map[i][j] !='W':
                        idx1 += 1
                    if map[i][j] !='B':
                        idx2 += 1
                else:
                    if map[i][j] !='B':
                        idx1 += 1
                    if map[i][j] !='W':
                        idx2 += 1
        result.append(idx1)
        result.append(idx2)
print(min(result))


