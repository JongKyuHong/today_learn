while 1:
    n = int(input())
    if n == 0:
        break
    a = [False,False] + [True]*((2*n)-1)
    so = []
    result = []
    for i in range(2,(2*n)+1):
        if a[i]:
            so.append(i)
            for j in range(2*i,(2*n)+1,i):
                a[j] = False
    for i in so:
        if n<i<=2*n:
            result.append(i)
    print(len(result))



