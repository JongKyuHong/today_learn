## 수 정렬하기2
import sys

n = int(input())
a = [int(sys.stdin.readline().rstrip()) for i in range(n)]
a.sort()
for i in a:
    print(i)

