import math

a,b,v = map(int,input().split())
daycut = a-b
days = 0
days = (v-a)/daycut
print(math.ceil(days+1))

