import sys
sys.stdin = open('input', 'r')
delta = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(x,y):
    q = [(x,y)]
    while q:
        x, y = q.pop(0)
        for dx,dy in delta:
            nx = x + dx
            ny = y + dy
            if 0<=nx<100 and 0<=ny<100:
                if maze[nx][ny] == 0:
                    maze[nx][ny] = 1
                    q.append((nx,ny))
                elif maze[nx][ny] == 3:
                    return 1
    return 0





for _ in range(1,11):
    tc = int(input())
    maze = [list(map(int,input())) for _ in range(100)]
    res = bfs(1,1)

    print(f'#{tc}', res)