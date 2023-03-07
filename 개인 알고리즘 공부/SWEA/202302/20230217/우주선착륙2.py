import sys
sys.stdin = open('input', 'r')

#상하좌우 상좌 상우 하좌 하우
dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]


T = int(input())
for tc in range(1,T+1):
    cnt = 0
    n,m = map(int, input().split())
    board = []
    result = 0
    for i in range(n):
        board.append(list(map(int,input().split())))

    for i in range(n):
        for j in range(m):
            x=i
            y=j
            cnt = 0
            for direction in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] < board[x][y]:
                    cnt +=1
            if cnt>=4:
                result += 1

    print(f'#{tc} {result}')


