import sys
sys.stdin= open('input','r')
delta= [(-1,0),(1,0),(0,-1),(0,1)]
def is_valid(x,y):
    return 0<=x<n and 0<=y<m

def ballon_pang():
    global total
    global max_total

    for x in range(n):
        for y in range(m):
            total = board[x][y]
            for dx,dy in delta:
                for i in range(1,board[x][y]+1):
                    nx = x + dx*i
                    ny = y + dy*i
                    if is_valid(nx,ny):
                        total += board[nx][ny]

            if total>max_total:
                max_total = total
    return max_total

T = int(input())
for tc in range(1,T+1):
    n,m = list(map(int,input().split()))
    board = [list(map(int,input().split())) for _ in range(n)]
    max_total = 0

    print(f'#{tc} {ballon_pang()}')
