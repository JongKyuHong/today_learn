import sys

n = int(sys.stdin.readline().rstrip())
data = list(map(int,input().split()))
m = int(sys.stdin.readline().rstrip())
data2 = list(map(int,input().split()))


def binary_search(data,target,start,end):
    while end>=start:
        mid = (start+end)//2
        if data[mid] == target:
            return mid
        elif data[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in data2:
    result = binary_search(data,i,0,n-1)
    if result:
        print("yes",end=' ')
    else:
        print("no",end=' ')










