import sys, math

a,b,v = list(map(int,sys.stdin.readline().rstrip().split(' ')))
print(math.ceil((v-a)/(a-b))+1)