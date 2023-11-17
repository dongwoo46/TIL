import sys
sys.stdin = open('input', 'r')

delta = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
T = int(input())

for tc in range(1,T+1):
    n = int(input())
    board = [input() for _ in range(n)]
    ans = 'NO'
    for x in range(n):
        for y in range(n):
            if board[x][y] == 'o':
                for dx,dy in delta:
                    cnt = 0
                    for i in range(5):
                        nx = x + dx*i
                        ny = y + dy*i
                        if 0<=nx<n and 0<=ny<n and board[nx][ny] == 'o':
                            cnt+=1
                        else:
                            break

                    if cnt == 5:
                        ans = 'YES'
                        break
            if ans == 'YES':
                break
        if ans == 'YES':
            break

    print(f'#{tc}', ans)














