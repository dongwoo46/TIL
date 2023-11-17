import sys
sys.stdin = open('input', 'r')

n = int(input())
board = [[0]*1001 for _ in range(1001)]
check = []


for k in range(n):

    a,b,w,h = list(map(int, input().split()))
    check.append((a,b,w,h))
    for i in range(a,a+w):
        for j in range(b,b+h):
            board[i][j] = k+1


for i in range(n):
    cnt = 0
    a,b,w,h = check[i]
    for x in range(a,a+w):
        for y in range(b,b+h):
            if board[x][y] == i+1:
                cnt += 1

    print(cnt)
