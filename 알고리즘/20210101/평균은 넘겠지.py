c = int(input())
for i in range(c):
    count = 0
    mlist = list(map(int,input().split()))
    avg = (sum(mlist) - mlist[0])/(len(mlist)-1)
    for i in range(1,len(mlist)):
        if avg < mlist[i]:
            count += 1
    print('%.3f' % (count/(len(mlist)-1)*100),end='')
    print('%')