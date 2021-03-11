


def divide(size,start_row,start_col):
    global cnt
    if size == 2:
        if start_row == r and start_col == c:
            print(cnt)
            return
        cnt += 1
        if start_row == r and start_col + 1 == c:
            print(cnt)
            return
        cnt += 1
        if start_row +1 == r and start_col + 1 == c:
            print(cnt)
            return
        cnt += 1
        if start_row + 1 == r and start_col + 1 == c:
            print(cnt)
            return
        cnt += 1
    else:
        divide(size // 2, start_row,start_col)
        divide(size // 2, start_row, start_col+size//2)
        divide(size // 2, start_row+size//2, start_col)
        divide(size // 2, start_row+size//2, start_col+size//2)

N , r, c = map(int,input().split(' '))
cnt = 0
divide(2**N,0,0)