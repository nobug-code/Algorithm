import sys
import collections

q = collections.deque()
x, y = map(int, input().split())
matrix = [list(map(int, sys.stdin.readline().split())) for i in range(y)]
#visited = [[True]*x for i in range(y)]

for i in range(y):
    for j in range(x):
        if(matrix[i][j] == 1):
            #visited[i][j] = False
            q.append((i, j, 1))
arrow = [(0,1), (-1,0), (0,-1), (1,0)]
total = 0
minus = 0
while(len(q) != 0):

    t_y, t_x, count = q.popleft()

    for temp_x, temp_y in arrow:
        c_x = t_x + temp_x
        c_y = t_y + temp_y

        if(c_x >= 0 and c_x < x and c_y >= 0 and c_y < y):
            if(matrix[c_y][c_x] == 0 and matrix[c_y][c_x] != -1):
                matrix[c_y][c_x] = count
                q.append((c_y, c_x, count + 1))

res =False
for x in matrix:
    if not all(x):
        res = True
        break

if(res):
    print(-1)
else:
    print(count - 1)




import collections

a, b = map(int, input().split())
matirx = []
for i in range(b):
    temp = list(map(int, input().split()))
    matrix.append(temp)
print(matrix)

queue = collections.deque()

for x in range(b):
    for y in range(a):
        if(matrix[x][y] == 1):
            queue.append((x, y, 0))

arrow = [(0, 1), (1, 0), (-1, 0), (0, -1)]
while(len(queue) != 0):
    x, y, count = queue.popleft()
    for t_x, t_y in arrow:
        c_x = x + t_x
        c_y = y + t_y
        #조건
        if(c_x < b and c_x >= 0 and c_y < a and c_y >= 0):

            if(matrix[c_x][c_y] != -1 and matrix[c_x][c_y] == 0):
                matrix[c_x][c_y] = 100
                queue.append((c_x, c_y, count + 1))

flag = 0
for x in range(b):
    for y in range(a):
        if(matrix[x][y] == 0):
            flag = 1
            break
if(flag == 1):
    print(-1)
else:
    print(count)