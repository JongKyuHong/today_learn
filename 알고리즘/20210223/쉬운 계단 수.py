n = int(input())
if n == 1:
    print(9)
    exit()
else:
    d = [x for x in range(10**(n-1),10**n)]

check = 0
result = 0
for i in range(len(d)):
    for j in range(len(str(d[i]))):
        if j == 0:
            check = int(str(d[i])[j])
        else:
            if int(str(d[i])[j]) - check == 1 or check - int(str(d[i])[j]) == 1:
                check = int(str(d[i])[j])
            else:
                break
            result += 1
print(result%(10**9))
