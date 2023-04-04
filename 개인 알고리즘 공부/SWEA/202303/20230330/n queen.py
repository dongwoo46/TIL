import sys
sys.stdin = open('input')

def backtracking(i):
    global cnt
    if i==n:
        cnt +=1
        return

    else:
        for j in range(n):
            if visited1[j]==visited2[i+j]==visited3[i-j]==0:
                visited1[j]=visited2[i+j]=visited3[i-j]=1
                backtracking(i+1)
                visited1[j]=visited2[i+j]=visited3[i-j]=0


T = int(input())
for tc in range(1,T+1):
    n = int(input())
    visited1 = [0] * n
    visited2 = [0] * (2 * n)
    visited3 = [0] * (2 * n)
    # board = [list(map(int,input().split())) for _ in range(n)]
    cnt = 0
    backtracking(0)
    print(f'#{tc}',cnt)