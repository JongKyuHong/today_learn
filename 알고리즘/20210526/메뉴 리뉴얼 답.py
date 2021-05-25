from itertools import combinations
from collections import Counter

def solution(orders,course):
    answer = []

    for c in course:
        temp = []
        for order in orders:
            combi = combinations(sorted(order),c)
            temp += combi
        odict = Counter(temp)
        if odict:
            max_ = max(list(odict.values()))
            if max_ >= 2:
                for key, value in odict.items():
                    if odict[key] == max_:
                        answer.append(''.join(key))
    return sorted(answer)

print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))

## combinations은 조합에서 중복없이 permutation은 조합인데 전부다
## Counter는 동일한 값의 자료가 몇개인지 파악 나머지는 어려운거 없지?