def fibo(n):
    next,last = 1,0
    for _ in range(1,n):
        last,next = next,last+next
    return next
n = int(input())
print(fibo(n))