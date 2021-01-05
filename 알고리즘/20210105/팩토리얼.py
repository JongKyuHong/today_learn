n = int(input())
result = 1
def ph(n):
    global result
    if n == 0:
        return result
    else:
        result *= n
        return ph(n-1)
print(ph(n))


