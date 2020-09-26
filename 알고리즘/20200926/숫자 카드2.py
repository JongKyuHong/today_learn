import sys

n = sys.stdin.readline()
list1 = sys.stdin.readline().rstrip().split(' ')
m = sys.stdin.readline()
list2 = sys.stdin.readline().rstrip().split(' ')
hash= {}
for n in list1:
    if n in hash:
        hash[n] += 1
    else:
        hash[n] = 1
print(' '.join(str(hash[m]) if m in hash else '0' for m in list2))

