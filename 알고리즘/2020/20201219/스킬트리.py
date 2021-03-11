def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        possible = True
        index = 0
        print(i+"여기")
        for j in range(len(i)):
            if i[j] in skill[index+1:]:
                index = 0
                possible = False
                print(j)
                break
            elif i[j] == skill[index]:
                index += 1
                if index == len(skill):
                    index = 0
        if possible:
            answer += 1
    return answer

print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))