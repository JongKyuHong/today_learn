def solution(n):
    watermelon = ['수','박']
    if n % 2 == 0:
        answer = watermelon[0] + watermelon[1]
        answer = answer * (n//2)
    else:
        answer = watermelon[0] + watermelon[1]
        answer = answer * (n//2)
        answer += watermelon[0]
    return answer

