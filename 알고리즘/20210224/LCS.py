ab = input()
cb = input()

matrix = [[0]*(len(cb)+1) for _ in range(len(ab)+1)]
for i in range(1,len(ab)+1):
    for j in range(1,len(cb)+1):
        if ab[i-1] == cb[j-1]:
            matrix[i][j] = matrix[i-1][j-1]+1
        else:
            matrix[i][j] = max(matrix[i-1][j],matrix[i][j-1])
print(matrix[-1][-1])


