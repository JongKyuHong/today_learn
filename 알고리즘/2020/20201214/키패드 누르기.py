def solution(numbers, hand):
    answer = ''
    pad = [[1,2,3],
           [4,5,6],
           [7,8,9],
           ["*",0,"#"]]
    rrow = 3
    rcol = 0
    lrow = 3
    lcol = 2
    left = [1,4,7]
    right = [3,6,9]
    #both = [2,5,8,0]

    for i in numbers:
        if i in left:
            answer += "L"
            for j in range(4):
                for k in range(3):
                    if pad[j][k] == i:
                        lrow = j
                        lcol = k
                        break
        elif i in right:
            answer += "R"
            for j in range(4):
                for k in range(3):
                    if pad[j][k] == i:
                        rrow = j
                        rcol = k
                        break
        else:
            for j in range(4):
                for k in range(3):
                    if pad[j][k] == i:
                        row = j
                        col = k
                        break
            rcount = abs(row-rrow) + abs(col-rcol)
            lcount = abs(row-lrow) + abs(col-lcol)
            if rcount < lcount:
                answer += "R"
                rrow = row
                rcol = col
            elif lcount < rcount:
                answer += "L"
                lrow = row
                lcol = col
            else:
                if hand == 'right':
                    rrow = row
                    rcol = col
                    answer += 'R'
                else:
                    lrow = row
                    lcol = col
                    answer += 'L'

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))

