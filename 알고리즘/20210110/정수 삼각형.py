n = int(input())
a = [[] for i in range(n)]

for i in range(n):
    if i == 0:
        lane = list(map(int,input().split()))
        a[0].append(lane[0])
    else:
        lane = list(map(int,input().split()))
        for j in range(len(lane)):
            if j == 0:
                a[i].append(lane[j]+a[i-1][0])
            elif j == (len(lane)-1):
                a[i].append(lane[j]+a[i-1][j-1])
            else:
                a[i].append(lane[j]+max(a[i-1][j-1],a[i-1][j]))
print(a)
print(max(a[n-1]))


