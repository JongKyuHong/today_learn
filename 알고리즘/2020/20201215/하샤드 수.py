def solution(x):
    x1 = str(x)
    result = 0
    for i in x1:
        result += int(i)
    if x % result == 0:
        return True
    else:
        return False