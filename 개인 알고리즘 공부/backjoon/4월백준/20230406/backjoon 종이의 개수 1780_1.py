import sys
sys.stdin = open('input', 'r')

def paper(board,n):
    b1 = []
    b2 = []
    b3 = []
    b4 = []
    b5 = []
    b6 = []
    b7 = []
    b8 = []
    b9 = []
    for i in range(n//3):
        b1.append(board[i][:n//3])
        b2.append(board[i][n//3:2*(n//3)])
        b3.append(board[i][2*(n//3):n])

    for i in range(n//3,2*(n//3)):
        b4.append(board[i][:n // 3])
        b5.append(board[i][n // 3:2 * (n // 3)])
        b6.append(board[i][2 * (n // 3):n])

    for i in range(2*(n//3),n):
        b7.append(board[i][:n // 3])
        b8.append(board[i][n // 3:2 * (n // 3)])
        b9.append(board[i][2 * (n // 3):n])

    return b1,b2,b3,b4,b5,b6,b7,b8,b9

def judge(board, n):
    global cnt,cnt1,cnt0
    for i in range(n):
        for j in range(n):
            if board[i][j] != board[0][0]:
                return False
    else:
        if board[0][0] == -1:
            cnt+=1
        elif board[0][0] == 0:
            cnt0 +=1
        else:
            cnt1+=1
        return True

def solve(board,n):
    if judge(board,n):
        return
    else:
        if n>=3:
            for i in paper(board,n):
                solve(i, len(i))
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
cnt=cnt1=cnt0 = 0
solve(board,n)


print(cnt)
print(cnt0)
print(cnt1)
