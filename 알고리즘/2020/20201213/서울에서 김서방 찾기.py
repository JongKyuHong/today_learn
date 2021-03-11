def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            target = i
            break
    answer = "김서방은 " + str(target)+"에 있다"
    return answer