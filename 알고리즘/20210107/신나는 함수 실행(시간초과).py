def w2(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20,20,20)
    elif a < b and b < c:
        return  w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    else:
        return w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)

def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a < b or a < c:
        return 2**a
    elif b == 1 and c == 1:
        return a+1
    # elif a < b and b < c:
    #     return 2**a
    # elif a == b == c:
    #     return 2**a
    # elif c < a and a < b:
    #     return 2**a
    # elif b < a and a < c:
    #     return 2**a
    elif a > 20 or b > 20 or c > 20:
        return 2**20
    else:
        return w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
while 1:
    a,b,c = map(int,input().split())
    if a== -1 and b == -1 and c == -1:
        break
    print('w(%d, %d, %d) = %d' % (a, b, c, w(a, b, c)))

