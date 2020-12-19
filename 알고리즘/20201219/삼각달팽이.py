def sum_generator(N):
    return sum(n for n in range(1, N+1))

def solution(n):
    answer = []
    map = [[0]*x for x in range(1,n+1)]
    number = 1
    index = 0 #첫번째 열에 넣기위한 인덱스였다
    col_index = -1  # 마지막 열에 넣기위한 인덱스
    col_first_index = 1
    row_index_first = 0
    row_first = 0
    row_index = n-1 # 마지막 행에 넣기위한 인덱스
    breaker = True
    while 1:
        for i in range(row_first,len(map)):
            if number > sum_generator(n):
                breaker = False
                break
            map[i][index] = number
            number += 1
        if breaker == False:
            break
        for j in range(col_first_index,len(map[row_index])):
            if number > sum_generator(n):
                breaker = False
                break
            map[row_index][j] = number
            number += 1
        if breaker == False:
            break
        for i in range(row_index-1,row_index_first,-1):
            if number > sum_generator(n):
                breaker = False
                break
            map[i][col_index] = number
            number += 1
        if breaker == False:
            break
        index += 1
        row_index -= 1
        col_index -= 1
        col_first_index += 1
        row_index_first += 1
        row_first += 2
    for i in map:
        for j in i:
            answer.append(j)
    return answer

print(solution(5))