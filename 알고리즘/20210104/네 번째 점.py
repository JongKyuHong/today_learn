a1,a2 = input().split()
b1,b2 = input().split()
c1,c2 = input().split()

if a2 == b2:
    d2 = c2
elif a2 == c2:
    d2 = b2
else:
    d2 = a2

if a1 == b1:
    d1 = c1
elif a1 == c1:
    d1 = b1
else:
    d1 = a1

print(d1, d2)

