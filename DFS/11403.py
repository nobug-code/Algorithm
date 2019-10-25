import sys
import time
'''
input() vs sys.stdin.readline()

속도면에서는 후자가 더 빠르다. 
why ? 
하지만 인터넷에서 찾아본 결과 꼭 sys.stdin.readline()
이 빠른 것이 아니라 오히려 readline().strip() 를 하는 상황에서는 input() 이 더 빠를 수 도 있다고 
설명한다. 오히려 여러 줄을 입력받을 경우 input이 더 좋을 수도 있다고 설명하고 있다. 
    input()     sys.stdin
3 - 1.3
7 - 0.37         0.3

속도는 비슷한것 같다. 
'''
scope = int(input())

def dfs(top, x, y):
    matrix[top][y] = 1
    vistied[top][y] = True
    for i in range(scope):
        if(matrix[y][i] == 1 and vistied[top][i] == False):
            dfs(top, y, i)


matrix = []
vistied = [ [False] * scope for i in range(scope)]

for i in range(scope):
    matrix.append(list(map(int, input().split(' '))))

#경로를 검색하는 문제이다. DFS로 어떻게 데이터를 업데이트를 할까 ?
for i in range(scope):
    for j in range(scope):
        if(matrix[i][j] == 1 and vistied[i][j] == False):
            dfs(i, i, j)

for i in range(scope):
    for j in range(scope):
        if(j == scope - 1):
            print(matrix[i][j])
        else:
            print(matrix[i][j], end=' ')
#폴로이드 워셜 알고리즘을 사용하면 간단히 풀수 있다.?
'''
그래프를 DFS 를 통해서 문제를 풀떄는 
무한 루프에 빠질 수 있기 때문에 방문 리스트를 사용해서 문제 해결 방식에 접근을 했다. 
DFS를 들어 갔을때 특정 행동을 해야 하는데 
정접 노드가 있으면 정접 노드에서 이어서 들어 가는 것이기 때문에 
a[top][x] -> a[x][y] 
만약 a[x][y]에 길이 존재 하면 a[top][y]도 길이 존재 한다고 코드를 수정해 주는 작업이 필요 했다. 
또 이때 a[top][y]는 방문했다는 것을 적어 줘야 한다. 

'''