import sys

n = int(input())
a = []
for i in range(n):
    a.append(list(map(int,input().split(' '))))
rank = 1
answer = []
for i in range(len(a)):
    rank = 1
    for j in range(len(a)):
        if a[i][0] < a[j][0] and a[i][1] < a[j][1]:
            rank += 1
    answer.append(str(rank))
print(" ".join(answer))

