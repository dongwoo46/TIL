dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]
T = int(input())
for tc in range(1,T+1):
    n, m = map(int,input().split())
    board = [[0]*(n+2) for _ in range(n+2)]
    board[n//2][n//2] = board[n//2+1][n//2+1] = 2
    board[n//2][n//2+1]= board[n//2+1][n//2] = 1
    for i in range(m):
        loc_x, loc_y, color = list(map(int, input().split()))
        board[loc_x][loc_y] = color
        for direction in range(8):
            candidate = []
            for m in range(1,n):
                nx = loc_x + dx[direction]*m
                ny = loc_y + dy[direction]*m
                if board[nx][ny] == 0 : # 인덱스를 넘어 버리면 보드판 넘어버림
                    break
                elif board[nx][ny] != color: #다른 돌인 경우에 뒤집기 후보에추가
                    candidate.append((nx,ny))
                else: #같은돌 ->후보들을 뒤집고 종료
                    while candidate:
                        a,b = candidate.pop()
                        board[a][b] = color
                    break
    black = 0
    white = 0
    for row in board:
        black+= row.count(1)
        white+= row.count(2)
    print(f'#{tc}',{black} {white})



