# 블록제거하기 -> 2초
# 인벤토리 블록 쌓기 ->1초
import sys
sys.stdin = open('input', 'r')

n,m,b = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
time = 10000000000
height = 0

for h in range(0, 257):
    inven = 0
    use = 0
    for i in range(n):
        for j in range(m):
            if board[i][j]>=h:
                inven+=board[i][j]-h
            else:
                use+=h-board[i][j]
    if inven+b>=use:
        if time>=inven*2+use:
            time = inven*2+use
            height = h
print(time,height)
