import math

t = int(input())

for _ in range(t):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if x1 == x2 and r1 == r2 and y1 == y2:
        print(-1)
        continue
    elif x1 == x2 and y1 == y2 and r1 != r2:
        print(0)
        continue
    if distance + r1 == r2 or distance + r2 == r1:
        print(1)
        continue
    elif (distance + r1) < r2 or (distance + r2) < r1:
        print(0)
        continue
    if r1 + r2 > distance:
        print(2)
    elif r1 + r2 == distance:
        print(1)
    else:
        print(0)

