import sys
sys.stdin = open('input','r')
for _ in range(4):
    cnt_x = 0
    cnt_y = 0

    #좌표를 다 받음
    x1,y1,x2,y2,x3,y3,x4,y4 = list(map(int,input().split()))
    board1_x = [i for i in range(x1,x2+1)]
    board1_y = [i for i in range(y1,y2+1)]
    board2_x = [i for i in range(x3,x4+1)]
    board2_y = [i for i in range(y3,y4+1)]
    x_len = min(len(board1_x),len(board2_x))
    y_len = min(len(board2_y),len(board2_y))
    # 길이가 짧은것을 기준으로 짧은 리스트의 값이 긴 리스트의 값에 있으면 cnt_x를 더해줌
    for i in range(x_len):
        if x_len == len(board1_x):
            if board1_x[i] in board2_x:
                cnt_x+=1
        else:
            if board2_x[i] in board1_x:
                cnt_x+=1
    # 마찬가지로 y에 대해서도 똑같은 방법 진행
    for j in range(y_len):
        if y_len == len(board1_y):
            if board1_y[j] in board2_y:
                cnt_y +=1
        else:
            if board2_y[j] in board1_y:
                cnt_y += 1
    #만약 cnt_x가 2이상이고 cnt_y가 1이나 0 이면 선이다 반대도 동일 b출력
    if (cnt_x > 1 and cnt_y <= 0) or (cnt_y>1 and cnt_x <= 0):
        print('b')
    # cnt_x,y가 각 각 1이면 한점에서 만난다  c출력
    elif cnt_x == 1 and cnt_y == 1:
        print('c')
    # cnt_x,y 가 각각 2이상이면 직사각형이다. a출력
    elif cnt_x>1 and cnt_y>1:
        print('a')
    #나머지 만나지 않는다 d출력
    else:
        print('d')