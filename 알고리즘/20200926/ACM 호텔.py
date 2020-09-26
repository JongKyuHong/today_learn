import sys
#
t = int(input())
for _ in range(t):
    h,w,n = list(map(int,input().split(' '))) # 층, 방, 몇번째
    a = (n//h)+1 # 호수
    b = n%h # 층
    if b == 0 : b=h;a-=1
    print(b*100+a)

