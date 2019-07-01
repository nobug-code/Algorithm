'''
입력값 받는 부분 부터 정의 해야 한다.
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''
import sys
#DFS는 범위를 지정해 주고 범위를 돌아 다니며 조건을 만족시키면 재귀함수 식으로 호출을 한다.
#오른, 아래 , 왼, 위
arrow = [(0,1), (1,0), (0,-1), (-1,0)]

def dfs(matrix, count, x, y):

    matrix[x][y] = 0
    for _x,_y in arrow:
        c_y = y + _y
        c_x = x + _x
        #check
        if(c_x >= 0 and c_x < scope and c_y >= 0 and c_y < scope):
            if(matrix[c_x][c_y] == 1):
                count = dfs(matrix, count+1, c_x, c_y)
    return count

scope = int(sys.stdin.readline())
matrix = [list(map (int, sys.stdin.readline().strip())) for _ in range(scope)]
count = 0

ans = []
for x in range(scope):
    for y in range(scope):
        if(matrix[x][y] == 1):
            ans.append(dfs(matrix, 1, x, y))

ans = sorted(ans)
print(len(ans))
[print(i) for i in ans]