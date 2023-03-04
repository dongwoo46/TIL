import sys
sys.stdin = open('input','r')
board = [[0]*101 for _ in range(101)]
for _ in range(4):
    x1,y1,x2,y2 = list(map(int,input().split()))
    for i in range(x1,x2):
        for j in range(y1,y2):
            board[i][j] = 1
cnt = 0
for x in range(101):
    for y in range(101):
        if board[x][y] == 1:
            cnt +=1

print(cnt)
