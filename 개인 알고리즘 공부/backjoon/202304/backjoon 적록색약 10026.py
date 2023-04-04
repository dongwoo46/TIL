# 백준 적록색약 10026

import sys
from collections import deque
sys.stdin = open('input','r')
input = sys.stdin.readline

# 정상 눈을 가진 갯수
def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
                if board[nx][ny] == board[x][y]:
                    q.append((nx,ny))
                    visited[nx][ny] = 1




n = int(input().rstrip())
board = [list(input()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
n_cnt = 0
d_cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i,j)
            n_cnt +=1

for i in range(n):
    for j in range(n):
        if board[i][j] == 'R':
            board[i][j] = 'G'

visited = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i,j)
            d_cnt +=1

print(n_cnt, d_cnt)