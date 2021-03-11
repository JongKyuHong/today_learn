import sys

n = int(sys.stdin.readline().rstrip())


for _ in range(n):
    stack = []
    a = 0
    text = sys.stdin.readline().rstrip()

    for i in text:
        if len(stack) == 0 and i == ')':
            a=1
            break
        if i == '(':
            stack.append(i)
        else:
            if stack[-1] == '(':
                stack.pop()
            else:
                a = 1
                break
    if len(stack) == 0 and a == 0:
        print("YES")
    else:
        print("NO")
