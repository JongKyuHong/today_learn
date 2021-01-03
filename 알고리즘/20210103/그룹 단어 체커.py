n = int(input())
result = 0
check = 1
for i in range(n):
    word = input()
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            continue
        else:
            for j in  range(i+1,len(word)):
                if word[i] == word[j]:
                    check = 0
                    break
    if check == 1:
        result += 1
    check = 1
print(result)