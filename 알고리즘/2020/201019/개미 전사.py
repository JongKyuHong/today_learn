n = int(input())
data = list(map(int,input().split()))

d = [0] * 1001

for i in range(2,n+1):
    d[i] = d[i-1] + 1
    



