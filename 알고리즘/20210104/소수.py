m = int(input())
n = int(input())

a = [False,False] + [True]*(n-1)
primes = []
result = []

for i in range(2,n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i,n+1,i):
            a[j] = False
for i in primes:
    if m <= i <= n:
        result.append(i)
if result:
    print(sum(result))
    print(result[0])
else:
    print(-1)



