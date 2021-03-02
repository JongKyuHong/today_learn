n = int(input())

vin = [0]
for _ in range(n):
    vin.append(int(input()))
dp = [0] * (n+1)

for i in range(1,n+1):
    if i == 1:
        dp[1] = vin[1]
    elif i == 2:
        dp[2] = vin[1] + vin[2]
    else:
        dp[i] = max(vin[i-1]+dp[i-3]+vin[i],dp[i-2]+vin[i],dp[i-1])
print(dp[n])

## 포도주 나중에 한번 더 해봅시다
