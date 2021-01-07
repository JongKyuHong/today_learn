dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
for _ in range(int(input())):
    t = int(input())
    for i in range(4,t+1):
        dp[i] = dp[i-2]+dp[i-3]
    print(dp[t])