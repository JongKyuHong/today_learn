while True:
    a = input().rstrip()
    b = []
    c = 1
    for i in a:
      if i == '(' or i == '[':
          b.append(i)
      elif i == ')':
          if b and b[-1] == '(':
              b.pop()
          else:
              c = 0
              break
      elif i == ']':
          if b and b[-1] == '[':
              b.pop()
          else:
              c = 0
              break
    if a == '.':
        break
    print("yes" if c and not(b) else "no")




