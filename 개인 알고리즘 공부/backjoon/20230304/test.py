import sys
sys.stdin = open('input','r')
# for _ in range(4):
cnt_x = 0
cnt_y = 0


x1,y1,x2,y2,x3,y3,x4,y4 = list(map(int,input().split()))
board1_x = [i for i in range(x1,x2+1)]
board1_y = [i for i in range(y1,y2+1)]
board2_x = [i for i in range(x3,x4+1)]
board2_y = [i for i in range(y3,y4+1)]
print(board1_x)
print(board2_x)
print(board1_y)
print(board2_y)
x_len = min(len(board1_x),len(board2_x))
y_len = min(len(board2_y),len(board2_y))
for i in range(x_len):
    if x_len == len(board1_x):
        if board1_x[i] in board2_x:
            cnt_x+=1
    else:
        if board2_x[i] in board1_x:
            cnt_x+=1

for j in range(y_len):
    if y_len == len(board1_y):
        if board1_y[j] in board2_y:
            cnt_y +=1
    else:
        if board2_y[j] in board1_y:
            cnt_y += 1
print(cnt_x,cnt_y)
if (cnt_x > 1 and cnt_y <= 1) or (cnt_y>1 and cnt_x <=1 ):
    print('b')
elif cnt_x == 1 and cnt_y == 1:
    print('c')
elif cnt_x>1 and cnt_y>1:
    print('a')
else:
    print('d')