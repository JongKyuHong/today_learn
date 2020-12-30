def solution(board):
    answer = 1234
    #board_new = board.deepcopy()
    def check(x,y,board):
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    if j+1 <= len(board) and i+1 <= len(board):
                        check(i,j+1)
                        check(i+1,j+1)

    return answer

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))