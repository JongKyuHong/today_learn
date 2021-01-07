idx0 = 0
idx1 = 0
def pibo(n):
    global idx1,idx0
    if n == 0:
        idx0+=1
        return 0
    elif n ==1:
        idx1 += 1
        return 1
    else:
        return pibo(n-1) + pibo(n-2)

for _ in range(int(input())):
    pibo(int(input()))
    print(idx0,idx1)
    idx0,idx1=0,0







