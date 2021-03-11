def solution(w,h):
    answer = 0
    square = w*h
    if w == h:
        answer = square - w
    elif w%2 == 0 and h%2 == 0:
        answer = ((w/2) * (h/2))*2 + (((w/2)-1) * ((h/2)-1))*2
    elif w%2 == 1 and h%2 == 0:
        answer = ((w//2) * (h/2)) * 3
    elif w%2==0 and h%2==1:
        answer = ((h//2) * (w/2)) * 3
    else:
        answer = ((h//2) * (w//2)) * 4

    return answer

print(solution(5,9))