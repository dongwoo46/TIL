import sys
sys.stdin = open('input','r')

#
# def delta(x,y):
#     for dx, dy in [(1,0),(0,1)]:
#         nx = x + dx
#         ny = y + dy
#         if 0<=nx<n and 0<=ny<n:
#             result[nx][ny] = min(board[x][y]+board[nx][ny],result[nx][ny])
#             x = nx
#             y = ny
#             if x == n-1 and y==n-1:
#                 return result[x][y]



INF = 1e9

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]
    result = [[INF]*n for _ in range(n)]
    for k in range(n):
        for a in range(n):
            for b in range(n):
                result[a][b] = min(board[a][b], board[a][k]+board[k][b])

    print(result[n-1][n-1])