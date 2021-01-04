n = int(input())
start = 2
while start <= n:
    if n % start == 0:
        n/=start
        print(start)
    else:
        start += 1


