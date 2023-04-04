# SWEA 동철이의 일분배


def backtracking(v):
    global mx,prob
    if prob<mx:
        return
    if v == n:
        mx = max(mx,prob)
        return
    else:
        for i in range(n):
            if visited[i] == 0 and board[v][i]!=0: # 해당 열이 비어잇는지 확인하기
                visited[i] = 1
                prob *= board[v][i]/100
                backtracking(v+1)
                visited[i] = 0
                prob /= board[v][i]/100

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    board = [list(map(float,input().split())) for _ in range(n)]
    visited = [0]*n
    prob = 1
    mx = 0
    backtracking(0)
    mx =round(mx*100,6)

    a,b = str(mx).split('.')
    if len(b) <6:
        b = b + str(0)*(6-len(b))
    print(f'#{tc}', a+'.'+b)