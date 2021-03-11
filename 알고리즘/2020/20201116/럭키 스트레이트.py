n = list(map(int,input()))

index = len(n) // 2
left = 0
right = 0
for i in range(index):
    left += n[i]
for i in range(index,len(n)):
    right += n[i]
if left == right:
    print("LUCKY")
else:
    print("READY")