import collections
import sys
total_num = int(input())

def bfs():
    while(len(queue) != 0):
        x, y, visited, count = queue.popleft()
        visited[x] = False
        visited[y] = False
        flag = 0
        #print(x,y, visited, count)
        for temp in visited:
            if(temp):
                flag = 1
        if(flag == 0):
            total.append(count)
            break
        for k in range(a):
            if(matrix[y][k] == 1 and visited[k]):
                queue.append((y, k, visited, count+1))
total = []
for i in range(total_num):

    a, b = map(int, sys.stdin.readline().split())
    print(a,b)
    matrix = [[0] * a for i in range(a)]
    visited = [True for i in range(a)]
    for j in range(b):
        x, y = map(int, sys.stdin.readline().split())
        matrix[x-1][y-1] = 1
        matrix[y-1][x-1] = 1
    queue = collections.deque()
    for k in range(a):
        if(matrix[0][k] == 1):
            queue.append((0, k, visited, 1))
            bfs()
            break

for temp in total:
    print(temp)