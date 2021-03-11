n,m = map(int,input().split())
rice = list(map(int,input().split()))

start = 0
end = max(rice)

result = 0
while start <= end:
    total = 0
    mid = (start+end)//2
    for i in rice:
        if i > mid:
            total += i - mid
    if total > m:
        start = mid + 1
    elif total < m:
        result = mid
        end = mid - 1
print(result)