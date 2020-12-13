def solution(a, b):
    answer = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    cal = [31,29,31,30,31,30,31,31,30,31,30,31]
    day = 0
    while a != 0:
        a -= 1
        day += cal[a-1]
    day -= cal[a-1] - b
    print(day)
    result = answer[(day%7)-1]

    return result

print(solution(5,24))