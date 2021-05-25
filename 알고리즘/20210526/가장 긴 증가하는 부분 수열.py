## LIS https://hyun-am-coding.tistory.com/entry/%EC%B5%9C%EC%9E%A5-%EC%A6%9D%EA%B0%80-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4LIS-%EA%B0%9C%EB%85%90

## dp로 풀때

# x = int(input())
#
# arr = list(map(int,input().split()))
# dp = [1 for i in range(x)]
# for i in range(x):
#     for j in range(i):
#         if arr[i] > arr[j]:
#             dp[i] = max(dp[i], dp[j]+1)
# print(max(dp))

## 이진트리로 풀때

import bisect

x = int(input())
arr = list(map(int,input().split()))
dp = [arr[0]]
for i in range(x):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        idx = bisect.bisect_left(dp,arr[i])
        dp[idx] = arr[i]
print(len(dp))

## bisect.biesct_left(arr,x) : arr이 정렬되어 있다는 가정하에 x값이 들어갈 위치 반환