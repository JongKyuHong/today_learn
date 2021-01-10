n = int(input())
a = [[] for i in range(n)]

for i in range(n):
    if i == 0:
        rgb = list(map(int, input().split()))
        for j in range(len(rgb)):
            a[0].append(rgb[j])
    else:
        rgb = list(map(int,input().split()))
        for j in range(len(rgb)):
            if j == 0:
                a[i].append(rgb[j] + min(a[i - 1][1], a[i - 1][2]))
            elif j == 1:
                a[i].append(rgb[j] + min(a[i - 1][0], a[i - 1][2]))
            else:
                a[i].append(rgb[j] + min(a[i - 1][0], a[i - 1][1]))
print(a)
print(min(a[n-1]))




