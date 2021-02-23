import sys
input = sys.stdin.readline
n = int(input())
listn = [0]
for _ in range(n):
    listn.append(int(input()))
dp = [0 for _ in range(n+1)]
dp[1] = listn[1]
dp[2] = listn[1] + listn[2]

for i in range(3,n+1):
    dp[i] = max(dp[i-3]+listn[i-1]+listn[i],dp[i-2]+listn[i],dp[i-1])
print(dp[i])

