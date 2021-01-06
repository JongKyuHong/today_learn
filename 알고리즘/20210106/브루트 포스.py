iterable,visited = [1,2,3,4,5],[False]*5

def get_permutations(_currentIndex,_permutation):
    if _currentIndex == 5:
        print(_permutation)
        return
    for index, value in enumerate(iterable):
        if not visited[index]:
            visited[index], _permutation[_currentIndex] = True, value
            get_permutations(_currentIndex+1,_permutation)
            visited[index] = False

if __name__ == '__main__':
    get_permutations(0,[None]*5)


