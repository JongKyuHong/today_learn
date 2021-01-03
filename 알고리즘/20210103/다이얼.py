n = input()

alpha = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
result = 0
for i in n:
    for j in alpha:
        if i in j:
            result += alpha.index(j) + 3

print(result)