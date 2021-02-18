def divid(x,y,n):
    global white,blue,listn
    color = listn[y][x]
    double_break = False
    for i in range(x,x+n):
        if double_break:
            break
        for j in range(y,y+n):
            if listn[j][i] != color:
                divid(x,y,n//2)
                divid(x+n//2,y,n//2)
                divid(x,y+n//2,n//2)
                divid(x+n//2,y+n//2,n//2)
                double_break = True
                break
    if not double_break:
        if listn[y][x] == 1:
            blue += 1
        else:
            white += 1

n = int(input())
listn = []
for _ in range(n):
    listn.append(list(map(int,input().split())))
white = 0
blue = 0
divid(0,0,n)
print(white)
print(blue)


