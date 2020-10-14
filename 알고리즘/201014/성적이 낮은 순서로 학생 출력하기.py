n = int(input())
array = []

for _ in range(n):
    array.append(input().split(' '))

result = sorted(array,key=lambda x: x[1])

for i in result:
    print(i[0],end=' ')

