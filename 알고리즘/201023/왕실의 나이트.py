n = input()

dx = [2,2,-2,-2,1,1,-1,-1]
dy = [1,-1,1,-1,2,-2,2,-2]

column = int(ord(n[0])-ord('a'))
row = int(n[1])
count = 0
for i in range(8):
    next_col = column + dx[i]
    next_row = row + dy[i]
    if next_col >= 1 and next_col <= 8 and next_row >= 1 and next_col <= 8:
        count += 1

print(count)

