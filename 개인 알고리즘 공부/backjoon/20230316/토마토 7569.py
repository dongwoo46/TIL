import sys
from collections import deque
sys.stdin = open('input','r')
def bfs():
    q = deque()
    for z in range(l):
        for x in range(m):
            for y in range(n):
                if board[z][x][y] == 1:
                    q.append((z, x, y))
    while q:
        z,x,y = q.popleft()
        for dx,dy,dz in [(1,0,0),(-1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
            nx = x+dx
            ny = y+dy
            nz = z+dz
            if 0<=nz<l and 0<=nx<m and 0<=ny<n and board[nz][nx][ny]==0:
                board[nz][nx][ny] = board[z][x][y]+1
                q.append((nz,nx,ny))


n,m,l = map(int,input().split())
board = [[list(map(int,input().split())) for _ in range(m)] for _ in range(l)]
ans = 0
bfs()
for i in board:
    for j in i:
        for k in j:
            if k == 0:
                ans = -1
                print(ans)
                exit()
            ans = max(ans,k)
print(ans-1)







