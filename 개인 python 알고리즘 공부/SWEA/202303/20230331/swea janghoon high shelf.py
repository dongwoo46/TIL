# SWEA 장훈이의 높은 선반

import sys
sys.stdin = open('../../../../input')

def backtracking(v,h):
    global mn
    if h>mn:
        return
    if v==n:
        if h>=b:
            mn = min(mn, h)
    else:
        backtracking(v+1,h+height[v])
        backtracking(v+1, h)

T = int(input())
for tc in range(1, T+1):
    n,b = map(int,input().split()) # 탐의 높이가 B이상인 탑중에서 높이가 가장낮은탑!
    height = list(map(int,input().split()))
    mn = 1e9
    visited = [0]*n
    backtracking(0,0)
    print(f'#{tc}', mn-b)