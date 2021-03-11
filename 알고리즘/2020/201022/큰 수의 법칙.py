import sys

input = sys.stdin.readline
n,m,k = map(int,input().split())
data = list(map(int,input().split()))
data.sort()

data2 = data[-1]
data3 = data[-2]

count = int(m/(k+1))*k
count += m%(k+1)

result = 0
result += count * data2
result += (m-count) * data3

print(result)




