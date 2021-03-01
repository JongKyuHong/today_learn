t = int(input())
for _ in range(t):
    n = int(input())
    dp = [[1] * i for i in range(n+1)]
    if n == 1 or n == 2 or n == 3:
        print(dp[n])
        break
    for i in range(4,n+1):
        dp[i] = dp[i-3] + dp[i-2]
    print(dp[n])


