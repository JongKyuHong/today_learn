def solution(m, n, puddles):
    answer = 0
    memo = [[0 for i in range(m+1)] for j in range(n+1)]
    memo[1][1] = 1
    print(memo)
    for k in range(1,n+1):
        for j in range(1,m+1):
            if [j,k] in puddles:
                continue
            if k==1 and j == 1:
                continue
            memo[k][j] = memo[k-1][j] + memo[k][j-1]
    return memo[-1][-1] % 1000000007

print(solution(4,3,[[2,2]]))