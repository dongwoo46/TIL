# SWEA 최소 생산 비용

import sys
sys.stdin = open('input')

def backtracking(i):
    global total
    global mn
    if total> mn:
        return
    if i==n:
        mn = min(mn, total)

    else:
        for j in range(n):
            if visited1[j]==0:
                visited1[j]=1
                total +=board[i][j]
                backtracking(i+1)
                visited1[j]=0
                total -=board[i][j]

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    visited1 = [0]*n
    board = [list(map(int,input().split())) for _ in range(n)]
    mn = 1e9
    total = 0
    backtracking(0)
    print(f'#{tc}',mn)


