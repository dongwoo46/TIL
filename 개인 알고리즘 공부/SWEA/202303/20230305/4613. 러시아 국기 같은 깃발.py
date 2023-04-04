import sys
sys.stdin = open('input', 'r')

T = int(input())
for tc in range(1, T+1):
    n,m = list(map(int,input().split()))
    board = [list(input()) for _ in range(n)]
    max_ans = 0


    for i in range(n-2):
        for j in range(i+1,n-1):
            cnt = 0
            for w in range(i+1):
                cnt+=board[w].count('W')
            for b in range(i+1,j+1):
                cnt += board[b].count('B')
            for r in range(j+1,n):
                cnt += board[r].count('R')
            max_ans = max(cnt,max_ans)
    print(f'#{tc}',n*m-max_ans)

