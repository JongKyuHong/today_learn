n = int(input())

vin = [0]
for _ in range(n):
    vin.append(int(input()))
dp = [0] * (n+1)
if n == 1:
    print(vin[1])
elif n == 2:
    print(vin[1]+vin[2])
elif n == 3:
    print(max(vin[1]+vin[3],vin[2]+vin[3]))
else:
    dp[1] = vin[1]
    dp[2] = vin[1]+vin[2]
    dp[3] = max(vin[1]+vin[3], vin[2]+vin[3])
    for i in range(4,n+1):
        dp[i] = max(dp[i-3]+vin[i-1]+vin[i],dp[i-2]+vin[i],dp[i-1])
    print(dp[n])





