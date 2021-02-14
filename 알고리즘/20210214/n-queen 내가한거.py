n = int(input())

def nqueen(arr):
    global ans
    length = len(arr)
    if length==n:
        ans += 1
        return
    array = list(range(n))
    for i in range(length):
        print(arr[i])
        if arr[i] in array:
            array.remove(arr[i])
        distance = length - i
        print("거리",distance)

        if arr[i] + distance in array:
            array.remove(arr[i]+distance)

ans = 0
for i in range(n):
    nqueen([i])
print(ans)