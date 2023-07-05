import sys
sys.stdin = open('input.txt')
from collections import deque
n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
sum_square = 0
tetris=[[(0,0),(0,1),(0,2),(0,3)],
        [(0,0),(1,0),(2,0),(3,0)],
        [(0,0),(1,0),(0,1),(1,1)],
        [(0,0),(1,0),(2,0),(2,1)],
        [(0,1),(1,1),(2,1),(2,0)],
        [(0,0),(0,1),(1,1),(2,1)],
        [(0,0),(0,1),(1,0),(2,0)],
        [(0,0),(1,0),(1,1),(1,2)],
        [(0,2),(1,1),(1,2),(1,0)],
        [(0,0),(0,1),(0,2),(1,2)],
        [(0,0),(1,0),(0,1),(0,2)],
        [(0,0),(1,0),(1,1),(2,1)],
        [(0,1),(1,1),(1,0),(2,0)],
        [(1,0),(1,1),(0,1),(0,2)],
        [(0,0),(0,1),(1,1),(1,2)],
        [(0,1),(1,0),(1,1),(1,2)],
        [(0,0),(0,1),(0,2),(1,1)],
        [(0,0),(1,0),(1,1),(2,0)],
        [(0,1),(1,1),(1,0),(2,1)]]
mx = -1

# def bfs(a,b):
#     global mx
#     visited = [[0] * m for _ in range(n)]
#     max_board = [[0] * m for _ in range(n)]
#     q = deque()
#     q.append((a,b))
#     visited[a][b] = 1
#     max_board[a][b] = board[a][b]
#     while q:
#         x,y = q.popleft()
#         for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
#             nx = x + dx
#             ny = y + dy
#             if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0:
#                 q.append((nx,ny))
#                 max_board[nx][ny] = max_board[x][y] + board[nx][ny]
#                 visited[nx][ny] = visited[x][y] + 1
#                 if visited[nx][ny] == 5:
#                     return
#                 else:
#                     if max_board[nx][ny] > mx:
#                         mx = max_board[nx][ny]
#

def bfs2(a,b):
    global mx,s,tetris
    for square in tetris:
        total = 0
        for dx,dy in square:
            nx = a + dx
            ny = b + dy
            if 0<=nx<n and 0<=ny<m:
                total += board[nx][ny]
            else:
                break
        if total>=mx:
            mx = total
    return mx

for i in range(n):
    for j in range(m):
        # bfs(i,j)
        bfs2(i,j)

print(mx)