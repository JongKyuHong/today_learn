n = int(input())
listn = []
for _ in range(n):
    listn.append(list(map(int,input().split())))

dp = [1]*n
result = 0
listn.sort(key = lambda x : x[0])
print(listn)

for i in range(1,len(listn)):
    for j in range(i):
        if listn[i][1] > listn[j][1]:
            dp[i] = max(dp[i],dp[j]+1)

print(n-max(dp))


