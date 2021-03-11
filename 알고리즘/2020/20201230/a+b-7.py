t = int(input())

for i in range(1,t+1):
    n,m = map(int,input().split())
    print("Case #",end='')
    print(i,end='')
    print(":", n+m)