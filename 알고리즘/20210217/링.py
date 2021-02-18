def gcd(x,y):
    while y:
        x,y = y,x%y
    return x

n = int(input())

listn = list(map(int,input().split()))

for i in range(1,len(listn)):
    g = gcd(listn[0],listn[i])
    print(str(listn[0]//g)+"/"+str(listn[i]//g),end=' ')



