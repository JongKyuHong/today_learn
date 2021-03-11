import sys

n,k = list(map(int,sys.stdin.readline().rstrip().split(' ')))

k2 = k-1
queue = [i for i in range(1,n+1)]
result = []
n2 = n-1
while queue:
    if k2>=len(queue):
        k2 = k2%len(queue)
    result.append(str(queue.pop(k2)))
    k2 += k - 1
    # if n == 2:
    #     if k % 2 !=0:
    #         result.append(str(queue.pop(0)))
    #         result.append(str(queue.pop(0)))
    #     else:
    #         result.append(str(queue.pop(1)))
    #         result.append(str(queue.pop(0)))
    #     break

print("<",end='')
print(', '.join(result),end='')
print(">")






