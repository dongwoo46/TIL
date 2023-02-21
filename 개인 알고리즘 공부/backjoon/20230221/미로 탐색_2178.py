import sys
sys.stdin = open('input','r')

delta = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(x,y,cnt):
    q = [(x,y,cnt)]
    while q:
        x,y,cnt = q.pop(0)
        for dx,dy in delta:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<m:
                if maze[nx][ny] == 1:
                    maze[nx][ny] = 0
                    q.append((nx,ny,cnt+1))
                elif x == n-1 and y == m-1:
                    return cnt

n,m = list(map(int,input().split()))
maze = [list(map(int, input())) for _ in range(n)]
print(bfs(0,0,1))






