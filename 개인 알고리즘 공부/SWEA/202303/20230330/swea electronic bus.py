# SWEA 전기버스2

import sys
sys.stdin = open('input')

def backtracking(s, e, left, cnt):
    global mn
    if cnt>=mn:
        return
    if s == e:
        mn = min(mn, cnt)
        return
    else:
        for i in range(n-1):
            if stop[i]==0:
                stop[i]=1
                backtracking(s+i,e, battery[i]-1,cnt+1)
                stop[i]=0

T =int(input())
for tc in range(1, T+1):
    arr = list(map(int,input().split()))
    n = arr[0]
    stop = [0]*(n-1)
    battery = arr[1:]
    mn = 1e9
    a= 0
    left = battery[0]
    backtracking(1, n, left, 0)
    print(f'#{tc} {mn}')

