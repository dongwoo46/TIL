import sys

sys.stdin = open('input', 'r')



def divide(board, n):
    board1 = []
    board2 = []
    board3 = []
    board4 = []
    for i in range(n//2):
        board1.append(board[i][:n//2])
        board2.append(board[i][n//2:])
    for i in range(n//2,n):
        board3.append(board[i][:n//2])
        board4.append(board[i][n//2:])

    return board1,board2,board3,board4

def color(board, n):
    global white
    global blue
    std = board[0][0]
    for i in range(n):
        for j in range(n):
            if std == 0:
                if board[i][j]!= std:
                    return False
            elif std==1:
                if board[i][j] != std:
                    return False
    else:
        if std == 0:
            white+=1
        else:
            blue +=1
        return True

def sol(board,n):
    if color(board, n):
        return
    else:
        if n>=2:
            for i in divide(board,n):
                sol(i,len(i))






n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
white = 0
blue = 0
sol(board,n)
print(white)
print(blue)
