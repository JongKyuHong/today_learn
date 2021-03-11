import math

def solution(n):
    answer = 0
    a = math.sqrt(n)
    if a.is_integer():
        answer = (a + 1) ** 2
    else:
        answer = -1
    return int(answer)

print(solution(121))