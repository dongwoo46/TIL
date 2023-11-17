import sys
sys.stdin = open('input', 'r')
def up_total(x,y):
    global total_up
    global m
    while x!=n//2:
        for i in range(m+1):
            total_up += board[x][y+i]
            total_up += board[x][y-i]
        m+=1
        x+=1
    return total_up

def down_total(x,y):
    global total_down
    global m
    m = m-1
    while x<n:
        for i in range(m+1):
            total_down += board[x][y+i]
            total_down += board[x][y-i]
        m-=1
        x+=1
    return total_down

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    board = [list(map(int,input())) for _ in range(n)]
    y = n // 2
    x = 0
    total_up = 0
    total_down = 0
    total = 0
    m = 0
    total = up_total(x,y) + down_total(x,y)

    print(f'#{tc}',total)

