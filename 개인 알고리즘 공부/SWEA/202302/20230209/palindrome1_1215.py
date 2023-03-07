import sys
sys.stdin = open('input', 'r')



for tc in range(1,11):
    length = int(input())
    board = [input()  for _ in range(8)]
    col_board = [[board[j][i] for j in range(8)] for i in range(8)]
    cnt = 0

    for row in board:
        for i in range(8-length +1):
            if row[i:i+length] == row[i:i+length][::-1]:
                cnt +=1

    for col in col_board:
        for i in range(8-length +1):
            if col[i:i + length] == col[i:i + length][::-1]:
                cnt += 1


    print(f'#{tc} {cnt}')
