n = int(input())
a = input().split()
location = [1,1]
for i in a:
    if i == 'R':
        if location[1] < n:
            location[1] += 1
    elif i == 'L':
        if location[1] > 1:
            location[1] -= 1
    elif i == 'U':
        if location[0] > 1:
            location[0] -= 1
    elif i == 'D':
        if location[0] < n:
            location[0] += 1

for i in location:
    print(i,end=' ')

