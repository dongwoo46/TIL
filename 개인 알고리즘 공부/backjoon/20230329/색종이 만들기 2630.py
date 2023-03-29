# 백준 색종이 만들기 2630

import sys
from collections import deque
sys.stdin = open('input','r')

def divide(board):
    if m <=1:
        return m

    mid = len(m)//2
    d1 = board[:mid][:mid]
    d2 = board[mid:][:mid]
    d3 = board[mid:]


def bfs(x,y,l):
    q = deque()
    q.append((x,y,l))

    visited[x][y] = board[x][y]
    while q:
        x, y, l = q.popleft()
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]
            nx = x + dx
            ny = y + dy
            if 0<=nx<l and 0<=ny<l and visited[nx][ny]==-1:
                q.append((nx,ny))
                visited[nx][ny] = board[nx][ny]


n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
visited = [[-1]*l for _ in range(l)] # 사각형의 길이
