rgb = []
result = 0
for _ in range(int(input())):
    rgb.append((input().split()))
print(rgb)
start = rgb[0].index(min(rgb[0]))
result += int(min(rgb[0]))
print(start,result)
for i in range(1,len(rgb)):
    if start == rgb[i].index(min(rgb[i])):
        rgb[i].sort()
        result += int(rgb[i][1])
        start = 1
    else:
        start = rgb[i].index(min(rgb[i]))
        result += int(min(rgb[i]))
print(result)




