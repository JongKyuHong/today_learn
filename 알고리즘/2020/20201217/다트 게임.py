def solution(dartResult):
    answer = []
    result = 0
    cal = 0
    index = 0
    check = 0
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            if i != 0:
                if dartResult[i-1].isalnum():
                    answer.append(cal)
                    index += 1
                    cal = 0
            if dartResult[i] == '1':
                if dartResult[i+1] == '0':
                    check = 1
                    continue
                else:
                    cal = int(dartResult[i])
            elif check == 1:
                cal = 10
                check = 0
            else:
                cal = int(dartResult[i])
        if dartResult[i].isalpha():
            if dartResult[i] == 'D':
                cal = cal**2
            elif dartResult[i] == 'T':
                cal = cal**3
            else:
                cal = cal**1
        if dartResult[i].isalnum() == False:
            if dartResult[i] == '*':
                if index != 0:
                    answer[index-1] = answer[index-1] * 2
                    cal = cal * 2
                else:
                    cal = cal * 2
            elif dartResult[i] == '#':
                cal = cal * -1
            answer.append(cal)
            index += 1
            cal = 0

    for i in answer:
        result += i
    result = result + cal
    return result

print(solution('1D2S3T*'))