def solution(food_times, k):
    answer = 0
    while True:
        for i in range(len(food_times)):
            answer += 1
            if food_times[i] != 0:
                food_times[i] -= 1
                k -= 1
            else:
                continue
            if k == 0:
                if answer == len(food_times):
                    return 1
                else:
                    return answer + 1
            else:
                if answer == len(food_times):
                    answer = 0
        if any(food_times):
            continue
        else:
            break
    answer = -1
    return answer

food_times = list(map(int,input().split()))
k = int(input())
print(solution(food_times,k))

