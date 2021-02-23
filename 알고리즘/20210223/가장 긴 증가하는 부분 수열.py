import sys
input = sys.stdin.readline
n = int(input())
array = list(map(int,input().split()))
dp = [0] * 1001

if n == 1:
    print(1)
    exit()

for k in range(n):
    dp[k] = 1
    for i in range(k):
        if array[i] < array[k]:
            dp[k] = max(dp[k],dp[i]+1)



