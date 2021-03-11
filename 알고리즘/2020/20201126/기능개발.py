def solution(progresses, speeds):
    days = []
    answer = [0 * i for i in range(len(progresses))]
    answer2 = []
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] != 0:
            days.append(((100 - progresses[i]) // speeds[i]) + 1)
        else:
            days.append(((100 - progresses[i]) // speeds[i]))

    index = 0
    for i in range(len(days)):
        if i == 0:
            answer[index] += 1
        elif days[index] < days[i]:
            index = i
            answer[index] += 1
        else:
            answer[index] += 1
    for i in answer:
        if i:
            answer2.append(i)
    return answer2