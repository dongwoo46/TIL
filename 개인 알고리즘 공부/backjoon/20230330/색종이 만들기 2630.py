# 백준 색종이 만들기 2630

import sys

sys.stdin = open('input','r')

def paper(x,y,n):
    for i in range(x,x+n//2):
        for j in range(y,y+n//2):
            first = board[x][y]
            if first!=board[i][j]:
                paper(x,y,n//2)




n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
for i in range()
