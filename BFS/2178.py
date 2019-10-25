import sys
import queue

arrow = [(0, 1), (-1, 0), (0, -1), (1, 0)]
def bfs():

    while(q.empty() == False):
        t_y , t_x, count = q.get()
        #print(t_y, t_x)

       # print(t_y, t_x)

        if(t_y == y -1 and t_x == x -1):
            print(count + 1)
            break
        else:
            for temp in arrow:
                c_y, c_x = temp
                temp_y = t_y + c_y
                temp_x = t_x + c_x
                if(temp_y >= 0 and temp_x >= 0 and temp_y < y and temp_x < x):
                    if(matrix[temp_y][temp_x] == 1 and visited[temp_y][temp_x]):
                        visited[temp_y][temp_x] = False
                        q.put((temp_y, temp_x, count + 1))

y, x = map(int, input().split())
q = queue.Queue()
q.put((0,0,0))
matrix = [list(map(int, sys.stdin.readline().strip())) for i in range(y)]
visited = [[True]* x for i in range(y)]
visited[0][0] = False
bfs()