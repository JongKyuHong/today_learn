n = int(input())
array = list(map(int,input().split()))
result = [-1 for _ in range(n)]
stack = []
stack.append(0)
i = 1

while stack and i < n:
    while stack and array[stack[-1]] < array[i]:
        result[stack[-1]] = array[i]
        stack.pop()
    stack.append(i)
    i += 1
for i in result:
    print(i,end=' ')








