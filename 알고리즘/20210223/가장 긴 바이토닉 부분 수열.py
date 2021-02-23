n = int(input())

array = list(map(int,input().split()))
dp = [1 for i in range(n)]
dp2 = [1 for i in range(n)]
for i in range(n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i],dp[j]+1)
array.reverse()
for i in range(n):
    for j in range(i):
        if array[i]>array[j]:
            dp2[i] = max(dp2[i],dp2[j]+1)
dp2.reverse()
result = [0 for i in range(n)]
for i in range(n):
    result[i] = dp[i] + dp2[i]
print(max(result)-1)



