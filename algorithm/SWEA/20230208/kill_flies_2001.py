import sys
sys.stdin = open('input','r')

T = int(input())

for tc in range(1,T+1):
    #n,m의 리스트를 만들어줌
    n,m = list(map(int,input().split()))
    #크기 n의 board를 만들어줌
    board = [list(map(int,input().split())) for _ in range(n)]
    #max_cnt를 정의해줌
    Max_cnt = 0
    #매행 매열마다 보드의 m*m 크기의 행렬안의 값을 다 더해서 cnt에 더하고
    #그 값이 max_cnt와 비교하여 큰 값을 max_cnt에 넣어주고 출력
    for i in range(0,n-m+1):
        for j in range(0,n-m+1):
            cnt = 0
            for k in range(i,i+m):
                for l in range(j,j+m):
                    cnt += board[k][l]
            if Max_cnt < cnt:
                Max_cnt = cnt


    print(f'#{tc} {Max_cnt}')

