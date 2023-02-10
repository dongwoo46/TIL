import sys
sys.stdin = open('input','r')

for _ in range(1,11):
    tc = int(input())
    board = [input() for _ in range(100)]
    col_board = [[board[j][i] for j in range(100)] for i in range(100)]
    row_str = 0
    max_row = 0
    col_str = 0
    max_col = 0


    for row in board:
        for i in range(100):
            for j in range(100):
                if row[i:j+i] == row[i:j+i][::-1]:
                    row_str = len(row[i:i+j])
                    if row_str > max_row:
                        max_row = row_str

    for col in col_board:
        for i in range(100):
            for j in range(100):
                if col[i:i+j] == col[i:i+j][::-1]:
                    col_str = len(col[i:i+j])
                    if col_str > max_col:
                        max_col = col_str

    print(f'#{tc}',max(max_col, max_row))




