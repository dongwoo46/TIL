# SWEA 요리사

import sys
sys.stdin= open('../../../input')

def score()

def backtracking(v):
    global mn

    if v == n//2:
        a = []
        b = []
        for i in range(n):
            if visited[i]:
                a.append(i)
            else:
                b.append(i)

        mn= min(mn,abs(b-a))
        return
    for i in range(v+1,n):
        if not visited[i]:
            visited[i] = 1
            backtracking(v+1)
            visited[i] = 0



T = int(input())
for tc in range(1,T+1):
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]
    mn = 1e9
    visited = [0] * n
    backtracking(0,0,0)
    print(mn)
