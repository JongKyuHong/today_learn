import sys

a = []
for _ in range(int(sys.stdin.readline().rstrip())):
    b = int(sys.stdin.readline().rstrip())
    if b == 0:
        a.pop()
    else:
        a.append(b)
sum=0
for i in a:
    sum += i
print(sum)