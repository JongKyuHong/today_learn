import sys

n = int(input())
m = []
for _ in range(n):
    a,b = sys.stdin.readline().rstrip().split(' ')
    a = int(a)
    m.append((a,b))
m.sort(key = lambda x:(x[0]))
for i in m:
    print(i[0],i[1])
