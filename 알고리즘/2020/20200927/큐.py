import sys

n = int(input())
stack = []
for i in range(n):
    w = sys.stdin.readline().rstrip().split(' ')
    if w[0] == "push":
        stack.append(w[1])
    elif w[0] == 'front':
        if stack:
            print(stack[0])
        else:
            print("-1")
    elif w[0] == 'back':
        if stack:
            print(stack[-1])
        else:
            print("-1")
    elif w[0] == 'size':
        print(len(stack))
    elif w[0] == 'empty':
        if stack:
            print("0")
        else:
            print("1")
    elif w[0] == 'pop':
        if stack:
            print(stack.pop(0))
        else:
            print("-1")