from collections import deque

n = int(input())

graph = []
answer = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph,x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    cnt = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= len(graph) or ny < 0 or ny >= len(graph):
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
                cnt += 1
    return cnt


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1: 
            cnt = bfs(graph,i,j)
            answer.append(cnt)
answer.sort()


print(len(answer))
for k in answer:
    print(k)