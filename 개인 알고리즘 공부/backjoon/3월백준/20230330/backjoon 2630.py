# 백준 색종이 만들기 2630

import sys

sys.stdin = open('input', 'r')

def paper(x,y,n):
    global white
    global blue
    for i in range(x,x+n):
        for j in range(y,y+n):
            first = board[x][y]
            if first!=board[i][j]:
                paper(x,y,n//2)
                paper(x,y+n//2,n//2)
                paper(x+n//2,y,n//2)
                paper(x+n//2,y+n//2,n//2)
                return
    if first == 0:
        white +=1
    else:
        blue +=1




n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
white=blue=0
paper(0,0,n)
print(white)
print(blue)
