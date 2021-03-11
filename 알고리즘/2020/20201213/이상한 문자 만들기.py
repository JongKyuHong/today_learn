def solution(s):
    answer = []
    count = 0
    for i in s:
        if i == ' ':
            answer.append(i)
            count = 0
        elif i != ' ':
            if count % 2 == 0:
                answer.append(i.upper())
                count += 1
            else:
                answer.append(i.lower())
                count += 1
    return ''.join(answer)

print(solution("try hello world"))