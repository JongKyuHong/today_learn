n = int(input())

listn = list(map(int,input().split()))
for i in range(1,n):
    listn[i] = max(listn[i],listn[i-1]+listn[i])
print(max(listn))

