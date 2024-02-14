import sys
from collections import deque

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == target:
            return graph[v]
        for next in (v-1, v+1, 2*v):
            if 0 <= next < MAX and not graph[next]:
                graph[next] = graph[v] + 1
                q.append(next)

MAX = 100001
start, target = map(int, sys.stdin.readline().split())
graph = [0] * MAX
print(bfs(start))