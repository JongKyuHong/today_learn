n,m,k = map(int,input().split())
array = list(map(int,input().split()))
array.sort()
first = array[n-1]
second = array[n-2]
sum = 0
while True:
    for i in range(k):
        if m == 0:
            break
        sum += first
        m -= 1
    if m == 0:
        break
    sum += second
    m -= 1
print(sum)