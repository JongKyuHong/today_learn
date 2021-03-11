def solution(s):
    answer = 0
    zip = 1
    string = ''
    Drainage = 1
    while (len(s)/2) != zip:
        commit = [s[i:i + zip] for i in range(0, len(s), zip)]
        for i in range(len(commit)-1):
            if commit[i] == commit[i+1]:
                Drainage += 1
            else:
                if Drainage == 1:
                    string += str(commit[i])
                else:
                    string += str(Drainage)+str(commit[i])
                    Drainage = 1
        zip += 1
        answer = len(string)
        print(string)
        string =''
    return answer

print(solution('aabbaccc'))



