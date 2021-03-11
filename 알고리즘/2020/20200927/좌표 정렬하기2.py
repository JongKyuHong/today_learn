import sys

n = int(input())

list2 = [list(map(int,sys.stdin.readline().rstrip().split(' '))) for _ in range(n)]
list2.sort(key = lambda x: (x[1],x[0]))
for i in list2:
    print(i[0],i[1])