n,k = map(int,input().split())

knap = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1,n+1):
    w,v = map(int,input().split())
    for j in range(1,k+1):
        if j < w:
            knap[i][j] = knap[i-1][j]
        else:
            knap[i][j] = max(knap[i-1][j],knap[i-1][j-w]+v)