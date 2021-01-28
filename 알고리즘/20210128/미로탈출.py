from collections import deque

n,m = map(int,input().split())
map = []
for _ in range(m):
    map.append(list(map(int,input())))
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >=n or ny >= m:
                continue
            if map[nx][ny] == 0:
                continue
            if map[nx][ny] == 1:
                map[nx][ny] = map[x][y] + 1
                queue.append((nx,ny))
        return map[n-1][m-1]
print(bfs(0,0))


