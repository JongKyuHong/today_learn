n = int(input())
nlist = list(map(int,input().split()))
nlist.sort(reverse=True)
a = nlist[0]
mlist = []
for i in range(len(nlist)):
    mlist.append((nlist[i]/a)*100)
print(sum(mlist)/len(mlist))
