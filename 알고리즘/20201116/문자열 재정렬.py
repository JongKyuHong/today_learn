s = list(input())
result = 0
s2 = []
for i in s:
    if i.isnumeric():
        result += int(i)
    else:
        s2.append(i)

s2.sort()
s2.append(result)
for i in s2:
    print(i,end='')


