n = int(input())
lista = []
for i in range(n):
    lista.append(int(input()))
print(round(sum(lista)/len(lista)))
lista.sort()
print(lista[len(lista)//2])

from collections import Counter
k = Counter(lista).most_common()

if len(lista) > 1:
    if k[0][1] == k[1][1]: print(k[1][0])
    else: print(k[0][0])
else: print(lista[0])

print(lista[-1]-lista[0])

