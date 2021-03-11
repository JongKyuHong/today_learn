n = int(input())
data = list(input().split())

nx = 1
ny = 1
dx = 0
dy = 0
for i in data:
    if i == 'R':
        if nx == n:
            continue
        else:
            nx += 1
    elif i == 'L':
        if nx == 1:
            continue
        else:
            nx -= 1
    elif i == 'U':
        if ny == 1:
            continue
        else:
            ny -= 1
    elif i == 'D':
        if ny == n:
            continue
        else:
            ny += 1
print(ny,nx)