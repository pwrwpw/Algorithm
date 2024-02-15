
n = int(input())

graph = []
visited = [0] * n
min_value = 1e3
for _ in range(n):
    graph.append(list(map(int,input().split())))

def dfs(depth,index):
    global min_value
    if depth == n//2:
        a, b = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    a += graph[i][j]
                elif not visited[i] and not visited[j]:
                    b += graph[i][j]
        min_value = min(abs(a-b),min_value)
        return

    for i in range(index,n):
        if not visited[i]:
            visited[i] = 1
            dfs(depth+1, i+1)
            visited[i] = 0

dfs(0,0)
print(min_value)