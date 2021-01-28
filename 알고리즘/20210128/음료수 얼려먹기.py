n,m = map(int,input().split())
map = []
for _ in range(m):
    map.append(list(map(int,input())))

def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >=m:
        return False
    if map[i][j] == 0:
        map[i][j] = 1
        dfs(i+1,j)
        dfs(i-1,j)
        dfs(i,j-1)
        dfs(i,j+1)
        return True
    return False
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j):
            result += 1
print(result)
