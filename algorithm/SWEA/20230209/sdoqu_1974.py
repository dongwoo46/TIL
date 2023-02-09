import sys
sys.stdin = open('input','r')

T = int(input())

for tc in range(1,T+1):
    row_board = [list(map(int, input().split())) for _ in range(9)]
    col_board = [[row_board[j][i] for j in range(9)] for i in range(9)]

    ans = 1
    while True:
        for row in row_board:
            if len(set(row)) != 9:
                ans = 0
                break


        for col in col_board:
            if len(set(col)) != 9:
                ans =0
                break

        for i in range(9):
            for j in range(9):
                three_board = []
                if i%3==0 and j%3 == 0:
                    for k in range(i,i+3):
                        for l in range(j,j+3):
                          three_board.append(row_board[k][l])
                    if len(set(three_board)) != 9:
                        ans = 0
                        break
                if ans == 0:
                    break
            if ans == 0:
                break

        col_board.clear()
        row_board.clear()
        three_board.clear()
        break
    print(f'#{tc} {ans}')
