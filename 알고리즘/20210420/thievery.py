def solution(money):
    dn = [0] * len(money)
    dn[0] = money[0]
    dn[1] = max(money[0],money[1])
    for i in range(2,len(money)-1):
        dn[i] = max(dn[i-1],dn[i-2]+money[i])
    dn1 = [0] * len(money)
    dn1[0] = 0
    dn1[1] = money[1]
    for i in range(2,len(money)):
        dn1[i] = max(dn1[i-1],money[i]+dn1[i-2])
    return max(max(dn),max(dn1))
money = list(map(int,input().split()))
print(solution(money))