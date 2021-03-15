n = int(input())
array = []

for _ in range(n):
    a,b = input().split()
    a = int(a)
    array.append((a,b))
array.sort(key=lambda x : x[0])
for a,b in array:
    print(a,b)




