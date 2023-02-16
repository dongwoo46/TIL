#상하좌우 상좌 상우 하좌 하우

n = int(input())
m = range(n)
dx = [-m,m,0,0,-m,-m,m,m]
dy = [0,0,-m,m,-m,m,-m,m]
visited = [[0]*n for _ in range(n)]

def is_valid(x,y,n):
    if 0<=x<n and 0<=y<n and visited == 0:
        True
    else:
        False

def queen(x,y):
    visited[x][y] = 1
    while m!= n-1:
        for direction in range(8):
            nx = x+dx[direction]
            ny = y+dy[direction]
            if is_valid(nx,ny,n):
                visited[nx][ny] = 1
            else:
                return

def location(x,y):
    for i in range(n):
        y=i
        if visited[x][y] == 0:
            visited[x][y] = 1
            queen(x,y)
            location(x+1,y)
        if x+1==n:
            return

n = int(input())
cnt = 0
x = 0
for i in range(n):
    location(x,y)


