n = int(input())
array = list(map(int,input().split()))
array.sort()
m = int(input())
array2 = list(map(int,input().split()))

def binary(start,end,array,target):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
        else:
            return True
    return False
for i in array2:
    if binary(0,n-1,array,i):
        print("yes")
    else:
        print("no")
