import sys

n = int(sys.stdin.readline().rstrip())

def sugar(n):
    sum = 0
    while True:
        if (n % 5) == 0:
            sum += (n//5)
            print(sum)
            break
        n -= 3
        sum += 1
        if n < 0:
            print("-1")
            break


