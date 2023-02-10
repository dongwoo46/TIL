import sys
sys.stdin = open('input.txt', 'r')
#좌 우 하
dx = [0,0,1]
dy = [-1,1,0]

for _ in range(1, 11):
    tc = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]
    start_y = []
    minnimum = 1000000

    x = 0
    for i in range(100):
        if board[0][i] ==1:
            start_y.append(i)

    for y in start_y:
        x = 0
        move = 0
        move_list = []
        temp = y

        while True:
            if x == 99:
                break

            if 0<y<=99 and board[x][y-1]==1:
                direction = 0
                while True:
                    x +=dx[direction]
                    y +=dy[direction]
                    move += 1
                    if y-1<0 or board[x][y-1]==0:
                        break
            elif 0<=y<99 and board[x][y+1]==1:
                direction = 1
                while True:
                   x += dx[direction]
                   y += dy[direction]
                   move += 1
                   if y+1>99 or board[x][y+1] == 0:
                       break
            direction = 2
            x += dx[direction]
            y += dy[direction]
            move += 1

        if minnimum > move:
            minnimum = move
            ans = temp

    print(f'#{tc} {ans}')
