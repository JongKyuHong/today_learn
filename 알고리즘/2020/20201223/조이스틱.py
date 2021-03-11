def solution(name):
    answer = 0
    for i in name:
        if ord(i) - ord('A') == 0:
            continue
        elif (ord(i) - ord('A')) > (ord("Z") - ord(i) + 1):
            answer += ord('Z') - ord(i) + 1
        else:
            answer += ord(i) - ord('A')
        answer += 1
    if answer == 0:
        return answer
    else:
        answer -= 1
    return answer

#print(solution('JEROEN'))
#print(solution('JAN'))
print(solution('AAAAAAAA')) #6
print(solution('AABAAAAAAAB')) #0
print(solution('ABBBBAAAAABAAA')) #15