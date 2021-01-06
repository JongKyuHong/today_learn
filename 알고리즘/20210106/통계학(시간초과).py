n = int(input())
lista = []
for i in range(n):
    lista.append(int(input()))
print(round(sum(lista)/len(lista)))
lista.sort()
print(lista[len(lista)//2])
a = sorted(set(lista))
setlist = []
for i in a:
    setlist.append(lista.count(i))
maxset = [i for i,x in enumerate(setlist) if x == max(setlist)]
if len(maxset) > 1: print(list(a)[maxset[1]])
else: print(list(a)[maxset[0]])
print(lista[-1]-lista[0])

