import sys
sys.stdin = open('input', 'r')

T = int(input())

for tc in range(1,T+1):
    n, m = list(map(int,input().split()))
    board = [input() for _ in range(n)]
    col_board = [[board[j][i] for j in range(n)] for i in range(n)]
    palindrome = []

    for row in board:
        for i in range(n-m+1):
            if row[i:i+m] == row[i:i+m][::-1]:
                palindrome.append(row[i:i+m])

    for col in col_board:
        for j in range(n-m+1):
            if ''.join(col)[j:j+m] == ''.join(col)[j:j+m][::-1]:
                palindrome.append(''.join(col)[j:j+m])


    print(f'#{tc}', *palindrome)

