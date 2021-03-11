def solution(n):
    answer = []
    n = str(n)
    for i in n:
        answer.append(i)
    answer.sort(reverse=True)
    result = ''
    for i in answer:
        result += i

    return int(result)

print(solution(118372))
