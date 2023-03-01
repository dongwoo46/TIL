import sys
sys.stdin = open('../20230209/input', 'r')

def rotation(arr,n):
    new_board = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_board[i][j] = arr[n-1-j][i]
    return new_board

T = int(input())

for tc in range(1,T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    #90도회전
    board_90 = rotation(board, n)
    board_180 = rotation(board_90,n)
    board_270 = rotation(board_180,n)

    # 369
    # 258
    # 147
    print(f'#{tc}')
    for i in range(n):
        print("".join(map(str, board_90[i])), end=" ")
        # print("".join(map(str, board_180[i])), end=" ")
        print()
    # for i in range(n):
    #     for j in range(n):
    #         print(board_90[i][j], end='')
    #     print(end=' ')
    #     for k in range(n):
    #         print(board_180[i][k], end='')
    #     print(end=' ')
    #     for l in range(n):
    #         print(board_270[i][l], end='')
    #     print()
