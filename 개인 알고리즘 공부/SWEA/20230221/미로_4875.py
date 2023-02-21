import sys
sys.stdin = open('input','r')
delta = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(x,y):
    q = [(x,y)]
    while q:
        x, y = q.pop(0)
        for dx,dy in delta:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<n:
                if maze[nx][ny] == 0:
                    maze[nx][ny] = 1
                    q.append((nx,ny))
                elif maze[nx][ny] == 3:
                    return 1
    return 0




T = int(input())
for tc in range(1,T+1):
    n = int(input())
    maze = [list(map(int,input())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                res = bfs(i,j)

    print(f'#{tc}', res)