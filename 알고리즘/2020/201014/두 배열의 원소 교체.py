n,k = map(int,input().split(' '))
a = list(map(int,input().split(' ')))
b = list(map(int,input().split(' ')))

for _ in range(k):
    mina = a.index(min(a))
    maxb = b.index(max(b))
    a[mina], b[maxb] = b[maxb], a[mina]
result = 0
for i in a:
    result += i
print(result)