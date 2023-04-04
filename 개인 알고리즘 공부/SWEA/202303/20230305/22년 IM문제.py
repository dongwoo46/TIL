import sys
sys.stdin = open('input', 'r')
delta = [(-1,0),(1,0),(0,-1),(0,1)]
elect = ['A','B','C']
def is_valid(x,y):
    return 0<=x<n and 0<=y<n

def check(x,y):
    cnt = 0
    if ground[x][y] == 'A':
        for dx,dy in delta:
            nx = x + dx
            ny = y + dy
            if is_valid(nx,ny) and ground[nx][ny] == 'H'and board[nx][ny]==1:
                cnt +=1
                board[nx][ny] = -1

    elif ground[x][y] == 'B':
        for dx,dy in delta:
            for i in range(1,3):
                nx = x + dx*i
                ny = y + dy*i
                if is_valid(nx, ny)  and board[nx][ny] == 1:
                    cnt += 1
                    board[nx][ny] = -1
    elif ground[x][y] == 'C':
        for dx,dy in delta:
            for i in range(1,4):
                nx = x + dx*i
                ny = y + dy*i
                if is_valid(nx,ny) and board[nx][ny] == 1:
                    cnt += 1
                    board[nx][ny] = -1

    return cnt
# 집은 1 기지국은 2 없으면 0
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    ground = [input() for _ in range(n)]
    board = [[0]*n for _ in range(n)]

    total = 0
    for i in range(n):
        for j in range(n):
            if ground[i][j] == 'H':
                board[i][j] = 1
                total +=1
            elif ground[i][j] in elect:
                board[i][j] = 2

    for a in range(n):
        for b in range(n):
            if board[a][b] ==2:
                total -= check(a,b)

    print(f'#{tc}',total)




