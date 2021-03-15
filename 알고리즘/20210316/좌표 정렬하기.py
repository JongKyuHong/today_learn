n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))
array.sort(key = lambda x : (x[0],x[1]))

for a,b in array:
    print(a,b)


