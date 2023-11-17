import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

def bfs(v):
    q = deque()
    q.append(v)
    check = [0 for _ in range(n)]
    while q:
        t = q.popleft()
        for i in range(n):
            if check[i]==0 and graph[t][i] == 1:
                visited[v][i] = 1
                q.append(i)
                check[i] = 1

for i in range(n):
    bfs(i)

for i in visited:
    print(*i)