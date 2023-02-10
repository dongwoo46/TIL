import sys
sys.stdin = open('input','r')

#상좌우

dx = [-1,0,0]
dy = [0,-1,1]

for tc in range(1, 11):
    t = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if board[99][i] == 2:
            y = i

    x = 99
    direction = 0

    while True:
        if x == 0:
            break
        # 좌로 가기
        if 0<=x<100 and 0<y<=99 and board[x][y-1] == 1:
            direction = 1
            while True:
                x = x + dx[direction]
                y = y + dy[direction]
                if (y-1)<0 or board[x][y-1] != 1:
                    break
        elif 0<=x<100 and 0<=y<99 and board[x][y+1] == 1:
            direction = 2
            while True:
                x = x + dx[direction]
                y = y + dy[direction]
                if (y+1)>99 or board[x][y+1]!=1:
                    break

        direction = 0
        x = x + dx[direction]
        y = y + dy[direction]

    print(f'#{tc} {y}')