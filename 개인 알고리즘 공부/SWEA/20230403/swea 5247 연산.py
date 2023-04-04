# SWEA 연산 5247
from collections import deque
import sys
sys.stdin = open('input','r')

def bfs(a,b):
    q = deque()
    q.append(a)
    visited[a] = 1
    while q:
        if visited[b]:
            return
        t = q.popleft()
        for i in [-1,+1,t,-10]:
            nt = t+i
            if 0<=nt<=1000000 and not visited[nt]:
                q.append(nt)
                visited[nt] = visited[t] + 1

T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    visited = [0]*(1000001)
    bfs(n,m)
    print(f'#{tc}',visited[m]-1)

