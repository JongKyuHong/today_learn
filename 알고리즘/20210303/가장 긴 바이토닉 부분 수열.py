n = int(input())

arr = list(map(int,input().split()))
result = [0]*n
result_ = [0] * n
res = 0
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and result[i] < result[j]:
            result[i] = result[j]
    result[i] += 1

for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if arr[i] > arr[j] and result_[i] < result_[j]:
            result_[i] = result_[j]
    result_[i] += 1
for i in range(n):
    res = max(res,result[i] + result_[i]-1)
print(res)