# 각 테스트 케이스의 첫 줄에는 지하 터널 지도의 세로 크기 N, 가로 크기 M, 맨홀 뚜껑이 위치한장소의 세로 위치 R, 가로 위치 C, 그리고 탈출 후 소요된 시간 L 이 주어진다.
dx = [-1,1,0,0]
dy = [0,0,-1,1]

T = int(input())
for tc in range(1,T+1):
    n,m,r,c,l = list(map(int,input().split()))
    board = [list(map(int,input().split())) for _ in range(n)]
    cnt = 0
    while l !=0:
        for i in range(n):
            for j in range(m):
                if board[r][c] == '1':
                    #상하좌우 다움직이고 nx,ny이가 벗어나지 않고 0이 아니면
                    #해당 인덱스를 리스트에 저장
                    #set으로 중복된것을 제거하고
                    #저장된 set의 값들을 각각 반복 실행하면서 재귀를 실행해야 할듯

            df