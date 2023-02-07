#우하좌상
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    board = [[0] * n for _ in range(n)]
    cnt = n
    x = 0
    y = 0
    numb = 1

    while numb != n ** 2:
        # 처음엔 오른쪽 진행 만약 y좌표가 n에 도달하면 break
        while board[x][y] == 0:
            if 0 <= y < n:
                board[x][y] = numb
                y = y + dy[0]
                numb += 1
            else:
                y -= 1
                break

        while board[x][y] == 0:
            if 0 <= x < n:
                x = x + dx[1]
                numb += 1
                board[x][y] = numb
            else:
                x -= 1
                break

        while board[x][y] == 0:
            if 0 <= y < n:
                numb += 1
                y = y + y[2]
                board[x][y] = numb
            else:
                y -= 1
                break

        while board[x][y] == 0:
            if 0 <= x < n:
                numb += 1
                x = x + dx[3]
                board[x][y] = numb
            else:
                x -= 1
                break

    if numb == n ** 2:
        break
    print(f'#{tc}', *board)