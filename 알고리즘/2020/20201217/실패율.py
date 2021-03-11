def solution(N, stages):
    answer = []
    stages.sort()
    newlist = [x for x in stages if x > N]
    newlen = len(newlist)
    dict = {}
    while N!=0:
        person = stages.count(N) # N스테이지에 머물고있는 사람 수
        if person + newlen == 0:
            dict[N] = 0
        else:
            diff = person/(newlen+person) # N스테이지의 난이도
            newlen += person
            dict[N] = diff
        N -= 1
    dict = sorted(sorted(dict.items()),key=lambda x : x[1],reverse=True)
    for i in dict:
        answer.append(i[0])
    return answer

print(solution(4,[4,4,4,4,4]))