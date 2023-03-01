import sys
sys.stdin = open('input', 'r')






T = int(input())
for tc in range(1,T+1):
    n = int(input())
    board = [[0]*x for x in range(1,n+1)]
    for i in range(n):
        for j in range(i+1):
            if j == 0 or j == i:
                board[i][j] = 1
            else:
                board[i][j] = board[i-1][j-1]+board[i-1][j]

    print(f'#{tc}')
    for numb in board:
        print(*numb)



