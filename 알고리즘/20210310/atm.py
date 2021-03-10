n = int(input())
a = list(map(int,input().split()))
if n == 1:
    print(a[0])
else:
    a.sort()
    result = 0
    q = 0
    for i in range(n):
        result += q+a[i]
        q += a[i]
    print(result)

