import sys

sys.stdin = open('input', 'r')
#하상우좌
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
#x<0 and x>n-1 and y<0 and y>m-1
T = int(input())

for tc in range(1, T + 1):
    n, m = list(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    max_cnt = 0
    for x in range(0, n):
        for y in range(0, m):
            cnt = 0
            cnt += board[x][y]
            if x+1<n:
                x += dx[0]
                y += dy[0]
                cnt += board[x][y]
                x -= dx[0]
                y -= dy[0]
            if x-1>=0:
                x += dx[1]
                y += dy[1]
                cnt += board[x][y]
                x -= dx[1]
                y -= dy[1]

            if y+1<m:
                x += dx[2]
                y += dy[2]
                cnt += board[x][y]
                x -= dx[2]
                y -= dy[2]
            if y-1>=0:
                x += dx[3]
                y += dy[3]
                cnt += board[x][y]
                x -= dx[3]
                y -= dy[3]


            if max_cnt < cnt:
                max_cnt = cnt

    print(f'#{tc} {max_cnt}')






