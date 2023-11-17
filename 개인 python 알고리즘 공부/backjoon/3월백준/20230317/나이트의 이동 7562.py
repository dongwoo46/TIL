import sys
sys.stdin = open('input', 'r')
from collections import deque

# 상상좌 상상우 하하좌 하하우 좌좌상 좌좌하 우우상 우우하
delta = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(1,-2),(-1,2),(1,2)]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    while q:
        x,y =q.popleft()
        for dx,dy in delta:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y]+1
                if nx == e_x and ny == e_y:
                    return visited[nx][ny]

T =int(input())
for tc in range(1,T+1):
    n = int(input())
    s_x ,s_y = map(int,input().split())
    e_x, e_y = map(int,input().split())

    visited= [[0]*n for _ in range(n)]
    if s_x == e_x and s_y == e_y:
        print(0)
    else:
        print(bfs(s_x,s_y))
