#상하좌우 우측아래대각 좌측아래 대각
dx = [-1,1,0,0,1,1]
dy = [0,0,-1,1,1,-1]

n = int(input())
board = [list(map(int,input().split())) for _ in range(3)]



def check(board):
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        x = 0
        y = i
        visited[x][y] = 1
    for direction in range(4):
        x += dx[direction]
        y += dy[direction]
        if  0<=x<n and 0<=y<n and visited[x][y]==0:
            visited[x][y] = 1

def move(board):
    for j in range(5,7):





