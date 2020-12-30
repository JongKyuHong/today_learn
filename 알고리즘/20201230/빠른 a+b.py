import sys

T = int(input())

while T:
    T -= 1
    n,m = map(int,sys.stdin.readline().rstrip().split())
    print(n+m)
