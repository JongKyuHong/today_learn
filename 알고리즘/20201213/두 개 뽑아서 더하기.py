def solution(numbers):
    answer = []
    number = 0
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            print(numbers[i],numbers[j])
            number = numbers[i] + numbers[j]

            if number not in answer:
                answer.append(number)
    answer.sort()

    return answer

print(solution([5,0,2,7]))