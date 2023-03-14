from collections import deque
import sys
sys.stdin = open('input','r')

def bfs(v):
    global cnt
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        t = q.popleft()
        for i in graph[t]:
            if not visited[i]:
                visited[i] = visited[t] + 1
                cnt += 1
                q.append(i)
    return cnt


computer = int(input())
n = int(input())
graph = [[] for _ in range(computer + 1)]
visited = [0] * (computer + 1)
cnt = 0

for i in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(1))