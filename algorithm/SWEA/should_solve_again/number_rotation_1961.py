import sys
sys.stdin = open('../20230209/input', 'r')

T = int(input())

for tc in range(1,T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    board_90 = [[0]*n for _ in range(n)]
    board_180 = [[0]*n for _ in range(n)]
    board_270 = [[0]*n for _ in range(n)]

    #90도회전
    for i in range(n):
        for j in range(n-1,-1,-1):
            board_90[j][i] += board[i][j]


    # 741
    # 852
    # 963

    #180도 회전
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            board_180[i][j] += board[i][j]

    # 987
    # 654
    # 321

    #270도회전
    for i in range(n):
        for j in range(n-1,-1,-1):
            board_270[j][i] += board[i][j]
    # 369
    # 258
    # 147
    print(f'#{tc}')
    for i in range(n):
        for j in range(n):
            print(board_90[i][j], end='')
        print(end=' ')
        for k in range(n):
            print(board_180[i][k], end='')
        print(end=' ')
        for l in range(n):
            print(board_270[i][l], end='')
        print()
