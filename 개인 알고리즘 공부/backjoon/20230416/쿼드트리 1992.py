import sys
sys.stdin = open('input','r')

n = int(input())
board = [list(map(int,input())) for _ in range(n)]
stack = []

# def check(stack):
#     if

def divide(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if board[x][y] != board[i][j]:
                stack.append('(')
                divide(x, y, n // 2)
                divide(x, y + n // 2, n // 2)
                divide(x+n//2,y,n//2)
                divide(x+n//2,y+n//2,n//2)
                stack.append(')')
                return
    stack.append(str(board[x][y]))

divide(0,0,n)
print(''.join(stack))