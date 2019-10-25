import sys
import queue

n, m, v = map(int, input().split())

matrix = [[0]*n for i in range(n)]
vertex = [0 for i in range(n)]

def dfs(top, y, ans):

    if(vertex[y] == 0):
        ans.append(y+1)
        vertex[y] = 1
    for j in range(n):
        if(matrix[y][j] == 1 and vertex[j] == 0):
            dfs(y, j, ans)

def bfs(q):
    q.put(v-1)
    vertex[v-1] = 1

    while(q.empty() == False):
        top = q.get()
        for j in range(n):
            if (matrix[top][j] == 1 and vertex[j] == 0):
                bfs_list.append(j+1)
                vertex[j] = 1
                q.put(j)

#Input data
for i in range(m):
    a, b = map(int, input().split())
    matrix[a-1][b-1] = 1
    matrix[b-1][a-1] = 1

dfs_list = []


#DFS
top = v - 1
vertex[top] = 1
dfs_list.append(top +1)
for j in range(n):
    if(matrix[top][j] == 1 and vertex[j] == 0):
            dfs(top ,j, dfs_list)


#BFS
top = v - 1
vertex[top] = 1
bfs_list = []
q = queue.Queue()
bfs_list.append(top +1)
vertex = [0 for i in range(n)]
bfs(q)
for i in dfs_list:
    print(i ,end=' ')

print()

for i in bfs_list:
    print(i ,end=' ')