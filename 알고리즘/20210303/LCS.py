n = input()
a = input()

res = 0
dp = [0]*n
dp[0] = n[0]
for i in range(n):
    dp[i] = n[:i]
    if dp[i] in a:
        res = len(dp[i])
print(res)