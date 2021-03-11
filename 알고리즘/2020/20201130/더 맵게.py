import heapq

def solution(scoville,K):
    heapq.heapify(scoville)
    answer = 0
    while K>scoville[0]:
        if len(scoville)>1:
            heapq.heappush(scoville,heapq.heappop(scoville) + (heapq.heappop(scoville)*2))
            answer += 1
        else:
            return -1
    return answer

print(solution([1,2,3,9,10,12],7))