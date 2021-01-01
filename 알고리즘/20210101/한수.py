n = int(input())
count = 1
result = 0
while n >= count:
    if count < 10:
        result += 1
    elif 10 <= count and count < 100:
        count = str(count)
        if int(count[0]) < int(count[1]) or int(count[1]) <= int(count[0]):
            result += 1
    else:
        count = str(count)
        if (int(count[1]) - int(count[0])) == (int(count[2]) - int(count[1])):
                result += 1
    count = int(count)
    count += 1
print(result)


