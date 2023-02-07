import sys
sys.stdin = open('input','r')

#좌우상
dy = [-1,1,0]
dx = [0,0,1]


# for tc in range(1,11):
#     t = int(input())
board = [list(map(int, input().split())) for _ in range(10)]
ans = 0
temp = 0


for i in range(10):
    if board[9][i] == 2:
        temp = i
        x = 9
y = temp
x = 9

while 0<=x<10 and 0<=y <10:
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<=9 and 0<=ny<=9:
            if board[nx][ny] == 1:
                x = x +dx[0]
                y = y + dy[0]
    if x == 0:
        ans = y
        break




        # if k == 2 and board[nx][ny] == 0:
        #     break
        # if 0<=nx<100 and 0<=ny<100 and board[nx][ny] == 1:
        #     x = nx
        #     y = ny
        # elif nx>100 or nx<0 or ny>100 or ny<0:
        #     break
        # elif ny == 0 and 0<=nx<100 and 0<=ny<100 and board[nx][ny] == 1:
        #     x = nx
        #     y = ny
        #     ans = x
        #     break


    #
    # if board[x][y] == 2:
    #     ans = x_list.pop()
    #     break

print(f'#{t} {ans}')
    #
    #
    #
    #
