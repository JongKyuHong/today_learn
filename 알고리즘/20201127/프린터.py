def solution(priorities, location):
    answer = 0
    number = [i for i in range(len(priorities))]
    target = number[location]
    while 1:
        if number[0] == target:
            if priorities[0] == max(priorities):
                answer += 1
                return answer
            else:
                number.append(number.pop(0))
                priorities.append(priorities.pop(0))
        else:
            if priorities[0] == max(priorities):
                answer += 1
                number.pop(0)
                priorities.pop(0)
            else:
                number.append(number.pop(0))
                priorities.append(priorities.pop(0))

print(solution([2,1,3,2],2))
print(solution([1,1,9,1,1,1],0))
