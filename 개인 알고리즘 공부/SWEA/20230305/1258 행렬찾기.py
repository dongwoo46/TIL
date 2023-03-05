import sys
sys.stdin = open('input','r')

def is_valid(x,y):
    return 0<=x<n and 0<=y<n
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    result = []
    ans = []


    for x in range(n):
        for y in range(n):
            cnt_x = 0
            cnt_y = 0
            if board[x][y] !=0 and visited[x][y] == 0:
                for i in range(n):
                    nx = x + i
                    ny = y
                    if is_valid(nx,ny) and visited[nx][ny]==0 and board[nx][ny]!=0:
                        visited[nx][ny] = 1
                        cnt_x +=1
                    else:
                        break
                visited[x][y] = 0
                for i in range(n):
                    nx = x
                    ny = y + i
                    if is_valid(nx, ny) and visited[nx][ny] == 0 and board[nx][ny] != 0:
                        visited[nx][ny] = 1
                        cnt_y += 1
                    else:
                        break
                result.append((cnt_x,cnt_y,cnt_x*cnt_y))


                for a in range(x,x+cnt_x):
                    for b in range(y,y+cnt_y):
                        visited[a][b] = 1

    result.sort(key=lambda x:x[2])
    for k in range(len(result)-1):
        if result[k][0]*result[k][1] == result[k+1][0]*result[k+1][1]:
            if result[k][0]>result[k+1][0]:
                result[k],result[k+1] = result[k+1],result[k]

    print(f'#{tc}',len(result),end=' ')
    for ans in result:
        print(ans[0],ans[1], end=' ')
    print()

