board = [[0]*20 for _ in range(20)]
n= int(input())
for _ in range(n):
    s,e  = list(map(int,input().split()))
    for j in range(e, e + 10):
        for i in range(s, s + 10):
            board[20-j][i] = 1


for row in board:
    print(row)