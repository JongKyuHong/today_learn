n = input().upper()
listn = []
for i in set(n):
    listn.append(n.count(i))
idx = [i for i,x in enumerate(listn) if x==max(listn)]
if len(idx) > 1: print("?")
else: print(list(set(n))[listn.index((max(listn)))])


