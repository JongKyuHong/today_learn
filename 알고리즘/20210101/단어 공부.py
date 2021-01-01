word = input().upper()
t = []
for i in set(word):
    t.append(word.count(i))
idx = [i for i,x in enumerate(t) if x==max(t)]
if len(idx) > 1: print("?")
else: print(list(set(word))[t.index(max(t))])


