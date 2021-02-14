n = int(input())

def dfs(arr):
    global ans
    length = len(arr)
    if length == n:
        ans+=1
        return
    candidate = list(range(n))
    for i in range(length):
        if arr[i] in candidate:
            candidate.remove(arr[i])
        distance = length - i
        if arr[i] + distance in candidate:
            candidate.remove(arr[i] + distance)
        if arr[i] - distance in candidate:
            candidate.remove(arr[i] - distance)
    if candidate:
        for i in candidate:
            arr.append(i)
            dfs(arr)
            arr.pop()
    else:
        return

ans = 0
for i in range(n):
    dfs([i])
print(ans)


