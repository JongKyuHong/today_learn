def solution(answers):
    a = [1,2,3,4,5]*2000
    b = [2,1,2,3,2,4,2,5]*1200
    c = [3,3,1,1,2,2,4,4,5,5]*1000
    a = a[:len(answers)]
    b = b[:len(answers)]
    c = c[:len(answers)]
    a1 = 0
    b1 = 0
    c1 = 0
    answer = []
    for k,l in zip(a,answers):
        if k == l:
            a1 += 1
    answer.append(1)

    for k,l in zip(b,answers):
        if k == l:
            b1 += 1

    if b1 > a1:
       del answer[:]
       answer.append(2)
    elif b1 == a1:
        answer.append(2)

    for k,l in zip(c,answers):
        if k == l:
            c1 += 1

    if answer[0] == 1:
        if c1 > a1:
            del answer[:]
            answer.append(3)
        elif c1 == a1:
            answer.append(3)
    elif answer[0] == 2:
        if c1 > b1:
            del answer[:]
            answer.append(3)
        elif c1 == b1:
            answer.append(3)

    return answer



