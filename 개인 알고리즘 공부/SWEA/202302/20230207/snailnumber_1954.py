import sys
sys.stdin = open('input', 'r')
#우하좌상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    board = [[0] * (n) for _ in range(n)]
    x = 0
    y = -1
    numb = 1
    direction = 0

    while numb <= n ** 2:
        x = x + dx[direction]
        y = y + dy[direction]
    # !!!! and문을 쓸 때  여기처럼 board[x][y]==0을 x,y의 범위보다 먼저쓰면 x,y값이 인덱스를 벗어난 상태로 board[x][y]를
    # 먼저 탐색하기 때문에 board[x][y]의 인덱스가 벗어났다고 런타임 에러가 뜬다!!!
    # 따라서 x, y의 좌표가 먼저 벗어나는지 확인하고 만약 x,y가 허용범위안에 있는것이 확인되고 board[x][y] ==0 인지 확인해야함!
        if  0<=x<n and 0<=y<n and board[x][y] ==0 :
            board[x][y] = numb
            numb +=1

        elif x>=n or x<0 or y>=n or y<0 or board[x][y] != 0:
            x = x - dx[direction]
            y = y - dy[direction]
            direction = (direction+1)%4


    print(f'#{tc}')
    for row in board:
        print(*row)