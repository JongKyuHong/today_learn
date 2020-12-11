from itertools import permutations
import math

def check(number):
    k = math.sqrt(number)

    if number < 2:
        return False

    for i in range(2,int(k)+1):
        if number % i == 0:
            return False
    return True


def solution(numbers):
    answer = []
    for i in range(1,len(numbers)+1):
        perlist = list(map(''.join,permutations(list(numbers),i)))
        print(perlist)
        for k in list(set(perlist)):
            if check(int(k)):
                answer.append(int(k))
    answer = len(set(answer))
    return answer



