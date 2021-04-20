def solution(N,number):
    a = [0,[N]]
    if N == number:
        return 1
    for i in range(2,9):
        case_set = []
        basic_num = int(str(N)*i)
        case_set.append(basic_num)
        for j in range(1,i//2+1):
            for x in a[j]:
                for y in a[i-j]:
                    case_set.append(x+y)
                    case_set.append(x-y)
                    case_set.append(y-x)
                    case_set.append(x*y)
                    if y!=0:
                        case_set.append(x/y)
                    if x!=0:
                        case_set.append(y/x)
            if number in case_set:
                return i
            a.append(case_set)
            print(a)
    return -1
N,number = map(int,input().split())
print(solution(N,number))