import sys
import collections

queue = collections.deque()

n, k, m = map(int, sys.stdin.readline().split())

#n 의 도착 할꺼야 1번 부터 시작해서
matrix = [[i] for i in range(n + m + 1)]
vistied = [True for i in range(n + m + 1)]
last_start = n + 1

for i in range(m):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in temp:
        matrix[j].append(last_start)
        matrix[last_start].append(j)
    last_start += 1

print(matrix)

queue.append((1,0))
vistied[1] = False
#BFS
flag = 0
while(len(queue) != 0):

    x, count = queue.popleft()
    #print(x, count)
    if(x == n):
        flag = 1
        print(count)
        break

    for i in matrix[x]:
      #  print(matrix[x])
        if(vistied[i]):
            if(i > n):
                count = count + 1
            vistied[x] = False
            queue.append((i, count))

if(flag == 0):
    print(-1)