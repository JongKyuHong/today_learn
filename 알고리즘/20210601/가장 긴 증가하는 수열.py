import bisect

x = int(input())
a = list(map(int,input().split()))
dp = [a[0]]

for i in range(x):
    if a[i] > dp[-1]:
        dp.append(a[i])
    else:
        idx = bisect.bisect_left(dp,a[i])
        dp[idx] = a[i]
print(len(dp))
