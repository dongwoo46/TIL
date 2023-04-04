import sys
sys.stdin = open('input', 'r')

delta = [(-1,0),(1,0),(0,-1),(0,1)]
delta_diag = [(-1,-1),(-1,+1),(1,-1),(1,1)]

def is_valid(x,y):
    return 0<=x<n and 0<=y<n

def kill_delta(x,y):
    cnt_delta = board[x][y]
    for dx,dy in delta:
        for i in range(1,m):
            nx = x + dx*i
            ny = y + dy*i
            if is_valid(nx,ny):
                cnt_delta += board[nx][ny]
    return cnt_delta

def kill_diag(x,y):
    cnt_diag = board[x][y]
    for dx,dy in delta_diag:
        for i in range(1,m):
            nx = x + dx*i
            ny = y + dy*i
            if is_valid(nx,ny):
                cnt_diag += board[nx][ny]
    return cnt_diag

T = int(input())
for tc in range(1,T+1):
    n,m = list(map(int,input().split()))
    board = [list(map(int,input().split())) for _ in range(n)]
    max_cnt = 0
    ans = 0
    for x in range(n):
        for y in range(n):
            max_cnt = max(kill_delta(x,y),kill_diag(x,y))
            if ans < max_cnt:
                ans = max_cnt

    print(f'#{tc}',ans)



