#이 문제를 접근해서 푸는 방식은 재귀함수로 접근하고 있다.

import sys
sys.setrecursionlimit(100000)
total_num = int(input())
each_ans = []
#오른쪽, 아래, 왼쪾, 위쪽
arrow = [(0,1), (1,0), (0,-1), (-1,0)]

def dfs(matrix, count, temp_y, temp_x):

    matrix[temp_y][temp_x] = 0

    for c_arrow in arrow:
        c_x = c_arrow[1]
        c_y = c_arrow[0]
        t_x = temp_x + c_x
        t_y = temp_y + c_y

        if(t_x >= 0 and t_x < x and t_y >= 0 and t_y < y):
            if(matrix[t_y][t_x] == 1):
                dfs(matrix, count+1, t_y, t_x)

for i in range(total_num):

    count = 0
    x, y, scope = map(int, input().split(' '))
    matrix = [[0]* x for i in range(y)]

    #Make Map
    for i in range(scope):
        temp = input().strip()
        t_x, t_y = map(int, temp.split(' '))
        matrix[t_y][t_x] = 1

    #DFS
    for i in range(y):
        for j in range(x):
            if(matrix[i][j] == 1):
                dfs(matrix, count+1, i, j)
                count += 1
    each_ans.append(count)

for i in each_ans:
    print(i)