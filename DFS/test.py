matrix = [[0, 1, 1, 0, 0],[1, 0, 0, 1, 1],[1, 0, 0, 0, 0],[0, 1, 0, 0, 0], [0, 1, 0, 0, 0]]
visited = [[0]*5 for i in range(len(matrix))]
dfs_list = []

def find_dfs(y):
    for t_y in range(len(matrix)):
        if(matrix[y][t_y] == 1 and visited[y][t_y] == 0):
                print(y, t_y)
                visited[y][t_y] = 1
                visited[t_y][y] = 1
                print(visited)
                dfs_list.append(t_y)
                find_dfs(t_y)

import queue

q = queue.Queue()
visited = [[0]*5 for i in range(len(matrix))]
dfs_list = []

for x in range(len(matrix)):
    if(matrix[0][x] == 1 and visited[0][x] == 0):
        visited[0][x] = 1
        visited[x][0] = 1
        dfs_list.append(x)
        q.put(x)

while(q.empty() == False):

    node = q.get()

    for i in range(len(matrix)):
        if (matrix[node][i] == 1 and visited[node][i] == 0):
            visited[node][i] = 1
            visited[i][node] = 1
            dfs_list.append(i)
            q.put(i)

print(dfs_list)
