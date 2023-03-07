import sys
sys.stdin = open('input','r')

delta = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(x,y):
    ans_list = []
    q = [(x,y)]
    visited[x][y] = 1
    ans_list.append(board[x][y])
    while q:
        x,y= q.pop(0)
        for dx,dy in delta:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
                if abs(board[nx][ny] - board[x][y]) == 1:
                    visited[nx][ny] = 1
                    ans_list.append(board[nx][ny])
                    q.append((nx,ny))
    return min(ans_list), len(ans_list)




T = int(input())
for tc in range(1,T+1):
    n = int(input())
    visited = [[0] * n for _ in range(n)]
    board = [list(map(int,input().split())) for _ in range(n)]
    cnt = 0
    ans = n*n+1
    for x in range(n):
        for y in range(n):
            if visited[x][y] == 0:
                value, temp = bfs(x,y)
                if cnt<temp or cnt == temp and ans>value:
                    ans, cnt = value, temp




    print(f'#{tc}',ans,cnt)



