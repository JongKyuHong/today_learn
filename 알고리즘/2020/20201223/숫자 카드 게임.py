n,m = list(map(int,input().split()))
data = []
result = 0
for i in range(n):
    data.append(input().split())
    min_value = min(data)
    result = max(result,min_value)
print(result)



