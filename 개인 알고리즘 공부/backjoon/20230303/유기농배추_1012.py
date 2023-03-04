import sys

sys.stdin = open('input','r')


delta = [(-1,0),(1,0),(0,-1),(0,1)]
def is_valid(x,y):
    return 0<=x<n and 0<=y<m
def bug(x,y):
    q = [(x,y)]
    board[x][y] = 2
    while q:
        x, y = q.pop(0)
        for dx,dy in delta:
            nx = x + dx
            ny = y + dy
            if is_valid(nx,ny) and board[nx][ny]==1:
                q.append((nx,ny))
                board[nx][ny] = 2

    return

T = int(input())
for tc in range(T):
    m,n,k = list(map(int,input().split()))
    board = [[0]*m for _ in range(n)]
    cnt = 0
    for _ in range(k):
        a,b = list(map(int,input().split()))
        board[b][a] = 1

    for x in range(n):
        for y in range(m):
            if board[x][y] == 1:
                cnt += 1
                bug(x,y)


    print(cnt)


