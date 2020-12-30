def solution(numbers, target):
    answer = 0
    bfs(numbers,target)
    return answer

def bfs(numbers,target):

    for i in numbers:
