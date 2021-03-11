def make(p):
    u = ''
    left_side = 0
    right_side = 0
    for i in p:
        if i == ')':
            left_side += 1
            u += i
        else:
            right_side += 1
            u += i
        if right_side > 0 and left_side > 0 and left_side == right_side:
            return u

def right(p):
    right_stack = []
    for i in p:
        if i == '(':
            right_stack.append(1)
        else:
            try:
                right_stack.pop()
            except:
                return False
    return True

def make_f(u,v):
    stack = []
    new_u = ''
    stack.append("(")
    stack.append(solution(v))
    stack.append(")")
    for i in range(len(u)):
        if i == 0:
            continue
        elif i == len(u)-1:
            continue
        else:
            if u[i] == ')':
                new_u += '('
            else:
                new_u += ')'
    stack.append(new_u)
    return ''.join(stack)

def solution(p):
    answer = ''
    if right(p):
        return p
    if p:
        u = make(p)
        v = p[len(u):]
        if right(u):
            answer += u
            answer += solution(v)
        else:
            answer += make_f(u,v)
    else:
        return p
    return answer

print(solution('()))((()'))
