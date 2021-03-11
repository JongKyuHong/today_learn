import sys

n,m = list(map(int,sys.stdin.readline().rstrip().split(' ')))
tree = list(map(int,sys.stdin.readline().rstrip().split(' ')))
start = 1
end = max(tree)

while start <= end:
    sum = 0
    mid = (start+end)//2
    for i in tree:
        if mid <= i:
            sum += i - mid

    if m > sum:
        end = mid-1
    else:
        start = mid+1
print(end)


