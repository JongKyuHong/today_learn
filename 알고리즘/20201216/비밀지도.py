def solution(n, arr1, arr2):
    answer = []
    map = [[0] * n for i in range(n)]
    map2 = [[0] * n for i in range(n)]
    pra = []
    for i in range(len(arr1)):
        if len(format(arr1[i],'b')) != n:
            zero = (n - len(format(arr1[i],'b'))) * '0'
            pra.append(zero + str(format(arr1[i],'b')))
        else:
            pra.append(str(format(arr1[i],'b')))
    for i in range(n):
        map[i] = pra[i]
    pra2 = []
    for i in range(len(arr2)):
        if len(format(arr2[i],'b')) != n:
            zero = (n - len(format(arr2[i],'b'))) * '0'
            pra2.append(zero + str(format(arr2[i],'b')))
        else:
            pra2.append(str(format(arr2[i],'b')))
    for i in range(n):
        map2[i] = pra2[i]

    for i in range(n):
        pra3 = ''
        for j in range(n):
            if map[i][j] == '1' or map2[i][j] == '1':
                pra3 += '#'
            elif map[i][j] == '0' and map2[i][j] == '0':
                pra3 += ' '
        answer.append(pra3)
    return answer

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))