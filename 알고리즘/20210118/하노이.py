def hanoi(begin,end,temp,n):
    if n == 1:
        end.append(begin.pop())
    else:
        hanoi(begin,temp,end,n-1)
        hanoi(begin,end,temp,1)
        hanoi(temp,end,begin,n-1)

a,b,c = [],[],[]
n = int(input())
for i in range(n):
    a.append(i)
hanoi(a,c,b,n)
print(a)
print(b)
print(c)