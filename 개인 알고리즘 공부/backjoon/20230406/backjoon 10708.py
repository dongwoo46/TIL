import sys
sys.stdin = open('input','r')

board = [list(input()) for _ in range(5)]
result = [[0]*15 for _ in range(15)]

for i in range(5):
    for j in range(len(board[i])):
        result[i][j] = board[i][j]
s = ''
for i in range(15):
    for j in range(15):
        if result[j][i] != 0:
            s += result[j][i]
print(s)

