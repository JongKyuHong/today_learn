def solution(board, moves):
    answer = 0
    target = -1
    count = 0
    stack = []
    for i in moves:
        for j in board:
            if j[i-1] != 0:
                stack.append(j[i-1])
                j[i-1] = 0
                break
    while True:
        try:
            count += 1
            if stack[target] == stack[target-1]:
                del stack[target]
                del stack[target]
                answer += 2
                target = -1
            else:
                target -= 1
        except IndexError:
            break

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))