n = int(input())

distance = list(map(int,input().split()))
liter = list(map(int,input().split()))
mina = liter[0]
ex = 0
result = 0
for i in range(1,len(liter)):
    if mina > liter[i]:
        ex += distance[i-1]
        result += mina*ex
        ex = 0
        mina = liter[i]
    else:
        if i == len(liter)-1:
            ex += distance[i-1]
            result += mina*ex
        else:
            ex += distance[i-1]
print(result)
