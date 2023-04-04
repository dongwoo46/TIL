# SWEA 햄버거 다이어트

import sys
sys.stdin= open('../../../../input')

def backtracking(v, score, cal):
    global mx
    if cal>l:
        return

    if v == n:
        mx = max(score, mx)
        return
    else:
        backtracking(v+1, ingred[v][0]+score, cal+ingred[v][1])
        backtracking(v + 1, score, cal)

T = int(input())
for tc in range(1,T+1):
    n, l = map(int,input().split())
    ingred = [list(map(int,input().split())) for _ in range(n)]
    mx = 0
    backtracking(0,0,0)
    print(f'#{tc}', mx)