def solution(n, times):
    start = 1
    end = n*max(times)
    while start < end:
        mid = start+end // 2
        if sum(mid//x for x in times) < n:
            start = mid + 1
        else:
            end = mid - 1
    return start