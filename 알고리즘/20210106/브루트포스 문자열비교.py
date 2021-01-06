arr = input()
search = input()
n = len(arr)
m = len(search)

def BruteForce(search,arr):
    i = 0
    j = 0
    while j < m and i < n:
        if arr[i] != search[j]:
            i = i-j
            j = -1
        i = i+1
        j = j+1
    if j == m :
        return i-m
    else:
        return -1
print(BruteForce(search,arr))

