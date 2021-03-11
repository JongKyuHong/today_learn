# itertools는 파이썬에서 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리이다.
# permutations, combinations등이 있다.
# permutations는 리스트와 같은 iterable 객체에서 r개의 데이털르 뽑아 일려로 나열하는 모든
# 경우를 계산해준다

from itertools import permutations

data = ['A','B','C']
result = list(permutations(data,3))
print(result)

# 결과 : [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

# combinations는 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고
# 나열하는 모든 경우 (조합)를 계산한다.
from itertools import combinations
data = ['A','B','C']
result = list(combinations(data,2))
print(result)

# 결과 : [('A', 'B'), ('A', 'C'), ('B', 'C')]\

# product는 permutations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는
# 모든 경우(순열)를 계산한다. 다만 원소를 중복하여 뽑는다.

from itertools import product

data = ['A','B','C']
result = list(product(data,repeat=2)) # 2개를 뽑는 모든 순열 구하기(중복허용)
print(result)

#결과 : [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

# combinations_with_replacement는 combinations와 같이 리스트와 같은 iterable 객체에서 r개의
# 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산한다.
from itertools import combinations_with_replacement

data = ['A','B','C']
result = list(combinations_with_replacement(data,2))
print(result)

# 결과 : [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]