n,k = map(int,input().split())

a = []
for _ in range(n):
    a.append(int(input()))
a.sort(reverse=True)
a1 = []
result = 0
for i in a:
    if i <= k:
        result += k // i
        k = k%i
        if k == 0:
            break
print(result)



