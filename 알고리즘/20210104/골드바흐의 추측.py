def prime(n):
    a = [True] * n
    m = int(n**0.5)
    for i in range(2, m+1):
        if a[i]:
            for j in range(2 * i,n, i):
                a[j] = False
    return [i for i in range(2,n) if a[i] == True]

def sosu(n):
    li = prime(n)
    newlist = max([x for x in range(len(li)) if li[x] <= n / 2])
    for i in range(newlist, -1, -1):
        for j in range(i, len(li)):
            if li[i] + li[j] == m:
                return li[i], li[j]

for _ in range(int(input())):
    m = int(input())
    print(" ".join(map(str,sosu(m))))




