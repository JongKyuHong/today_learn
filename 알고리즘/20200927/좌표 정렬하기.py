import sys

n = int(input())

N = [list(map(int,sys.stdin.readline().rstrip().split(' '))) for _ in range(n)]
N.sort(key = lambda x : (x[0],x[1]))

for i in N:
    print(i[0],i[1])