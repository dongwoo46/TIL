import sys
sys.stdin = open('input','r')

n, m = list(map(int,input().split()))
chess = [input() for _ in range(n)]
board = [[0]*m for j in range(n)]

for i in range(n):
    for j in range(m):
        if chess[i][j] == 'W':
            board[i][j] = 0
        else:
            board[i][j] = 1
min_cnt = 100000000
#8*8행렬로 큰 행렬을 짜르고 만약 그 안의 합이 32에 가장 가까운것을 고름
for i in range(n-8+1):
    for j in range(m-8+1):
        eight_board = []
        cnt = 0
        if i%8==0 and j%8==0:
            for k in range(i,i+8):
                for l in range(j,j+8):
                    eight_board.append(board[k][l])
            cnt = sum(eight_board)


        # for k in range(i,i+8):
        #     for l in range(j,j+8):
        #
        #         if board[k][l] == 1:
        #             cnt+=1
        # cnt = sum(eight_board)

        if abs(cnt -32) < min_cnt:
            min_cnt = abs(cnt-32)

print(min_cnt)


#eight_board를 eight_list에 넣는다. 그리고 for문을 돌려서 각 eight_board의 열을
#각각 합해서 총 합이 32에 가장 가까운 것을 고른다. 그후 그 고른 eight_board의 총합에서
#32를 빼고 절대값을 씌우면 값이 나온다!!









