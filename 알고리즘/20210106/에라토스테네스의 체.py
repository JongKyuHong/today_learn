n = int(input())

a = [False,False] + [True]*(n-1)
sum = []
for i in range(2,n):
    if a[i]:
        sum.append(i)
        for j in range(2*i,n,i):
            a[j] = False
print(sum)


