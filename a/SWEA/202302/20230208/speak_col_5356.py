import sys
sys.stdin = open('input', 'r')
T = int(input())

for tc in range(1,T+1):
    row_board = [list(map(str, input())) for _ in range(5)]
    empty_board = [[0]*15 for _ in range(15)]
    ans = ''

    for i in range(5):
        for j in range(len(row_board[i])):
            empty_board[i][j] = row_board[i][j]

    for i in range(15):
        for j in range(15):
            if empty_board[j][i] != 0:
                ans += empty_board[j][i]

    print(f'#{tc} {ans}')