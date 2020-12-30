import math

def solution(arr):
    answer = []
    if len(arr) >= 2:
        i = len(arr)
        print(arr[i-2:i])
        print(i)

    else:
        if arr[0] == 1:
            answer = [0,1]
        else:
            answer =[1,0]

    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
#print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))