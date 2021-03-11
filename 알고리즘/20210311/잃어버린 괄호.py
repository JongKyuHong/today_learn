n = input().split('-')
result = 0
n2 = n[0].split('+')
for i in n2:
    result += int(i)

for i in n[1:]:
    for j in i.split('+'):
        result -= int(j)
print(result)



