# 백준 1074 Z
import sys
sys.stdin = open('input')

def divide(x,y,n):
    if n == 2:
        full(x,y,n)
        return
    else:
        for i in range(x,x+n):
            for j in range(y,y+n):
                divide(x,y,n//2)
                divide(x,y+n//2,n//2)
                divide(x+n//2,y,n//2)
                divide(x+n//2,y+n//2,n//2)
                return


def full(board,x,y,n):
    global cnt
    for i in range(x,x+n):
        for j in range(y, y+n):
            board[i][j] = cnt
            cnt+=1


N, r, c = map(int,input().split())

# board = [[0]*(2**N) for _ in range(2**N)]
cnt = 0
result = []
if 2**n//2 >r and 2**n> c:
    divide()
divide(0,0,2**N)
print(board[r][c])