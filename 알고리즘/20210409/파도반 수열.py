p = [0]*101
p[1] = 1
p[2] = 1
p[3] = 1
for i in range(int(input())):
    n = int(input())
    for i in range(4,n+1):
        p[i] = p[i-2]+p[i-3]
    print(p[n])
