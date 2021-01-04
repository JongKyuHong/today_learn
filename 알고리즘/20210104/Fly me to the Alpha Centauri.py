T = int(input())
for i in range(T):
    d = 0
    result = 1
    x,y = map(int,input().split())
    target = y-x-2
    if target % 2 == 0:
        target=target/2
        while target != result:
            d += 1
            result += d
        print(d*2+2)
    else:
        



