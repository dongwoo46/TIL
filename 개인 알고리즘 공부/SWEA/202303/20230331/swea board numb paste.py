# 격자판 숫자 이어 붙이기

import sys
sys.stdin= open('../../../../input')

def backtracking(v, s, x, y):
    if v == 7:
        s_set.add(s)
        return
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x+dx,y+dy
        if 0<=nx<4 and 0<=ny<4:
            backtracking(v+1,s+board[nx][ny],nx,ny)

T = int(input())
for tc in range(1,T+1):
    board = [input().split() for _ in range(4)]
    s_set = set()

    for i in range(4):
        for j in range(4):
            backtracking(1,board[i][j],i,j)

    print(f'#{tc}', len(s_set))

