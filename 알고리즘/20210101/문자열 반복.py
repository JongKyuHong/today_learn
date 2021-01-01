n = int(input())

for i in range(n):
    result = ''
    n,m = input().split()
    for i in range(len(m)):
        result += m[i]*int(n)
        #print(m[i]*int(n),end='')
    print(result)