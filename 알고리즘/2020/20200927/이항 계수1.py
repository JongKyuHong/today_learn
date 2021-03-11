from math import factorial

n,k = map(int,input().split(' '))
# print(factorial(n)//factorial(k)//factorial(n-k))
def a(n,k):
    if k==0 or n==k:
        return 1
    return a(n-1,k) + a(n-1,k-1)

print(a(n,k))