import sys
sys.stdin = opne('input','r')

T = int(input())

for tc in range(1,T+1):
    n = int(input())
    board = [list(map(int,input().split())) for _in range(n)]
    board_90 = [[0]*n for _ in range(n)]
    board_180 = [[0]*n for _ in range(n)]
    board_270 = [[0]*n for _ in range(n)]

    #90도회전
    for i in range(2, -1, -1):
        for j in range(3):
            board_90[i][j]=+board[j][i]

    # 741
    # 852
    # 963

    #180도 회전
    for i in range(2,-1,-1):
        for j in range(2, -1, -1):
            board_180[i][j] += board[i][j]

    # 987
    # 654
    # 321

    #270도회전
    for i in range(3):
        for j in range(2, -1, -1):
            board_270[i][j] += board[j][i]
    # 369
    # 258
    # 147

    for i in range(n):

        print(f'#{tc}',)