a = int(input())

zero = [1,0,1]
one = [0,1,1]

def pibo(a):
    length = len(zero)
    if length <= a:
        for i in range(length,a+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print("%d %d"%(zero[a],one[a]))
for i in range(a):
    k = int(input())
    pibo(k)