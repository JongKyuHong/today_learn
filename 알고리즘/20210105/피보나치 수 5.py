n = int(input())
result = 0
def ph(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return ph(n - 1) + ph(n - 2)
print(ph(n))

