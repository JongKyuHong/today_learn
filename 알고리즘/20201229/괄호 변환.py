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
        if i == ')':
            right_stack.append(1)
        else:
            try:
                right_stack.pop()
            except:
                return False
    return True

def solution(p):
    if p:
        u = make(p)
        v = p[len(u):]
        if right(u):
            solution(v)
        else:

    else:
        return p


    return answer