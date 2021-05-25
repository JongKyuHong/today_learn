def solution(orders, course):
    answer = []
    answer2 = []
    counter = [0 for i in range(len(orders)+1)]
    for i in range(len(orders)):
        for j in range(i+1,len(orders)):
            array = lcs(orders[i], orders[j])
            answer.append(array)
    max1 = 0
    for i in course:
        for j in answer:
            if len(j) == i:
                if max1 <
                max1 = answer.count(i)
    for i in answer:
        if len(i) > 1:
            if i not in answer2:
                answer2.append(i)

    answer2.sort()
    return answer2
def lcs(arr1,arr2):
    array = ''
    new_arr = ''
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                array = array+arr2[j]
    for i in sorted(array):
        new_arr += i
    return new_arr

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))

