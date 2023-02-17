import sys
sys.stdin = open('input','r')
dx = [-1,1,0,0]
dy = [0,0,-1,1]
n =int(input())
board = [[0]*102 for _ in range(102)]
cnt = 0
for _ in range(n):
    s,e  = list(map(int,input().split()))
    for j in range(e, e + 10):
        for i in range(s,s+10):
            board[j][i] = 1



for row in board:
    cnt += row.count(1)
print(cnt)
