def solution(board):
    answer = 1

    N = len(board)
    def check(x,y,n):
        cnt = 1
        for i in range(x,n):
            for j in range(y,n):
                if board[i][j] == 1:
                    if j+1 <= len(board) and i+1 <= len(board):
                        a = check(i,j+1,n)
                        b = check(i+1,j+1,n)
                        c = check(i+1,j,n)
                        if (a == True and b == True) and c == True:
                            nonlocal answer
                            nonlocal cnt
                            cnt += 1
                            if cnt >= answer:
                                answer = cnt
                    else:
                        return False
                else:
                    return False
        return True

    check(0,0,N)
    return answer**2

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))