from collections import deque
## BFS(너비우선 탐색) ##
def bfs(x):
  queue = deque([x])
  visited[x] = True

  while queue:
    v = queue.popleft()
    print(v, end = ' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

for e in graph:
  e.sort()

visited = [False] * (n+1)
dfs(start)