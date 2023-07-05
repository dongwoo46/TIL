import sys
sys.stdin = open('input', 'r')

def paper(x,y,n):
    global cnt,cnt0,cnt1
    for i in range(x,x+n):
        for j in range(y,y+n):
            initial = board[x][y]
            if initial != board[i][j]:
                paper(x,y,n//3)
                paper(x,y+n//3,n//3)
                paper(x,y+2*(n//3),n//3)
                paper(x+n//3,y,n//3)
                paper(x + n // 3, y+n//3, n // 3)
                paper(x + n // 3, y+2*(n//3), n // 3)
                paper(x + 2*(n//3), y, n // 3)
                paper(x + 2*(n//3), y+n//3, n // 3)
                paper(x + 2*(n//3), y+2*(n//3), n // 3)
                return
    if initial == -1:
        cnt+=1
    elif initial == 0:
        cnt0+=1
    else:
        cnt1+=1





n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
cnt0 = 0
cnt1 = 0
cnt = 0
paper(0,0,n)

print(cnt)
print(cnt0)
print(cnt1)