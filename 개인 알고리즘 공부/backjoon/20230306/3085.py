

def is_valid(x,y):
    return 0<=x<n and 0<=y<n

def change_board(board):
    mx = 0 
    for x in range(n-1):
        for y in range(n):
            for dx,dy in delta:
                nx = x + dx
                ny = y + dy
                if is_valid(nx,ny):
                    board[x][y], board[nx][ny] = board[nx][ny],board[x][y]
                    mx = max(mx,check_row(board[x]),check_row(board[x+1]))
                    board[nx][ny], board[x][y] = board[x][y],board[nx][ny]
    return mx

def check_row(lst):
    cnt = ans = 1
    for i in range(1,len(lst)):
        if lst[i] == lst[i-1]:
            cnt += 1
            ans = max(ans,cnt)
    return ans

n = int(input())
board = [list(input()) for _ in range(n)]
board_t = list(map(list,zip(*board)))
# board_t = [[board[j][i] for j in range(n)] for i in range(n)]

delta = [(1,0),(0,1)]
ans = max(change_board(board),change_board(board_t))
print(ans)
