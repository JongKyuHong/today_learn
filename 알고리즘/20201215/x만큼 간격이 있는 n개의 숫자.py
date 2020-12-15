def solution(x, n):
    answer = []
    target = 0
    ln = x
    while target < n:
        target += 1
        answer.append(x)
        x += ln
    return answer