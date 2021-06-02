import bisect

n = int(input())
an = list(map(int,input().split()))
dp = [an[0]]

for i in range(n):
    if an[i] > dp[-1]:
        dp.append(an[i])
    else:
        idx = bisect.bisect_left(dp,an[i])
        dp[idx] = an[i]
print(len(dp))



