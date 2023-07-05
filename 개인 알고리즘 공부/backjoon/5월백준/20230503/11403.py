import sys
from collections import deque
sys.stdin = open('input', 'r')

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

def bfs(v):
    q =deque()
    q.append(v)
    check = [0 for _ in range(n)]
    while q:
        t= q.popleft()
        for i in range(n):
            if board[t][i]==1 and check[i]==0:
                q.append(i)
                check[i] = 1
                visited[v][i] = 1

for i in range(n):
    bfs(i)

for visit in visited:
    print(*visit)
