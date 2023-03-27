import sys
from collections import deque
sys.stdin = open('input')

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1
    while q:
        t = q.pop(0)
        for i in graph[t]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)

n,m =map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

cnt = 0
while 0 in visited:
    for i in range(n+1):
        if visited[i] == 0:
            bfs(i)
            cnt+=1
print(cnt)

