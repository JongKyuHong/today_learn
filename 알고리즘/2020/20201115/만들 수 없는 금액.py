n = int(input())
listn = list(map(int,input().split()))
listn.sort()

target = 1
for x in listn:
    if target < x:
        break
    target += x
print(target)






