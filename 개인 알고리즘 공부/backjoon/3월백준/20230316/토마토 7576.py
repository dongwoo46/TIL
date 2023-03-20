import sys
from collections import deque
sys.stdin = open('input', 'r')
def bfs():
    q = deque()
    for x in range(m):
        for y in range(n):
            if board[x][y] == 1:
                q.append((x, y))
    while q:
        x,y = q.popleft()
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx = x+dx
            ny = y+dy
            if 0<=nx<m and 0<=ny<n and board[nx][ny]==0:
                board[nx][ny] = board[x][y]+1
                q.append((nx,ny))


n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(m)]
visited = [[0]*n for _ in range(m)]
ans = 0
bfs()
for i in board:
    for j in i:
        if j == 0:
            ans = -1
            print(ans)
            exit()
        ans = max(ans,j)
print(ans-1)







