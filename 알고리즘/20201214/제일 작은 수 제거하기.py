def solution(arr):
    index = arr.index(min(arr))
    arr.pop(index)
    if arr:
        return arr
    else:
        arr.append(-1)
        return arr
