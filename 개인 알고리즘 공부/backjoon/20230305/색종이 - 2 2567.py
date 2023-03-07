import sys
sys.stdin = open('input','r')
delta = [(-1,0),(1,0),(0,-1),(0,1)]
def is_valid(x,y):
    return 0<=x<101 and 0<=y<101
def count_side(x,y):
    cnt = 0
    if board[x][y] ==1:
        for dx,dy in delta:
            nx = x+dx
            ny = y+dy
            if is_valid(nx,ny) and  board[nx][ny]==0:
                cnt +=1
    return cnt
n = int(input())
board = [[0]*101 for _ in range(101)]
side = 0
for _ in range(n):
    a,b = list(map(int,input().split()))
    for i in range(a,a+10):
        for j in range(b,b+10):
            board[i][j] = 1
for x in range(101):
    for y in range(101):
        if count_side(x,y) == 1:
            side +=1
        elif count_side(x,y) == 2:
            side += 2

print(side)
