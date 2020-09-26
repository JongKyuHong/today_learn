import sys

while True:
    a = list(map(int,sys.stdin.readline().rstrip().split(' ')))
    b = max(a)
    if b == 0: break
    a.remove(b)
    if a[0]**2 + a[1]**2 == b**2: print("right")
    else: print("wrong")