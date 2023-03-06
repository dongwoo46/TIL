import sys
sys.stdin = open('input','r')
n = int(input())
board = [list(input()) for _ in range(n)]

delta = [(1,0),(0,1)]
delta_r = [(-1,0),(1,0),(0,-1),(0,1)]

def is_valid(x,y):
    return 0<=x<n and 0<=y<n

max_cnt = 0

for x in range(n):
    for y in range(n):
        
        for dx,dy in delta:
            nx = x + dx
            ny = y + dy
            if is_valid(nx,ny):
                board[x][y],board[nx][ny] = board[nx][ny],board[x][y]
            for dx, dy in delta_r:
                cnt = 0
                for i in range(n):
                    nx = x + dx*i
                    ny = y + dy*i
                    if is_valid(nx,ny) and board[x][y] == board[nx][ny]:
                        cnt +=1
                    else:
                        continue
                max_cnt = max(max_cnt,cnt)
            if is_valid(nx,ny):
                board[nx][ny], board[x][y]  = board[x][y], board[nx][ny]

print(max_cnt)