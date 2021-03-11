def solution(n, lost, reserve):
    answer = [1] * n
    result = 0
    for i in reserve:
        answer[i-1] += 1
    print(answer)
    for i in lost:
        answer[i-1] -= 1
    print(answer)
    for i in range(len(answer)-1):
        if answer[i] == 0:
            if i == 0:
                if answer[i+1] == 2:
                    answer[i+1] -= 1
                    answer[i] += 1
            else:
                if answer[i-1] == 2:
                    answer[i-1] -= 1
                    answer[i] += 1
                elif answer[i+1] == 2:
                    answer[i+1] -= 1
                    answer[i] += 1
    print(answer)
    for i in answer:
        if i >= 1:
            result += 1
    return result
print(solution(5,[2,4],[3]))