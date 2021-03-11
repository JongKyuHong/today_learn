## 블랙잭 https://www.acmicpc.net/problem/2798
import sys

n,m = map(int,sys.stdin.readline().split(' '))
k = list(map(int,sys.stdin.readline().split(' ')))

max = 0
for i in range(n):
    for j in range(i+1,n):
        for l in range(j+1,n):
            sum = k[i] + k[j] + k[l]
            if sum > max:
                if sum <= m:
                    max = sum
print(max)