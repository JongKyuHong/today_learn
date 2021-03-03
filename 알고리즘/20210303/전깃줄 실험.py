n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

res = 0
for i in range(1,n):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            res += 1
            break
print(n-res)