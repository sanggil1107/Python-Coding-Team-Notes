## DFS(깊이우선 탐색) ##
def dfs(x):
  print(x, end = ' ')
  visited[x] = True
  for i in graph[x]:
    if not visited[i]:
      dfs(i)


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