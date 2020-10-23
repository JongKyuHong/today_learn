
n = int(input())

data = list(input().split())

#location = [1,1]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
x = 1
y = 1

for i in data:
   if i == "D":
     nx = x + dx[0]
     ny = y + dy[0]
   elif i == 'U':
     nx = x + dx[1]
     ny = y + dy[1]
   elif i == 'R':
     nx = x + dx[2]
     ny = y + dy[2]
   elif i == 'L':
     nx = x + dx[3]
     ny = y + dy[3]
   if nx < 1 or nx > n or ny > n or ny < 1:
       continue
   x = nx
   y = ny
print(x, y)