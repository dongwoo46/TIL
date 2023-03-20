import sys
sys.stdin = open('input', 'r')
n , k = list(map(int,input().split()))
ans = 0
board = [True]*(n+1)
cnt = 0
for i in range(2,n+1):
    for j in range(i, n+1,i):
        if board[j] == True:
            board[j] = False
            cnt += 1
            if cnt == k:
                ans = j
                break

print(ans)
